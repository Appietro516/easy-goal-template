from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from database.database import *
from models.progress import *

router = APIRouter()


@router.get("/", response_description="progresses retrieved")
async def get_progresses():
    progresss = await retrieve_progresses()
    return ResponseModel(progresss, "progresses data retrieved successfully") \
        if len(progresss) > 0 \
        else ResponseModel(
        progresss, "Empty list returned")


@router.get("/{id}", response_description="progress data retrieved")
async def get_progress_data(id):
    progress = await retrieve_progress(id)
    return ResponseModel(progress, "progress data retrieved successfully") \
        if progress \
        else ErrorResponseModel("An error occured.", 404, "progress doesn't exist.")


@router.post("/", response_description="progress data added into the database")
async def add_progress_data(progress: ProgressModel = Body(...)):
    progress = jsonable_encoder(progress)
    new_progress = await add_progress(progress)
    return ResponseModel(new_progress, "progress added successfully.")


@router.delete("/{id}", response_description="progress data deleted from the database")
async def delete_progress_data(id: str):
    deleted_progress = await delete_progress(id)
    return ResponseModel("progress with ID: {} removed".format(id), "progress deleted successfully") \
        if deleted_progress \
        else ErrorResponseModel("An error occured", 404, "progress with id {0} doesn't exist".format(id))


@router.put("{id}")
async def update_progress(id: str, req: UpdateProgressModel = Body(...)):
    updated_progress = await update_progress_data(id, req.dict())
    return ResponseModel("progress with ID: {} name update is successful".format(id),
                         "progress name updated successfully") \
        if updated_progress \
        else ErrorResponseModel("An error occurred", 404, "There was an error updating the progress.".format(id))

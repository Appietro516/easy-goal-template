from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from database.database import *
from models.goal import *

router = APIRouter()


@router.get("/", response_description="Goals retrieved")
async def get_goals():
    goals = await retrieve_goals()
    return ResponseModel(goals, "Goals data retrieved successfully") \
        if len(goals) > 0 \
        else ResponseModel(
        goals, "Empty list returned")


@router.get("/{id}", response_description="Goal data retrieved")
async def get_goal_data(id):
    goal = await retrieve_goal(id)
    return ResponseModel(goal, "Goal data retrieved successfully") \
        if goal \
        else ErrorResponseModel("An error occured.", 404, "Goal doesn't exist.")


@router.post("/", response_description="Goal data added into the database")
async def add_goal_data(goal: GoalModel = Body(...)):
    goal = jsonable_encoder(goal)
    new_goal = await add_goal(goal)
    return ResponseModel(new_goal, "Goal added successfully.")


@router.delete("/{id}", response_description="Goal data deleted from the database")
async def delete_goal_data(id: str):
    deleted_goal = await delete_goal(id)
    return ResponseModel("Goal with ID: {} removed".format(id), "Goal deleted successfully") \
        if deleted_goal \
        else ErrorResponseModel("An error occured", 404, "Goal with id {0} doesn't exist".format(id))


@router.put("{id}")
async def update_goal(id: str, req: UpdateGoalModel = Body(...)):
    updated_goal = await update_goal_data(id, req.dict())
    return ResponseModel("Goal with ID: {} name update is successful".format(id),
                         "Goal name updated successfully") \
        if updated_goal \
        else ErrorResponseModel("An error occurred", 404, "There was an error updating the goal.".format(id))

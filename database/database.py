import motor.motor_asyncio
from bson import ObjectId
from decouple import config
import asyncio

from .database_helper import goal_helper, admin_helper, progress_helper

MONGO_DETAILS = config('MONGO_DETAILS')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
client.get_io_loop = asyncio.get_event_loop


database = client.goals

progress_collection = database.get_collection('progress_collection')
goal_collection = database.get_collection('goals_collection')
admin_collection = database.get_collection('admins')

async def add_admin(admin_data: dict) -> dict:
    admin = await admin_collection.insert_one(admin_data)
    new_admin = await admin_collection.find_one({"_id": admin.inserted_id})
    return admin_helper(new_admin)

#goals
async def retrieve_goals():
    goals = []
    async for goal in goal_collection.find():
        goals.append(goal_helper(goal))
    return goals


async def add_goal(goal_data: dict) -> dict:
    goal = await goal_collection.insert_one(goal_data)
    new_goal = await goal_collection.find_one({"_id": goal.inserted_id})
    return goal_helper(new_goal)


async def retrieve_goal(id: str) -> dict:
    goal = await goal_collection.find_one({"_id": ObjectId(id)})
    if goal:
        return goal_helper(goal)


async def delete_goal(id: str):
    goal = await goal_collection.find_one({"_id": ObjectId(id)})
    if goal:
        await goal_collection.delete_one({"_id": ObjectId(id)})
        return True


async def update_goal_data(id: str, data: dict):
    goal = await goal_collection.find_one({"_id": ObjectId(id)})
    if goal:
        goal_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return True
        
    
async def retrieve_goals():
    goals = []
    async for goal in goal_collection.find():
        goals.append(goal_helper(goal))
    return goals


async def add_goal(goal_data: dict) -> dict:
    goal = await goal_collection.insert_one(goal_data)
    new_goal = await goal_collection.find_one({"_id": goal.inserted_id})
    return goal_helper(new_goal)

#progress
async def retrieve_progress(id: str) -> dict:
    progress = await progress_collection.find_one({"_id": ObjectId(id)})
    if progress:
        return progress_helper(progress)


async def delete_progress(id: str):
    progress = await progress_collection.find_one({"_id": ObjectId(id)})
    if progress:
        await progress_collection.delete_one({"_id": ObjectId(id)})
        return True


async def update_progress_data(id: str, data: dict):
    progress = await progress_collection.find_one({"_id": ObjectId(id)})
    if progress:
        progress_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return True
    
async def retrieve_progresses():
    progresses = []
    async for progress in progress_collection.find():
        progresses.append(progress_helper(progress))
    return progresses


async def add_progress(progress_data: dict) -> dict:
    progress = await progress_collection.insert_one(progress_data)
    new_progress = await progress_collection.find_one({"_id": progress.inserted_id})
    return progress_helper(new_progress)

import motor.motor_asyncio
from bson import ObjectId
from decouple import config

from .database_helper import goal_helper, admin_helper

MONGO_DETAILS = config('MONGO_DETAILS')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.goals

goal_collection = database.get_collection('goals_collection')
admin_collection = database.get_collection('admins')

async def add_admin(admin_data: dict) -> dict:
    admin = await admin_collection.insert_one(admin_data)
    new_admin = await admin_collection.find_one({"_id": admin.inserted_id})
    return admin_helper(new_admin)

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

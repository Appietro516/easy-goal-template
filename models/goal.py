from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class GoalModel(BaseModel):
    name: str = Field(...)
    description: str = Field(...)
    deadline: str = Field(...)
    category: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Get an A in SWE",
                "description": "Do good demos",
                "deadline": "23:15:30 GMT+0200 (CEST)",
                "category": "Acedemic",
            }
        }


class UpdateGoalModel(BaseModel):
    name: Optional[str]
    description: Optional[EmailStr]
    deadline: Optional[str]
    category: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "name": "Get an A in SWE",
                "description": "Do good demos",
                "deadline": "23:15:30 GMT+0200 (CEST)",
                "category": "Acedemic",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [
            data
        ],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }

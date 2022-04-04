from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class ProgressModel(BaseModel):
    name: str = Field(...)
    value: str = Field(...)
    entry: str = Field(...)
    goal_name: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Get an A in SWE",
                "value": "Do good demos",
                "entry": "23:15:30 GMT+0200 (CEST)",
                "goal_name": "Acedemic",
            }
        }


class UpdateProgressModel(BaseModel):
    name: Optional[str]
    value:  Optional[EmailStr]
    entry: Optional[str]
    goal_name: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "name": "Get an A in SWE",
                "value": "Do good demos",
                "entry": "23:15:30 GMT+0200 (CEST)",
                "goal_name": "Acedemic",
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

from pydantic import BaseModel
from enum import Enum


class GenderEnum(str, Enum):
    Male = "Male"
    Female = "Female"


class User(BaseModel):
    id: int
    age: int
    gender: GenderEnum
    location: str
    user_description: str


class ChatHistory(BaseModel):
    role: str
    content: str

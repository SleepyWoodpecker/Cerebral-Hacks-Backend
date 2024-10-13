from pydantic import BaseModel
from enum import Enum


class GenderEnum(str, Enum):
    Male = "Male"
    Female = "Female"


class User(BaseModel):
    id: int
    rating: int
    explanation: str
    improvement: str
    action: str


class ChatHistory(BaseModel):
    role: str
    content: str

from pydantic import BaseModel


class Generate_Evaluation_Body(BaseModel):
    pid: str
    country: str
    tags: list[str]

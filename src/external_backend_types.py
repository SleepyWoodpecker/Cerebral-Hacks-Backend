from pydantic import BaseModel


class Generate_Evaluation_Body(BaseModel):
    pid: str
    country: str
    demographicTags: list[str]

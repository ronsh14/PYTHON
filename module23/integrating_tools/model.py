from pydantic import BaseModel
from typing import Optional,List

class Developer(BaseModel):
    name: str
    experience: Optional[int] = None


class Projects(BaseModel):
    title: str
    descrption: Optional[str] = None
    language: Optional[List[str]] = None
    lead_developer: Developer



from pydantic import BaseModel


class Course(BaseModel):
    id: int
    title: str
    description: str
    credits: int
    is_elective: bool = False
    likes: int = 0

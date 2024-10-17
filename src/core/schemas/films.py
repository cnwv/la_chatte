from pydantic import BaseModel


class FilmsRead(BaseModel):
    id: int
    name: str
    description: str
    rating: float
    picture_path: str

from pydantic import BaseModel


class Cell(BaseModel):
    x: int
    y: int

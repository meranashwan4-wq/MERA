from pydantic import BaseModel, Field


class MarkCreate(BaseModel):  # input
    subject_id: int
    score: float = Field(ge=0, le=100)
    pass


class MarkUpdate(BaseModel):
    score: float = Field(ge=0, le=100)
    pass


class MarkRead(BaseModel):
    id: int
    subject_id: int
    student_id: int
    score: float

    model_config = {"from_attributes": True}
    pass

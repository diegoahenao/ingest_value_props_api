from pydantic import BaseModel, Field
from datetime import date

class TapsCreate(BaseModel):
    day: date
    position: int = Field(ge=0)
    value_prop: str = Field(min_length=1, max_length=50)
    user_id: int = Field(ge=0)

class PrintsCreate(BaseModel):
    day: date
    position: int = Field(ge=0)
    value_prop: str = Field(min_length=1, max_length=50)
    user_id: int = Field(ge=0)

class PaysCreate(BaseModel):
    pay_date: date
    total: float = Field(ge=0)
    user_id: int = Field(ge=0)
    value_prop: str = Field(min_length=1, max_length=50)
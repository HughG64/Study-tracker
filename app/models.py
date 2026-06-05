from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class StudySession(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date: date
    hours: float
    module: str
    topics: str

class UpdateSession(SQLModel):
    hours: Optional[float] = None
    module: Optional[str] = None
    topics: Optional[str] = None
    date: Optional[date] = None

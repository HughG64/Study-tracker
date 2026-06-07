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

class Module(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str
    name: str
    credits: int
    is_complete: bool

class UpdateModule(SQLModel):
    code: Optional[str]
    name: Optional[str]
    credits: Optional[int]
    is_complete: Optional[bool]

class Assignment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    assignment_number: int
    module_id: Optional[int] = Field(default=None, foreign_key="module.id")
    due_date: date
    topics: str
    score: float
    is_complete: bool

class UpdateAssignment(SQLModel):
    assignment_number: Optional[int] = None
    due_date: Optional[date] = None
    topics: Optional[str] = None
    score: Optional[float] = None
    is_complete: Optional[bool] = None

from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from app.database import create_db_and_tables, get_session
from app.models import StudySession
from sqlmodel import Session, select

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/sessions")
def create_session(session_data: StudySession, db: Session = Depends(get_session)):
    db.add(session_data)
    db.commit()
    db.refresh(session_data)
    return session_data

@app.get("/sessions")

def get_sessions(db: Session = Depends(get_session)):
    sessions = db.exec(select(StudySession)).all()
    return sessions

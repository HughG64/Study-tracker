from fastapi import FastAPI, Depends, HTTPException
from contextlib import asynccontextmanager
from app.database import create_db_and_tables, get_session
from app.models import StudySession, UpdateSession, Module, UpdateModule
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

@app.get("/sessions/{id}")
def get_one_session(id: int, db: Session = Depends(get_session)):
    session = db.exec(select(StudySession).where(StudySession.id == id)).first()
    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    return session

@app.delete("/sessions/{id}")
def del_one_session(id: int, db:Session = Depends(get_session)):
    session = db.exec(select(StudySession).where(StudySession.id == id)).first()
    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    db.delete(session)
    db.commit()
    return {"message": "Session deleted"}

@app.patch("/sessions/{id}")
def patch_session(id: int, updates: UpdateSession, db:Session = Depends(get_session)):
    session = db.exec(select(StudySession).where(StudySession.id == id)).first()
    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")

    update_data = updates.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(session, key, value)

    db.add(session)
    db.commit()
    db.refresh(session)
    return session

@app.post("/modules")
def create_module(module_data: Module, db: Session = Depends(get_session)):
    db.add(module_data)
    db.commit()
    db.refresh(module_data)
    return module_data


@app.get("/modules")
def get_module(db: Session = Depends(get_session)):
    module = db.exec(select(Module)).all()
    return module

@app.get("/modules/{id}")
def get_one_module(id: int, db: Session = Depends(get_session)):
    module = db.exec(select(Module).where(Module.id == id)).first()
    if module is None:
        raise HTTPException(status_code=404, detail="Module not found")
    return module

@app.patch("/modules/{id}")
def patch_module(id: int, updates: UpdateModule, db: Session = Depends(get_session)):
    module = db.exec(select(Module).where(Module.id == id)).first()
    if module is None:
        raise HTTPException(status_code=404, detail="Module not found")

    update_data = updates.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(module, key, value)
    db.add(module)
    db.commit()
    db.refresh(module)
    return module

@app.delete("/modules/{id}")
def delete_module(id: int, db: Session = Depends(get_session)):
    module = db.exec(select(Module).where(Module.id == id)).first()
    if module is None:
        raise HTTPException(status_code=404, detail="Module not found")

    db.delete(module)
    db.commit()
    return {"message": "Module deleted"}

from fastapi import FastAPI
from pydantic import BaseModel, Field
from database import engine, SessionLocal
from models import Base
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from models import Todos

app = FastAPI()

Base.metadata.create_all(bind=engine)


class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(Todos).all()


@app.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency,
                      todo_request: TodoRequest):
    todo_model = Todos(**todo_request.dict())

    db.add(todo_model)
    db.commit()

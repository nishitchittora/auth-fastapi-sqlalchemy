from fastapi import FastAPI
from pydantic import Field
from app.proj_3_todo.routers import auth, todos
from database import engine
from models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)

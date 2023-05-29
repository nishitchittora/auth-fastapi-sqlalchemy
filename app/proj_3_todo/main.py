from fastapi import FastAPI
from pydantic import Field
from routers import auth, todos, admin, users
from database import engine
from models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)

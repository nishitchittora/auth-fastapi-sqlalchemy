from fastapi import FastAPI
from pydantic import BaseModel, Field
from database import engine, SessionLocal
from models import Base
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from models import Todos

router = APIRouter()


@router.get("/")
async def index():
    return {'user': "authenticate"}

from fastapi import APIRouter, status, Depends, HTTPException, Request
from pymongo.client_session import ClientSession
from pydantic_core import ValidationError
from app.db.init_db import get_session
from app.config import settings


router = APIRouter()

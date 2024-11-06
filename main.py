from fastapi import FastAPI
import sqlite3
from pydantic import BaseModel
from routes import router
from database import handle_database

app = FastAPI()

app.get('/')
async def index():
    return {"message": "Hello, GET!"}

app.include_router(router.app, tags=['router'])


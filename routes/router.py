from fastapi import APIRouter
from database import handle_database
from schemes import scheme
from models import models

app = APIRouter(
    prefix="/api",
    tags=["api"],
)

@app.get("/")
async def index():
    return {"message": "Hello, GET!"}

@app.get('/signin')
async def signin():
    

@app.post('/verify')
async def verify(data: scheme.verify):
    if handle_database.verify(data.phone_number):
        return {"message": "Already verified"}

    return models.continue_verify(data.phone_number)
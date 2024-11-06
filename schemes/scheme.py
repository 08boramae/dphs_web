from pydantic import BaseModel

class verify(BaseModel):
    phone_number: str

class signup(BaseModel):
    name: str
    phone_number: str
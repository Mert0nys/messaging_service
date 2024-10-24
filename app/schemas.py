from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class MessageCreate(BaseModel):
    recipient_id: int
    content: str

class Message(BaseModel):
    id: int
    sender_id: int
    recipient_id: int
    content: str

    class Config:
        orm_mode = True

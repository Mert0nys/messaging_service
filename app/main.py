from fastapi import FastAPI, Depends, WebSocket
from sqlalchemy.orm import Session
from .database import engine, Base, SessionLocal
from .auth import get_db, authenticate_user
from .models import User as UserModel, Message as MessageModel
from .schemas import UserCreate, MessageCreate, Message as MessageSchema

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/register/")
async def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserModel(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials")
    return {"access_token": user.username}

@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await websocket.accept()
    # Логика обработки сообщений через WebSocket.

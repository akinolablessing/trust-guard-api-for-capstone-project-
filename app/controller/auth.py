from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.data_base import SessionLocal
from app.models.agent import Agent
from app.schema.schemas import AgentCreate, AgentLogin, TokenResponse
from app.db.data_base import get_db
from app.services.auth import auth

router = APIRouter(prefix="/auth", tags=["Authentication"])



@router.post("/register")
def register(agent: AgentCreate, db: Session = Depends(get_db)):
    return auth.register(agent, db)

@router.post("/login", response_model=TokenResponse)
def login(agent: AgentLogin, db: Session = Depends(get_db)):
    return auth.login(agent, db)

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.data_base import SessionLocal
from app.models.agent import Agent
from app.schema.schemas import AgentCreate, AgentLogin, TokenResponse
from app.auth.hash import hash_password, verify_password
from app.auth.jwt_handler import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(agent: AgentCreate, db: Session = Depends(get_db)):
    existing_user = db.query(Agent).filter(Agent.email == agent.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(agent.password)
    new_agent = Agent(
        name=agent.name,
        email=agent.email,
        phone=agent.phone,
        password=hashed_password
    )
    db.add(new_agent)
    db.commit()
    db.refresh(new_agent)
    return {"message": "Agent registered successfully"}

@router.post("/login", response_model=TokenResponse)
def login(agent: AgentLogin, db: Session = Depends(get_db)):
    db_agent = db.query(Agent).filter(Agent.email == agent.email).first()
    if not db_agent or not verify_password(agent.password, db_agent.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": db_agent.email})
    return {"access_token": token, "token_type": "bearer"}

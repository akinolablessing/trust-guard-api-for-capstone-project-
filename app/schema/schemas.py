from datetime import datetime

from pydantic.v1 import BaseModel

class AgentCreate(BaseModel):
    name: str
    phone: str
    email: str
    password: str


class AgentLogin(BaseModel):
    email: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class AgentSchema(BaseModel):
    id: int
    name: str
    phone: str
    email: str
    password: str



class ReceiptSchema(BaseModel):
    parsed_text: str




class TransactionSchema(BaseModel):
    reference_id: str
    sender_name: str
    amount: float
    date: datetime



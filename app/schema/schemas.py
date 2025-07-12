from datetime import datetime

from pydantic import BaseModel, ConfigDict




class AgentCreate(BaseModel):
    name: str
    phone: str
    email: str
    password: str
    model_config = ConfigDict(from_attributes=True)


class AgentLogin(BaseModel):
    email: str
    password: str
    model_config = ConfigDict(from_attributes=True)

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    model_config = ConfigDict(from_attributes=True)

class AgentSchema(BaseModel):
    id: int
    name: str
    phone: str
    email: str
    password: str
    model_config = ConfigDict(from_attributes=True)



class ReceiptSchema(BaseModel):
    parsed_text: str
    model_config = ConfigDict(from_attributes=True)




class TransactionSchema(BaseModel):
    reference_id: str
    sender_name: str
    amount: float
    date: datetime
    model_config = ConfigDict(from_attributes=True)


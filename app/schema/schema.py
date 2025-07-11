from datetime import datetime

from pydantic.v1 import BaseModel


class AgentSchema(BaseModel):
    id: int
    name: str
    phone: str
    email: str



class ReceiptSchema(BaseModel):
    parsed_text: str




class TransactionSchema(BaseModel):
    reference_id: str
    sender_name: str
    amount: float
    date: datetime



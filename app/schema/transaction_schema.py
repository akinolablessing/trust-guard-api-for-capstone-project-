from datetime import datetime

from pydantic import BaseModel


class TransactionSchema(BaseModel):
    reference_id: str
    sender_name: str
    amount: float
    date: datetime
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Transaction:
    senderName: str
    referenceId: str
    amount: float
    receiverBankName: str
    senderBankName: str
    date: datetime

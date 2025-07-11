from dataclasses import dataclass, field
from typing import List

from app.apis.models.account import Account
from app.apis.models.transaction import Transaction


@dataclass
class Agent:
    name: str
    phone: str
    email: str
    password: str
    account: Account
    transactions: List[Transaction] = field(default_factory=list)

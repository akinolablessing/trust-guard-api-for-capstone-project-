from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.data_base import Base

class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(20), nullable=False)

    account_id = Column(Integer, ForeignKey("accounts.id"))
    account = relationship("Account", back_populates="agent")

    transactions = relationship("Transaction", back_populates="agent")

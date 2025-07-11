from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.data_base import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    sender_name = Column(String, nullable=False)
    reference_id = Column(String, nullable=False, unique=True)
    amount = Column(Float, nullable=False)
    receiver_bank_name = Column(String, nullable=False)
    sender_bank_name = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)

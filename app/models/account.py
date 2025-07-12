from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.db.data_base import Base


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    bankName = Column(String(50), nullable=False)
    accountNumber = Column(String(20),unique=True, nullable=False)
    agent = relationship("Agent", back_populates="accounts")

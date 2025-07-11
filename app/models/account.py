from sqlalchemy import Column, String

from app.db.data_base import Base


class Account(Base):
    __tablename__ = "account"

    bankName = Column(String, nullable=False)
    accountNumber = Column(String,unique=True, nullable=False)


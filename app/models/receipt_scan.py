from dataclasses import dataclass

from sqlalchemy import Column, String


@dataclass
class ReceiptScan:
    __tablename__ = "receipt_scan"
    parsed_text = Column(String, nullable=False)
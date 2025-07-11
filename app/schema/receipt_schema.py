from pydantic import BaseModel


class ReceiptSchema(BaseModel):
    parsed_text: str
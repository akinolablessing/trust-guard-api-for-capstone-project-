from pydantic.v1 import BaseModel


class AgentSchema(BaseModel):
    id: int
    name: str
    phone: str
    email: str
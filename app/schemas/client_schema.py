from pydantic import BaseModel
from typing import List
from app.schemas.category_schema import CategorySchema


class ClientNewSchema(BaseModel):
    name: str


class ClientSchema(BaseModel):
    id: int
    name: str


class ClientInfoSchema(BaseModel):
    client: ClientSchema
    accounts: List[int] = []
    categories: List[CategorySchema] = []


class ClientBalanceSchema(BaseModel):
    accounts: List[int] = []

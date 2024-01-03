from pydantic import BaseModel
from typing import List
from app.models import MovementEnum


class MovementSchema(BaseModel):
    id_account: int
    type: MovementEnum
    amount: float


class MovementBalanceItemSchema(BaseModel):
    id_account: int
    amount_pesos: float
    amount_dolar: float|str


class MovementBalanceSchema(BaseModel):
    balance: List[MovementBalanceItemSchema]

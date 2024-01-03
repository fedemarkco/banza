from pydantic import BaseModel


class AccountSchema(BaseModel):
    id_client: int


class AccountClientSchema(BaseModel):
    id: int

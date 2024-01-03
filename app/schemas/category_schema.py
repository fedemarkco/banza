from pydantic import BaseModel


class CategoryNewSchema(BaseModel):
    name: str


class CategorySchema(BaseModel):
    id: int
    name: str


class CategoryClientSchema(BaseModel):
    id_category: int
    id_client: int    

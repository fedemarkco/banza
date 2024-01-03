from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config import get_db
from app.service import create_category_service, add_client_to_category_service
from app.schemas import CategoryClientSchema, CategoryNewSchema


router = APIRouter()


@router.post("/category/")
async def create_category(category: CategoryNewSchema, db: Session = Depends(get_db)):
    return await create_category_service(category=category, db=db)

@router.post("/client_to_category/")
async def add_client_to_category(category_client: CategoryClientSchema, db: Session = Depends(get_db)):
    return await add_client_to_category_service(category_client=category_client, db=db)

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Category, CategoryClient, Client
from app.schemas.category_schema import CategoryClientSchema, CategoryNewSchema


async def create_category_service(
    category: CategoryNewSchema, db: AsyncSession
) -> Category:
    """
    A new category is added
    """
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)

    return db_category


async def add_client_to_category_service(
    category_client: CategoryClientSchema, db: AsyncSession
) -> CategoryClient:
    """
    It checks if the client and the category exist, and adds it to CategoryClient
    """
    db_client = db.query(Client).filter(Client.id == category_client.id_client).first()
    db_category = (
        db.query(Category).filter(Category.id == category_client.id_category).first()
    )

    if db_client and db_category:
        category_client = CategoryClient()
        category_client.client = db_client
        category_client.category = db_category
        db.add(category_client)
        db.commit()
        db.refresh(category_client)

        return category_client
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Client or Category not found"
        )

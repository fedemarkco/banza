from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Account, Client
from app.schemas.account_schema import AccountSchema


async def add_account_to_client_service(
    client: AccountSchema, db: AsyncSession
) -> Account:
    """
    It checks if the client exists and adds an account
    """
    db_client = db.query(Client).filter(Client.id == client.id_client).first()

    if db_client:
        db_account = Account(**client.dict())
        db.add(db_account)
        db.commit()
        db.refresh(db_account)

        return db_account
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Client not found"
        )

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config import get_db
from app.service import add_account_to_client_service
from app.schemas.account_schema import AccountSchema


router = APIRouter()


@router.post("/account_to_client/")
async def add_account_to_client(client: AccountSchema, db: Session = Depends(get_db)):
    return await add_account_to_client_service(client=client, db=db)

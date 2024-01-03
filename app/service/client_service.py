from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Account, Category, CategoryClient, Client
from app.schemas import MovementBalanceSchema
from app.schemas.category_schema import CategorySchema
from app.schemas.client_schema import (ClientInfoSchema, ClientNewSchema,
                                       ClientSchema)
from app.service.utils import AccountBalance


async def create_client_service(client: ClientNewSchema, db: AsyncSession) -> Client:
    """
    A new client is added
    """
    db_client = Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)

    return db_client


async def edit_client_service(
    id_client: int, client: ClientSchema, db: AsyncSession
) -> Client:
    """
    Client data is edited
    """
    db_client = db.query(Client).filter(Client.id == id_client).first()

    if db_client:
        db_client.name = client.name

        db.merge(db_client)
        db.commit()
        db.refresh(db_client)

    return db_client


async def delete_client_service(id_client: int, db: AsyncSession) -> Client:
    """
    Client data is deleted
    """
    db_client = db.query(Client).filter(Client.id == id_client).first()

    if db_client:
        db.delete(db_client)
        db.commit()

    return db_client


async def list_clients_service(db: AsyncSession) -> Client:
    """
    Obtain a list of clients
    """
    db_client = db.query(Client).all()

    return db_client


async def client_info_service(id_client: int, db: AsyncSession):
    """
    Obtain the accounts, categories of a client
    """
    db_client = db.query(Client).filter(Client.id == id_client).first()
    db_accounts = db.query(Account).filter(Account.id_client == id_client).all()
    db_categories = (
        db.query(Category)
        .join(CategoryClient)
        .filter(CategoryClient.id_client == id_client)
        .all()
    )

    if db_client:
        client_dict = db_client.__dict__
        accounts_list = [db_account.id for db_account in db_accounts]
        categories_list = [
            CategorySchema(**db_category.__dict__) for db_category in db_categories
        ]

        client_info_schema = ClientInfoSchema(
            client=ClientSchema(**client_dict),
            accounts=accounts_list,
            categories=categories_list,
        )
        return client_info_schema
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Client not found"
        )


async def client_balance_service(id_client: int, db: AsyncSession):
    """
    The available balance is obtained in each client account.
    It also returns the balance in dollars.
    """
    db_client = db.query(Client).filter(Client.id == id_client).first()

    if db_client:
        balance_list = []

        for db_account in db_client.accounts:
            account = AccountBalance()
            amount_pesos, amount_dolar = account.balance(db_account.movements)

            balance_list.append(
                {
                    "id_account": db_account.id,
                    "amount_pesos": amount_pesos,
                    "amount_dolar": amount_dolar,
                }
            )

        client_balance_schema = MovementBalanceSchema(balance=balance_list)
        return client_balance_schema

    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Client not found"
        )

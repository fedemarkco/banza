from fastapi import status
from fastapi import HTTPException
from app.models import Account, Movement, Account, MovementEnum
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import MovementSchema
from app.service.utils import AccountBalance


async def remove_movement_service(id_movement: int, db: AsyncSession) -> Movement:
    """
    Movement is deleted
    """
    db_movement = db.query(Movement).filter(Movement.id==id_movement).first()

    if db_movement:
        db.delete(db_movement)
        db.commit()

        return db_movement
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movement or Account not found")

async def movement_service(id_account: int, id_movement: int, db: AsyncSession):
    """
    Obtain movement information
    """
    db_movement = db.query(Movement).filter(Account.id==id_account, Movement.id==id_movement).first()

    if db_movement:
        return db_movement
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movement or Account not found")

async def create_movement_service(movement: MovementSchema, db: AsyncSession) -> Movement:
    """
    Check if the account exists.
    If a withdrawal is requested, it is checked if the client has an available balance,
    if he has an available balance, it allows him to withdraw, otherwise, an error is generated.
    If a deposit is requested, it allows you to add money to the account.
    """
    db_account = db.query(Account).filter(Account.id == movement.id_account).first()

    if db_account:
        account = AccountBalance()
        amount_pesos, amount_dolar = account.balance(db_account.movements)
        if (amount_pesos >= movement.amount and movement.type == MovementEnum.WITHDRAWAL) or (movement.type == MovementEnum.DEPOSIT):
            db_movement = Movement(**movement.dict())
            db.add(db_movement)
            db.commit()
            db.refresh(db_movement)
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="insufficient balance")
        return db_movement
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Account not found")

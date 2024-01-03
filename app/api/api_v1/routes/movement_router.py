from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config import get_db
from app.service import remove_movement_service, movement_service, create_movement_service
from app.schemas import MovementSchema


router = APIRouter()


@router.delete("/movement/{id_movement}")
async def remove_movement(id_movement: int, db: Session = Depends(get_db)):
    return await remove_movement_service(id_movement=id_movement, db=db)

@router.get("/movement/{id_account}/{id_movement}")
async def movement(id_account: int, id_movement: int, db: Session = Depends(get_db)):
    return await movement_service(id_account=id_account, id_movement=id_movement, db=db)

@router.post("/movement/")
async def create_movement(movement: MovementSchema, db: Session = Depends(get_db)):
    return await create_movement_service(movement=movement, db=db)

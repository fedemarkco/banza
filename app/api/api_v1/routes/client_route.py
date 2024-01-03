from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config import get_db
from app.service import create_client_service, edit_client_service, delete_client_service, list_clients_service, client_info_service, client_balance_service
from app.schemas import ClientSchema, ClientNewSchema


router = APIRouter()


@router.post("/client/")
async def create_client(client: ClientNewSchema, db: Session = Depends(get_db)):
    return await create_client_service(client=client, db=db)
    
@router.patch("/client/{id_client}")
async def edit_client(id_client: int, client: ClientNewSchema, db: Session = Depends(get_db)):
    return await edit_client_service(id_client=id_client, client=client, db=db)

@router.delete("/client/{id_client}")
async def delete_client(id_client: int, db: Session = Depends(get_db)):
    return await delete_client_service(id_client=id_client, db=db)

@router.get("/clients/")
async def list_clients(db: Session = Depends(get_db)):
    return await list_clients_service(db=db)

@router.get("/client_info/{id_client}")
async def client_info(id_client: int, db: Session = Depends(get_db)):
    return await client_info_service(id_client=id_client, db=db)

@router.get("/client_balance/{id_client}")
async def client_balance(id_client: int, db: Session = Depends(get_db)):
    return await client_balance_service(id_client=id_client, db=db)

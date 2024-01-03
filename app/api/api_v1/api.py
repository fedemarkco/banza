from fastapi import APIRouter

import app.api.api_v1.routes.client_route as client
import app.api.api_v1.routes.category_route as category
import app.api.api_v1.routes.account_route as account
import app.api.api_v1.routes.movement_router as movement


api_router = APIRouter()
api_router.include_router(client.router, tags=["Client"])
api_router.include_router(category.router, tags=["Category"])
api_router.include_router(account.router, tags=["Account"])
api_router.include_router(movement.router, tags=["Movement"])

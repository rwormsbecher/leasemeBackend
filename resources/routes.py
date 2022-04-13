from fastapi import APIRouter
from resources import auth
from resources import  lease_agreements


api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(lease_agreements.router)


from fastapi import APIRouter
from services.ether_mainet import eth

router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@router.get("/ether/{wallet}/{token}")
async def get_balance_wallet(wallet, token):
    return eth.get_balance_by_token(wallet, token)

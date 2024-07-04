from fastapi import APIRouter
from services.ether_mainet import eth

router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@router.get("/ether/balabce/{wallet}/{token}")
async def get_balance_wallet(wallet, token):
    return eth.get_balance_by_token(wallet, token)

@router.get("/ether/balabce/{wallet}")
async def get_balances_wallet(wallet):
    return eth.get_balance_by_eth_tokens(wallet)

from fastapi import APIRouter
from app.services.balance_sheet import fetch_balance_sheet

router = APIRouter()

@router.get('/balance-sheet')
async def get_balance_sheet():
    return fetch_balance_sheet()

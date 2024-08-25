from fastapi import APIRouter
from services.balance_sheet import fetch_balance_sheet

router = APIRouter()

"""
Sets up an API router for handling balance sheet-related requests.

Args:
- None (Router is configured directly within the module).

Returns:
- None (Router configuration does not return any value).
"""

@router.get('/balance-sheet')
async def get_balance_sheet():
    """
    Endpoint to fetch the balance sheet data.

    Args:
    - None.

    Returns:
    - dict: The balance sheet data fetched from the fetch_balance_sheet service.
    """
    return fetch_balance_sheet()

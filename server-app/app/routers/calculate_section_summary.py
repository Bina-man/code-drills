from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.services.balance_sheet import fetch_balance_sheet
from app.services.calculate_section_summary import calculate_section_summary

router = APIRouter()

"""
Sets up an API router for handling balance sheet-related requests.

Args:
- None (Router is configured directly within the module).

Returns:
- None (Router configuration does not return any value).
"""

@router.get('/summary/')
async def get_section_summary(
    report_id: str = Query(..., description="The ID of the report to search for."),
    report_type: str = Query(..., description="The type of the report (e.g., 'BalanceSheet')."),
    section_title: str = Query(..., description="The title of the section to calculate the summary for.")
):
    """
    Endpoint to fetch the summary of a specific section in the balance sheet.

    Args:
    - report_id (str): The ID of the report to search for.
    - report_type (str): The type of the report (e.g., 'BalanceSheet').
    - section_title (str): The title of the section to calculate the summary for.

    Returns:
    - dict: A dictionary containing 'sum_current' and 'sum_previous' values if the section is found.
    - HTTPException: If the report or section is not found.
    """
    # Fetch the balance sheet data
    reports = fetch_balance_sheet()

    # Calculate the section summary
    summary = calculate_section_summary(report_id, report_type, section_title, reports)
    
    if summary is None:
        raise HTTPException(status_code=404, detail="Report or section not found")

    return summary
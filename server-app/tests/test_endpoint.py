import asyncio
from datetime import datetime
import pytest
from app.main import app
from app.config.balance_types import known_balance_types
from httpx import AsyncClient

def check_balance_depth_data(data):
    # Iterate through each section in the JSON data
    for section in data[0]["Rows"]:
        section_title = section.get("Title", "Unknown")
        section_type = section.get("RowType", "Unknown")

        # Check if the section type is 'Section' and the title exists in known_balance_types
        assert section_type == "Section", f"Unexpected RowType '{section_type}' for section '{section_title}'"
        assert section_title in known_balance_types, f"Unexpected section title '{section_title}'"

        # Iterate through each row within the section
        for row in section.get("Rows", []):
            if row["RowType"] == "Row":  # Make sure we're checking rows
                row_title = row["Cells"][0]["Value"]

                # Assert that the row title exists in the known_balance_types dictionary for this section
                assert row_title in known_balance_types[section_title], f"Unexpected row '{row_title}' in section '{section_title}'"

    return True  # If all assertions pass

async def check_balance_sheet_response(ac):
    response = await ac.get("/balance-sheet")
    assert response.status_code == 200, "Expected 200 status code"
    data = response.json()
    
    # Existing checks
    assert data[0]["ReportID"] == "BalanceSheet", "Expected ReportID to match 'BalanceSheet'"
    assert data[0]["ReportName"] == "Balance Sheet", "Expected ReportName to match 'Balance Sheet'"
    
    # Additional checks for hypothetical fields
    assert data[0]["ReportType"] == "BalanceSheet", "Expected ReportType to match 'BalanceSheet'"
    assert data[0]["ReportTitles"][0] == "Balance Sheet", "Expected the first title to be 'Balance Sheet'"
    assert datetime.strptime(data[0]["ReportDate"], "%d %B %Y") == datetime.strptime("2024-08-25", "%Y-%m-%d"), "Expected ReportDate to match '2024-08-25'"
    assert "UpdatedDateUTC" in data[0], "Expected 'UpdatedDateUTC' to be present in the response"
    
    # Check if 'Fields' is a list and not empty
    assert isinstance(data[0]["Fields"], list), "Expected 'Fields' to be a list"
    
    # Checking nested data within 'Rows'
    assert data[0]["Rows"][0]["RowType"] == "Header", "Expected first row type to be 'Header'"
    assert data[0]["Rows"][1]["Title"] == "Assets", "Expected second row title to be 'Assets'"
    # data = check_balance_depth_data(data)
    return response

@pytest.mark.asyncio
async def test_balance_sheet_route_success():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        await check_balance_sheet_response(ac)

@pytest.mark.asyncio
async def test_timeout_under_load():
    url = "http://127.0.0.1:8000/balance-sheet"

    # Setup the AsyncClient with a timeout less than the expected delay
    async with AsyncClient(timeout=1.0) as ac:
        # Create multiple concurrent requests to simulate load
        tasks = [ac.get(url) for _ in range(10)]  # Adjust the range for desired concurrency level
        responses = await asyncio.gather(*tasks, return_exceptions=True)

        # Check responses for timeout exceptions
        timeouts = [isinstance(response, asyncio.TimeoutError) for response in responses]
        assert not any(timeouts), "Expected at least one timeout due to load but didn't get any."

        # Print out response statuses or exceptions for debugging
        print("Responses under load:", responses)

@pytest.mark.asyncio
async def test_balance_sheet_concurrency():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        tasks = [check_balance_sheet_response(ac) for _ in range(20)]  # Adjust the range for desired concurrency level
        responses = await asyncio.gather(*tasks)
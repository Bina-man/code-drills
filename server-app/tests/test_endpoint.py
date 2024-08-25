# import asyncio
# import pytest
# from main import app
# from httpx import AsyncClient
# from datetime import datetime
# from config.balance_types import known_balance_types

# def check_balance_depth_data(data):
#     """
#     Validates section and row titles against known_balance_types.

#     Args:
#     - data (dict): The parsed JSON data from the balance sheet report.

#     Asserts:
#     - Each section has the RowType 'Section'.
#     - Each section title exists in known_balance_types.
#     - Each row within a section has the RowType 'Row'.
#     - Each row title exists within the corresponding section in known_balance_types.
#     """
#     for section in data[0]["Rows"]:
#         section_title = section.get("Title", "Unknown")
#         section_type = section.get("RowType", "Unknown")
#         assert section_type == "Section", f"Unexpected RowType '{section_type}' for section '{section_title}'"
#         assert section_title in known_balance_types, f"Unexpected section title '{section_title}'"
#         for row in section.get("Rows", []):
#             if row["RowType"] == "Row":
#                 row_title = row["Cells"][0]["Value"]
#                 assert row_title in known_balance_types[section_title], f"Unexpected row '{row_title}' in section '{section_title}'"
#     return True

# async def check_balance_sheet_response(ac):
#     """
#     Checks the balance sheet response for expected structure and content.

#     Args:
#     - ac (AsyncClient): The async client used to make HTTP requests.

#     Asserts:
#     - The response status code is 200.
#     - The 'ReportID' matches 'BalanceSheet'.
#     - The 'ReportName' matches 'Balance Sheet'.
#     - The 'ReportType' matches 'BalanceSheet'.
#     - The first 'ReportTitle' matches 'Balance Sheet'.
#     - The 'ReportDate' matches '2024-08-25'.
#     - The 'UpdatedDateUTC' field is present.
#     - The 'Fields' is a list.
#     - The first row has RowType 'Header'.
#     - The second row title is 'Assets'.
#     """
#     response = await ac.get("/balance-sheet")
#     assert response.status_code == 200, "Expected 200 status code"
#     data = response.json()
#     assert data[0]["ReportID"] == "BalanceSheet", "Expected ReportID to match 'BalanceSheet'"
#     assert data[0]["ReportName"] == "Balance Sheet", "Expected ReportName to match 'Balance Sheet'"
#     assert data[0]["ReportType"] == "BalanceSheet", "Expected ReportType to match 'BalanceSheet'"
#     assert data[0]["ReportTitles"][0] == "Balance Sheet", "Expected the first title to be 'Balance Sheet'"
#     assert datetime.strptime(data[0]["ReportDate"], "%d %B %Y") == datetime.strptime("2024-08-25", "%Y-%m-%d"), "Expected ReportDate to match '2024-08-25'"
#     assert "UpdatedDateUTC" in data[0], "Expected 'UpdatedDateUTC' to be present in the response"
#     assert isinstance(data[0]["Fields"], list), "Expected 'Fields' to be a list"
#     assert data[0]["Rows"][0]["RowType"] == "Header", "Expected first row type to be 'Header'"
#     assert data[0]["Rows"][1]["Title"] == "Assets", "Expected second row title to be 'Assets'"
#     check_balance_depth_data(data)
#     return response

# @pytest.mark.asyncio
# async def test_balance_sheet_route_success():
#     """
#     Tests the balance sheet route for successful response and structure.

#     Args:
#     - None.

#     Asserts:
#     - The balance sheet response has the correct structure and expected values.
#     """
#     async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
#         await check_balance_sheet_response(ac)

# @pytest.mark.asyncio
# async def test_timeout_under_load():
#     """
#     Tests the balance sheet route for timeouts under load.

#     Args:
#     - None.

#     Asserts:
#     - There is no timeout when making multiple concurrent requests to the balance sheet route.
#     """
#     url = "http://127.0.0.1:8000/balance-sheet"
#     async with AsyncClient(timeout=1.0) as ac:
#         tasks = [ac.get(url) for _ in range(10)]
#         responses = await asyncio.gather(*tasks, return_exceptions=True)
#         timeouts = [isinstance(response, asyncio.TimeoutError) for response in responses]
#         assert not any(timeouts), "Expected at least one timeout due to load but didn't get any."
#         print("Responses under load:", responses)

# @pytest.mark.asyncio
# async def test_balance_sheet_concurrency():
#     """
#     Tests the balance sheet route for concurrency handling.

#     Args:
#     - None.

#     Asserts:
#     - The balance sheet route handles multiple concurrent requests correctly.
#     """
#     async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
#         tasks = [check_balance_sheet_response(ac) for _ in range(20)]
#         responses = await asyncio.gather(*tasks)

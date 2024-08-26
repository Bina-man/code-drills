from typing import Dict, Any, Optional

def calculate_section_summary(report_id: str, report_type: str, section_title: str, reports: list) -> Optional[Dict[str, float]]:
    """
    Calculate the sum of the current and previous values for a specific section
    in a report based on the report ID, report type, and section title.

    Parameters:
    - report_id (str): The ID of the report to search for.
    - report_type (str): The type of the report (e.g., 'BalanceSheet').
    - section_title (str): The title of the section to calculate the summary for.
    - reports (list): The list of reports from which to search.

    Returns:
    - dict: A dictionary containing 'sum_current' and 'sum_previous' values if the section is found.
    - None: If the report or section is not found.
    """
    # Find the specific report by report_id and report_type
    report = next((r for r in reports if r['ReportID'] == report_id and r['ReportType'] == report_type), None)
    if report is None:
        return None

    # Calculate the summary for the given section
    for row in report['Rows']:
        if row['RowType'] == 'Section' and row['Title'] == section_title:
            current_sum = 0.0
            previous_sum = 0.0

            for sub_row in row.get('Rows', []):
                if sub_row['RowType'] == 'Row':
                    current_value = float(sub_row['Cells'][1]['Value'].replace(',', ''))
                    previous_value = float(sub_row['Cells'][2]['Value'].replace(',', ''))
                    current_sum += current_value
                    previous_sum += previous_value

            return {'sum_current': current_sum, 'sum_previous': previous_sum}

    # If the section is not found, return None
    return None

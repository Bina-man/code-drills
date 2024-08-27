# services/report_service.py

from typing import Any, Dict, Optional
from app.models.report import ReportModel
from app.services.balance_sheet import fetch_balance_sheet

class ReportService(ReportModel):
    def __init__(self, report_type: str, organization_name: str):
        super().__init__(report_type, organization_name)
        self.reports = self.__fetch_reports__()

    def __fetch_reports__(self):
        # Fetch the balance sheet data
        data = fetch_balance_sheet()

        # Check if the organization name matches the one in the data
        if data and isinstance(data, list) and 'ReportTitles' in data[0]:
            report_titles = data[0]['ReportTitles']
            if len(report_titles) >= 2 and report_titles[1] == self.organization_name:
                return data
        return None

    def calculate_section_summary(self, report_id: str, section_title: str) -> Optional[Dict[str, float]]:
        # Fetch the balance sheet data
        reports = self.reports

        # Debug: Print the reports data and the provided report_id and report_type
        print(f"Reports: {reports}")
        print(f"Provided Report ID: {report_id}")
        print(f"Provided Report Type: {self.report_type}")

        # Check all report IDs and Types in the data
        for r in reports:
            print(f"Comparing Report ID: {r['ReportID']} == {report_id} -> {r['ReportID'] == report_id}")
            print(f"Comparing Report Type: {r['ReportType']} == {self.report_type} -> {r['ReportType'] == self.report_type}")

        # Find the specific report by report_id and report_type
        report = next(
            (r for r in reports if r['ReportID'] == report_id and r['ReportType'] == self.report_type), None)

        # Debug: Print the selected report
        print(f"Selected Report: {report}")

        if report is None:
            return None

        # Calculate the summary for the given section
        for row in report['Rows']:
            if row['RowType'] == 'Section' and row['Title'] == section_title:
                current_sum = 0.0
                previous_sum = 0.0

                for sub_row in row.get('Rows', []):
                    if sub_row['RowType'] == 'Row':
                        try:
                            current_value = float(sub_row['Cells'][1]['Value'].replace(',', ''))
                            previous_value = float(sub_row['Cells'][2]['Value'].replace(',', ''))
                            current_sum += current_value
                            previous_sum += previous_value
                        except (ValueError, IndexError):
                            # Handle cases where conversion fails or cells are missing
                            continue

                return {'sum_current': current_sum, 'sum_previous': previous_sum}

        # If the section is not found, return None
        return None

# models/report.py

from typing import Dict, Any, Optional

class ReportModel:
    def __init__(self, report_type: str, organization_name: str):
        self.report_type = report_type
        self.organization_name = organization_name

    def get_report_details(self) -> Dict[str, Any]:
        """
        Should return detailed information about the report.
        """
        raise NotImplementedError("This method should be implemented by the service layer.")
    
    def fetch_and_process_report(self) -> Dict[str, Any]:
        """
        Should fetch the report data and process it.
        """
        raise NotImplementedError("This method should be implemented by the service layer.")

    def calculate_section_summary(self, report_id: str, section_title: str) -> Optional[Dict[str, float]]:
        """
        Should calculate the sum of the current and previous values for a specific section in the report.
        """
        raise NotImplementedError("This method should be implemented by the service layer.")

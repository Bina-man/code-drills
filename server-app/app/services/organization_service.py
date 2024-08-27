# services/organization_service.py

from typing import Dict, Any
from app.models.organization import OrganizationModel
from app.services.balance_sheet import fetch_balance_sheet
from app.utils.date_utils import extract_report_date

class OrganizationService(OrganizationModel):
    def __init__(self, organization_name: str):
        super().__init__(organization_name)
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

    def get_organization_name(self):
        # Now implemented in the service layer
        return self.organization_name
    
    def get_information(self) -> Dict[str, Any]:
        # Relying on ReportTitles for detailed information
        if self.reports and isinstance(self.reports, list) and 'ReportTitles' in self.reports[0]:
            report_titles = self.reports[0]['ReportTitles']
            
            # Extract the details from the ReportTitles
            if len(report_titles) >= 3:
                report_type = report_titles[0]
                organization_name = report_titles[1]
                report_date_str = report_titles[2]
                
                # Extract and process the report date
                date_info = extract_report_date(report_date_str)
                
                if "error" in date_info:
                    return date_info  # Return the error if date extraction fails
                
                return {
                    "report_type": report_type,
                    "organization_name": organization_name,
                    "report_date_original": date_info["report_date_original"],
                    "report_date_extracted": date_info["report_date_extracted"]
                }
            else:
                return {"error": "Report titles format is incorrect"}
        else:
            return {"error": "No valid reports data found"}
        
        # services/organization_service.py

    def get_organization_details(organization_name: str, token: str):
        # Logic to retrieve organization details
        pass

    def update_organization_details(organization_name: str, token: str, updated_data: dict):
        # Logic to update organization details
        pass

    def create_organization(organization_data: dict, token: str):
        # Logic to create a new organization
        pass

    def delete_organization(organization_name: str, token: str):
        # Logic to delete an organization
        pass


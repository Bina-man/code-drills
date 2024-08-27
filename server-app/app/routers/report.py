from fastapi import APIRouter, HTTPException, Query
from app.services.report_service import ReportService

router = APIRouter()

@router.get('/summary/')
async def get_section_summary(
    organization_name: str = Query(..., description="The name of the organization."),
    report_id: str = Query(..., description="The ID of the report to search for."),
    report_type: str = Query(..., description="The type of the report (e.g., 'BalanceSheet')."),
    section_title: str = Query(..., description="The title of the section to calculate the summary for.")
):
    report_service = ReportService(report_type=report_type, organization_name=organization_name)
    section_summary = report_service.calculate_section_summary(report_id=report_id, section_title=section_title)
 
    if section_summary is None:
        raise HTTPException(status_code=404, detail="Report or section not found")

    return section_summary

from fastapi import APIRouter, Body, HTTPException, Query
from app.services.organization_service import OrganizationService

router = APIRouter()

@router.get('/details/')
async def get_organization_details(
    organization_name: str = Query(..., description="The name of the organization."),
    token: str = Query(None, description="Optional authentication token.")
):
    service = OrganizationService(organization_name)
    details = service.get_information()

    if 'error' in details:
        raise HTTPException(status_code=404, detail=details['error'])

    return details


@router.put('/update/')
async def update_organization_details(
    organization_name: str = Query(..., description="The name of the organization to update."),
    updated_data: dict = Body(None, description="Optional update data."),
    token: str = Query(None, description="Optional authentication token.")
):
    service = OrganizationService(organization_name)
    
    
    result = service.update_organization_details(updated_data, token)
    
    if 'error' in result:
        raise HTTPException(status_code=400, detail=result['error'])

    return {"message": "Organization updated successfully", "updated_organization": result}



@router.post('/create/')
async def create_organization(
    organization_data: dict = Body(..., description="The data for the new organization."),  # Use Body to accept JSON data
    token: str = Query(None, description="Optional authentication token.")
):
    service = OrganizationService(organization_data['organization_name'])
    
    # Implement your logic for creating a new organization
    result = service.create_organization(organization_data, token)
    
    if 'error' in result:
        raise HTTPException(status_code=400, detail=result['error'])

    return {"message": "Organization created successfully", "new_organization": result}

@router.delete('/delete/')
async def delete_organization(
    organization_name: str = Query(..., description="The name of the organization to delete."),
    token: str = Query(None, description="Optional authentication token.")
):
    service = OrganizationService(organization_name)
    
    # Implement your logic for deleting the organization
    result = service.delete_organization(token)
    
    if 'error' in result:
        raise HTTPException(status_code=400, detail=result['error'])

    return {"message": "Organization deleted successfully"}

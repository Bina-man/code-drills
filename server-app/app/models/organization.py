# models/organization.py

class OrganizationModel:
    def __init__(self, organization_name: str):
        self.organization_name = organization_name

    def get_organization_name(self):
        """
        Should return the name of the organization.
        """
        raise NotImplementedError("This method should be implemented by the service layer.")

    def get_information(self):
        """
        Should return detailed information about the organization.
        """
        raise NotImplementedError("This method should be implemented by the service layer.")

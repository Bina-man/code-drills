import pytest
from app.services.organization_service import OrganizationService
from unittest.mock import patch

# Mock data for testing
mock_balance_sheet_data = [
    {
        'ReportID': 'BalanceSheet',
        'ReportName': 'Balance Sheet',
        'ReportType': 'BalanceSheet',
        'ReportTitles': ['Balance Sheet', 'Demo Org', 'As at 26 August 2024'],
        'ReportDate': '26 August 2024',
        'Rows': []
    }
]

@pytest.fixture
def organization_service():
    with patch('app.services.organization_service.fetch_balance_sheet') as mock_fetch:
        mock_fetch.return_value = mock_balance_sheet_data
        service = OrganizationService(organization_name='Demo Org')
        yield service

def test_get_organization_name(organization_service):
    assert organization_service.get_organization_name() == 'Demo Org'

def test_get_information(organization_service):
    info = organization_service.get_information()
    assert info['report_type'] == 'Balance Sheet'
    assert info['organization_name'] == 'Demo Org'
    assert info['report_date_original'] == 'As at 26 August 2024'
    assert info['report_date_extracted'].strftime('%Y-%m-%d') == '2024-08-26'

def test_get_information_no_report_found():
    with patch('app.services.organization_service.fetch_balance_sheet', return_value=[]):
        service = OrganizationService(organization_name='Unknown Org')
        info = service.get_information()
        assert info == {"error": "No valid reports data found"}

def test_get_information_invalid_format():
    invalid_data = [{'ReportTitles': ['Balance Sheet']}]
    with patch('app.services.organization_service.fetch_balance_sheet', return_value=invalid_data):
        service = OrganizationService(organization_name='Demo Org')
        info = service.get_information()
        assert info == {"error": "No valid reports data found"}


def test_get_information_date_parsing_error():
    invalid_date_data = [
        {
            'ReportID': 'BalanceSheet',
            'ReportTitles': ['Balance Sheet', 'Demo Org', 'Invalid Date String']
        }
    ]
    with patch('app.services.organization_service.fetch_balance_sheet', return_value=invalid_date_data):
        service = OrganizationService(organization_name='Demo Org')
        info = service.get_information()
        assert 'error' in info and 'Date parsing error' in info['error']

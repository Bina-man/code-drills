from unittest.mock import patch
from app.services.report_service import ReportService

def test_calculate_section_summary_valid():
    valid_data = [
        {
            'ReportID': 'BalanceSheet',
            'ReportType': 'BalanceSheet',
            'ReportTitles': ['Balance Sheet', 'Demo Org', 'As at 26 August 2024'],
            'Rows': [
                {'RowType': 'Section', 'Title': 'Bank', 'Rows': [
                    {'RowType': 'Row', 'Cells': [
                        {'Value': 'My Bank Account'},
                        {'Value': '126.70'},
                        {'Value': '99.60'}
                    ]},
                    {'RowType': 'Row', 'Cells': [
                        {'Value': 'Sample Business'},
                        {'Value': '92911.00'},
                        {'Value': '92911.00'}
                    ]}
                ]}
            ]
        }
    ]
    with patch('app.services.report_service.fetch_balance_sheet', return_value=valid_data):
        service = ReportService(report_type='BalanceSheet', organization_name='Demo Org')
        summary = service.calculate_section_summary(report_id='BalanceSheet', section_title='Bank')
        assert summary == {'sum_current': 93037.7, 'sum_previous': 93010.6}

def test_calculate_section_summary_invalid_report_id():
    valid_data = [
        {
            'ReportID': 'OtherReport',
            'ReportType': 'BalanceSheet',
            'ReportTitles': ['Balance Sheet', 'Demo Org', 'As at 26 August 2024'],
            'Rows': []
        }
    ]
    with patch('app.services.report_service.fetch_balance_sheet', return_value=valid_data):
        service = ReportService(report_type='BalanceSheet', organization_name='Demo Org')
        summary = service.calculate_section_summary(report_id='BalanceSheet', section_title='Bank')
        assert summary is None

def test_calculate_section_summary_invalid_section_title():
    valid_data = [
        {
            'ReportID': 'BalanceSheet',
            'ReportType': 'BalanceSheet',
            'ReportTitles': ['Balance Sheet', 'Demo Org', 'As at 26 August 2024'],
            'Rows': [
                {'RowType': 'Section', 'Title': 'Assets', 'Rows': []}
            ]
        }
    ]
    with patch('app.services.report_service.fetch_balance_sheet', return_value=valid_data):
        service = ReportService(report_type='BalanceSheet', organization_name='Demo Org')
        summary = service.calculate_section_summary(report_id='BalanceSheet', section_title='Bank')
        assert summary is None

def test_calculate_section_summary_empty_data():
    with patch('app.services.report_service.fetch_balance_sheet', return_value=[]):
        service = ReportService(report_type='BalanceSheet', organization_name='Demo Org')
        summary = service.calculate_section_summary(report_id='BalanceSheet', section_title='Bank')
        assert summary is None

from app.services.calculate_section_summary import calculate_section_summary

def test_calculate_section_summary():
    # Test data
    reports = [
        {
            'ReportID': 'BalanceSheet',
            'ReportType': 'BalanceSheet',
            'Rows': [
                {
                    'RowType': 'Section',
                    'Title': 'Bank',
                    'Rows': [
                        {'RowType': 'Row', 'Cells': [{'Value': 'My Bank Account'}, {'Value': '126.70'}, {'Value': '99.60'}]},
                        {'RowType': 'Row', 'Cells': [{'Value': 'Sample Business'}, {'Value': '92911.00'}, {'Value': '92911.00'}]},
                        {'RowType': 'Row', 'Cells': [{'Value': 'Sample Business 1'}, {'Value': '11039.00'}, {'Value': '11039.00'}]}
                    ]
                },
                {
                    'RowType': 'Section',
                    'Title': 'Assets',
                    'Rows': []
                }
            ]
        }
    ]

    # Case 1: Valid report and section
    result = calculate_section_summary('BalanceSheet', 'BalanceSheet', 'Bank', reports)
    assert result == {'sum_current': 104076.7, 'sum_previous': 104049.6}

    # Case 2: Non-existent report
    result = calculate_section_summary('NonExistentReport', 'BalanceSheet', 'Bank', reports)
    assert result is None

    # Case 3: Non-existent section
    result = calculate_section_summary('BalanceSheet', 'BalanceSheet', 'NonExistentSection', reports)
    assert result is None

    # Case 4: Report with no matching section rows
    result = calculate_section_summary('BalanceSheet', 'BalanceSheet', 'Assets', reports)
    assert result == {'sum_current': 0.0, 'sum_previous': 0.0}

    # Case 5: Empty reports list
    result = calculate_section_summary('BalanceSheet', 'BalanceSheet', 'Bank', [])
    assert result is None

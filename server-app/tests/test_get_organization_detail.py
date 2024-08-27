import unittest
from datetime import datetime
from app.utils.date_utils import extract_report_date


class TestExtractReportDate(unittest.TestCase):

    def test_valid_date(self):
        report_date_str = "As at 26 August 2024"
        result = extract_report_date(report_date_str)
        expected_date = datetime(2024, 8, 26)
        
        self.assertEqual(result["report_date_original"], report_date_str)
        self.assertEqual(result["report_date_extracted"], expected_date)

    def test_invalid_date_format(self):
        report_date_str = "As at 26th August 2024"  # Invalid format
        result = extract_report_date(report_date_str)
        
        self.assertIn("error", result)
        self.assertTrue("Date parsing error" in result["error"])

    def test_empty_date_string(self):
        report_date_str = ""
        result = extract_report_date(report_date_str)
        
        self.assertIn("error", result)
        self.assertTrue("Date parsing error" in result["error"])

if __name__ == '__main__':
    unittest.main()

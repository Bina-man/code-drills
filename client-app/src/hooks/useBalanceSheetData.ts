// src/hooks/useBalanceSheetData.ts
import { useState, useEffect } from 'react';
import { fetchBalanceSheet, getSummary } from '../services/api'; // Ensure the import paths are correct
import { Report } from '../type'; // Import any necessary types

const useBalanceSheetData = () => {
  const [report, setReport] = useState<Report | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [summaries, setSummaries] = useState<{ [key: string]: { sum_current: number; sum_previous: number } }>({});

  useEffect(() => {
    const loadData = async () => {
      try {
        const data = await fetchBalanceSheet();
        setReport(data[0]);

        // Fetch summaries for each section
        const sectionSummaries: { [key: string]: { sum_current: number; sum_previous: number } } = {};
        for (const row of data[0].Rows) {
          if (row.RowType === 'Section' && row.Title) {
            try {
              // Update this line to include the correct number of arguments
              const summary = await getSummary(
                'Demo Org', // Organization name
                data[0].ReportID, // Report ID
                data[0].ReportType, // Report Type
                row.Title // Section Title
              );
              sectionSummaries[row.Title] = summary;
            } catch (err) {
              console.error(`Failed to fetch summary for ${row.Title}:`, err);
            }
          }
        }
        setSummaries(sectionSummaries);
      } catch (err) {
        setError('Failed to fetch balance sheet data or summaries. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, []);

  return { report, loading, error, summaries };
};

export default useBalanceSheetData;

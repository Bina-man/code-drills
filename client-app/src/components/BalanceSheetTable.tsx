import React, { useEffect, useState } from 'react';
import { fetchBalanceSheet } from '../services/api';
import { Report, Row } from '../type';

const BalanceSheetTable: React.FC = () => {
  const [report, setReport] = useState<Report | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [expandedSections, setExpandedSections] = useState<{ [key: string]: boolean }>({});

  useEffect(() => {
    const loadData = async () => {
      try {
        const data = await fetchBalanceSheet();
        setReport(data[0]); // Assuming you're returning an array of reports and you're interested in the first one
        setLoading(false);
      } catch (err) {
        setError('Failed to fetch balance sheet data');
        setLoading(false);
      }
    };

    loadData();
  }, []);

  const toggleSection = (title: string) => {
    setExpandedSections((prev) => ({
      ...prev,
      [title]: !prev[title],
    }));
  };

  const renderRows = (rows: Row[]) =>
    rows.map((row, index) => (
      <React.Fragment key={index}>
        {row.RowType === 'Section' && (
          <>
            <tr onClick={() => toggleSection(row.Title || `section-${index}`)} style={{ cursor: 'pointer' }}>
              <td colSpan={3}><strong>{row.Title}</strong></td>
            </tr>
            {expandedSections[row.Title || `section-${index}`] && row.Rows && renderRows(row.Rows)}
          </>
        )}
        {row.RowType === 'Row' && (
          <tr>
            {row.Cells.map((cell, cellIndex) => (
              <td key={cellIndex}>{cell.Value}</td>
            ))}
          </tr>
        )}
      </React.Fragment>
    ));

  if (loading) return <p>Loading...</p>;
  if (error) return <p>{error}</p>;
  if (!report) return <p>No data available</p>;

  return (
    <div>
      <h2>{report.ReportName}</h2>
      <table>
        <thead>
          <tr>
            <th>Account</th>
            <th>Amount (Current)</th>
            <th>Amount (Previous)</th>
          </tr>
        </thead>
        <tbody>{renderRows(report.Rows)}</tbody>
      </table>
    </div>
  );
};

export default BalanceSheetTable;

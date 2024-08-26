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
        setReport(data[0]);
      } catch (err) {
        setError('Failed to fetch balance sheet data. Please try again later.');
      } finally {
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
            <tr
              onClick={() => toggleSection(row.Title || `section-${index}`)}
              style={{
                cursor: 'pointer',
                backgroundColor: '#E8F0FE',
                color: '#333',
                padding: '12px 16px',
                fontSize: '18px',
                fontWeight: 'bold',
              }}
            >
              <td colSpan={3} style={{ padding: '12px 16px' }}>
                {row.Title}
                <span style={{ float: 'right', fontSize: '14px', color: '#555' }}>
                  {expandedSections[row.Title || `section-${index}`] ? 'Hide Details' : 'See More'}
                </span>
              </td>
            </tr>
            {expandedSections[row.Title || `section-${index}`] && row.Rows && (
              <>
                {renderRows(row.Rows)}
                <tr style={{ backgroundColor: '#F9FAFB' }}>
                  <td colSpan={3} style={{ padding: '12px 16px', fontWeight: 'bold' }}>
                    Summary of {row.Title}
                  </td>
                </tr>
              </>
            )}
          </>
        )}
        {row.RowType === 'Row' && (
          <tr style={{ backgroundColor: '#fff', borderBottom: '1px solid #ddd' }}>
            {row.Cells.map((cell, cellIndex) => (
              <td key={cellIndex} style={{ padding: '12px 16px', fontSize: '16px' }}>
                {cell.Value}
              </td>
            ))}
          </tr>
        )}
      </React.Fragment>
    ));

  if (loading) return <p>Loading balance sheet data...</p>;
  if (error) return <p className="error">{error}</p>;
  if (!report) return <p>No data available.</p>;

  return (
    <div style={{ width: '100%', padding: '20px', boxSizing: 'border-box' }}>
      <h2 style={{ textAlign: 'center', fontSize: '24px', marginBottom: '20px' }}>{report.ReportName}</h2>
      <table
        style={{
          width: '100%',
          borderCollapse: 'collapse',
          boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)',
        }}
      >
        <thead>
          <tr style={{ backgroundColor: '#4A5568', color: '#fff', fontSize: '18px' }}>
            <th style={{ padding: '12px 16px', textAlign: 'left' }}>Account</th>
            <th style={{ padding: '12px 16px', textAlign: 'left' }}>Amount (Current)</th>
            <th style={{ padding: '12px 16px', textAlign: 'left' }}>Amount (Previous)</th>
          </tr>
        </thead>
        <tbody>{renderRows(report.Rows)}</tbody>
      </table>
    </div>
  );
};

export default BalanceSheetTable;

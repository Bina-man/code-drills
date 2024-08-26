// src/components/BalanceSheetTable.tsx
import React, { useState } from 'react';
import useBalanceSheetData from '../hooks/useBalanceSheetData';
import RenderRows from './RenderRows';

const BalanceSheetTable: React.FC = () => {
  const { report, loading, error, summaries } = useBalanceSheetData();
  const [expandedSections, setExpandedSections] = useState<{ [key: string]: boolean }>({});

  const toggleSection = (title: string) => {
    setExpandedSections((prev) => ({
      ...prev,
      [title]: !prev[title],
    }));
  };

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
        <tbody>
          <RenderRows rows={report.Rows} expandedSections={expandedSections} toggleSection={toggleSection} summaries={summaries} />
        </tbody>
      </table>
    </div>
  );
};

export default BalanceSheetTable;

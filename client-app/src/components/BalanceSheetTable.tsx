// src/components/BalanceSheetTable.tsx
import React, { useState } from 'react';
import useBalanceSheetData from '../hooks/useBalanceSheetData';
import RenderRows from './RenderRows';
import OrganizationHeader from './OrganizationHeader';

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
    <div style={{ display: 'flex', flexDirection: 'column', minHeight: '100vh', width: '100%' }}>
      <OrganizationHeader
        organizationName={report.ReportTitles[1]}
        reportDate={new Date(report.ReportDate).toLocaleDateString()}
      />
      <div style={{ flexGrow: 1, padding: '20px', backgroundColor: '#f4f4f4' }}>
        <h2 style={{ textAlign: 'center', fontSize: '24px', marginBottom: '20px' }}>{report.ReportName}</h2>
        <table
          style={{
            width: '100%',
            borderCollapse: 'collapse',
            boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)',
            backgroundColor: '#e7edf8',
          }}
        >
          <tbody>
            <RenderRows rows={report.Rows} expandedSections={expandedSections} toggleSection={toggleSection} summaries={summaries} />
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default BalanceSheetTable;

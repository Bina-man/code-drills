import React from 'react';
import OrganizationHeader from './OrganizationHeader';
import BalanceSheetTable from './BalanceSheetTable';
import useBalanceSheetData from '../../hooks/useBalanceSheetData';

const BalanceSheetPage: React.FC = () => {
  const { report, loading, error, summaries } = useBalanceSheetData();

  if (loading) return <p>Loading balance sheet data...</p>;
  if (error) return <p className="error">{error}</p>;
  if (!report) return <p>No data available.</p>;

  return (
    <div style={{ display: 'flex', flexDirection: 'column', minHeight: '100vh', width: '100%' }}>
      <OrganizationHeader
        organizationName={report.ReportTitles[1]}
        reportDate={new Date(report.ReportDate).toLocaleDateString()}
      />
      <div style={{ flexGrow: 1, width: '100%', padding: '0 20px', backgroundColor: '#f4f4f4' }}>
        <BalanceSheetTable report={report} summaries={summaries} />
      </div>
    </div>
  );
};

export default BalanceSheetPage;

import React, { useState } from 'react';
import { TableContainer, TableTitle } from '../../styles/balanceSheetStyles';
import RenderRows from '../RenderRows/RenderRows';

interface BalanceSheetTableProps {
  report: any;
  summaries: any;
}

const BalanceSheetTable: React.FC<BalanceSheetTableProps> = ({ report, summaries }) => {
  const [expandedSections, setExpandedSections] = useState<{ [key: string]: boolean }>({});

  const toggleSection = (title: string) => {
    setExpandedSections((prev) => ({
      ...prev,
      [title]: !prev[title],
    }));
  };

  return (
    <TableContainer>
      <TableTitle>{report.ReportName}</TableTitle>
      <table>
          <RenderRows rows={report.Rows} expandedSections={expandedSections} toggleSection={toggleSection} summaries={summaries} />
      </table>
    </TableContainer>
  );
};

export default BalanceSheetTable;

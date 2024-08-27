import React, { useState } from 'react';
import RenderRows from './RenderRows';
import { TableContainer, TableTitle } from '../../styles/balanceSheetStyles';

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
        <tbody>
          <RenderRows rows={report.Rows} expandedSections={expandedSections} toggleSection={toggleSection} summaries={summaries} />
        </tbody>
      </table>
    </TableContainer>
  );
};

export default BalanceSheetTable;

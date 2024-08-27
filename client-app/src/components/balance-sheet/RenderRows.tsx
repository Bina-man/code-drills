import React from 'react';

const RenderRows: React.FC<{ rows: any; expandedSections: any; toggleSection: any; summaries: any }> = ({
  rows,
  expandedSections,
  toggleSection,
  summaries,
}) => {
  return (
    <>
      {rows.map((row: any) => (
        // Row rendering logic here
        // Use expandedSections, toggleSection, summaries props as needed
        <div key={row.Title}>
          {/* Render row data */}
        </div>
      ))}
    </>
  );
};

export default RenderRows;

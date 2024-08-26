// src/components/RenderRows.tsx
import React from 'react';
import { Row } from '../type';

const RenderRows: React.FC<{ 
  rows: Row[], 
  expandedSections: { [key: string]: boolean }, 
  toggleSection: (title: string) => void, 
  summaries: { [key: string]: { sum_current: number; sum_previous: number } } 
}> = ({ rows, expandedSections, toggleSection, summaries }) => {
  return (
    <>
      {rows.map((row, index) => {
        const sectionTitle = row.Title || `section-${index}`;
        return (
          <React.Fragment key={index}>
            {row.RowType === 'Section' && (
              <>
                <tr
                  onClick={() => toggleSection(sectionTitle)}
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
                      {expandedSections[sectionTitle] ? 'Hide Details' : 'See More'}
                    </span>
                  </td>
                </tr>
                {expandedSections[sectionTitle] && row.Rows && (
                  <>
                    {/* Add a table header when a section is expanded */}
                    <tr style={{ backgroundColor: '#4A5568', color: '#fff', fontSize: '18px' }}>
                      <th style={{ padding: '12px 16px', textAlign: 'left' }}>Account</th>
                      <th style={{ padding: '12px 16px', textAlign: 'left' }}>Amount (Current)</th>
                      <th style={{ padding: '12px 16px', textAlign: 'left' }}>Amount (Previous)</th>
                    </tr>

                    {/* Recursively render nested rows */}
                    <RenderRows rows={row.Rows} expandedSections={expandedSections} toggleSection={toggleSection} summaries={summaries} />

                    {/* Add a summary row at the end of each expanded section */}
                    <tr style={{ backgroundColor: '#F9FAFB' }}>
                      <td colSpan={3} style={{ padding: '12px 16px', fontWeight: 'bold' }}>
                        Summary of {row.Title}: Current - {summaries[sectionTitle]?.sum_current || 'N/A'}, Previous - {summaries[sectionTitle]?.sum_previous || 'N/A'}
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
        );
      })}
    </>
  );
};

export default RenderRows;

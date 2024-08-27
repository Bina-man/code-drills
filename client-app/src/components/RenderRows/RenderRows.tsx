import React from 'react';
import { Row } from '../../type';
import styles from './RenderRows.module.css'; // Assuming you create a CSS module for styles

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
                  className={styles.sectionHeader} // Apply CSS class
                >
                  <td colSpan={3} className={styles.sectionTitle}>
                    {row.Title}
                    <span className={styles.sectionToggle}>
                      {expandedSections[sectionTitle] ? 'Hide Details' : 'See More'}
                    </span>
                  </td>
                </tr>
                {expandedSections[sectionTitle] && row.Rows && (
                  <>
                    <tr className={styles.tableHeader}>
                      <th className={styles.tableHeaderCell}>Account</th>
                      <th className={styles.tableHeaderCell}>Amount (Current)</th>
                      <th className={styles.tableHeaderCell}>Amount (Previous)</th>
                    </tr>

                    {/* Recursively render nested rows */}
                    <RenderRows rows={row.Rows} expandedSections={expandedSections} toggleSection={toggleSection} summaries={summaries} />

                    {/* Add a summary row at the end of each expanded section */}
                    <tr className={styles.summaryRow}>
                      <td colSpan={3} className={styles.summaryCell}>
                        Summary of {row.Title}: Current - {summaries[sectionTitle]?.sum_current || 'N/A'}, Previous - {summaries[sectionTitle]?.sum_previous || 'N/A'}
                      </td>
                    </tr>
                  </>
                )}
              </>
            )}
            {row.RowType === 'Row' && (
              <tr className={styles.dataRow}>
                {row.Cells.map((cell, cellIndex) => (
                  <td key={cellIndex} className={styles.dataCell}>
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

import axios from 'axios';

const API_URL = 'http://localhost:8000';

// Fetch the balance sheet data
export const fetchBalanceSheet = async () => {
  try {
    console.log("Fetching balance sheet data...");
    const response = await axios.get(`${API_URL}/balance-sheet`);
    console.log("Balance sheet data:", response.data);
    return response.data; // Return the JSON data
  } catch (error) {
    console.error('Error fetching balance sheet data:', error);
    throw error; // Rethrow the error to be caught in your component
  }
};

// Fetch the summary data for a specific section
export const getSummary = async (reportId: string, reportType: string, sectionTitle: string) => {
  try {
    console.log(`Fetching summary for ${sectionTitle}...`);
    const response = await axios.get(`${API_URL}/summary/`, {
      params: {
        report_id: reportId,
        report_type: reportType,
        section_title: sectionTitle,
      },
    });
    console.log(`Summary for ${sectionTitle}:`, response.data);
    return response.data; // Return the JSON data
  } catch (error) {
    console.error(`Error fetching summary for ${sectionTitle}:`, error);
    throw error; // Rethrow the error to be caught in your component
  }
};

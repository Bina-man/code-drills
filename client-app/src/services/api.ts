// src/services/api.ts
import axios from 'axios';

const API_URL = 'http://localhost:8000/balance-sheet';

export const fetchBalanceSheet = async () => {
  try {
    console.log("Hello world")
    const response = await axios.get(API_URL);
    console.log(response)
    return response.data; // Ensure that you return the JSON data
  } catch (error) {
    console.error('Error fetching balance sheet data:', error);
    throw error; // Rethrow the error to be caught in your component
  }
};

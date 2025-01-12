import React, { useState } from 'react';
import axios from 'axios';

// API URL from environment variables
const API_URL = process.env.REACT_APP_API_URL;

/**
 * Utility to handle API errors
 * @param {Object} error - The error object from Axios
 * @returns {Object} Standardized error response
 */
export const handleApiError = (error) => {
  if (error.response) {
    // Server responded with a status outside 2xx range
    console.error('Response Error:', error.response.data);
    return {
      success: false,
      message: error.response.data.message || 'An error occurred on the server.',
    };
  } else if (error.request) {
    // Request made but no response received
    console.error('No Response Error:', error.request);
    return {
      success: false,
      message: 'No response received from the server.',
    };
  } else {
    // Other errors
    console.error('General Error:', error.message);
    return {
      success: false,
      message: error.message || 'An unknown error occurred.',
    };
  }
};

/**
 * API call to predict polymer properties
 * @param {Object} data - The payload to send to the API
 * @returns {Object} The API response or error object
 */
export const predictPolymerProperties = async (data) => {
  try {
    const response = await axios.post(`${API_URL}/predict/`, data);
    return { success: true, data: response.data }; // Return the API response data
  } catch (error) {
    return handleApiError(error); // Handle error and return standardized response
  }
};

/**
 * Loader component for displaying a loading indicator
 * @param {Object} props
 * @param {string} props.message - Message to display alongside the loader
 */
const Loader = ({ message = 'Loading...' }) => {
  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
      <div>
        <div
          className="spinner"
          style={{
            width: '50px',
            height: '50px',
            border: '5px solid #ccc',
            borderTop: '5px solid #333',
            borderRadius: '50%',
            animation: 'spin 1s linear infinite',
          }}
        ></div>
        <p>{message}</p>
      </div>
    </div>
  );
};

/**
 * PolymerPredictor component to predict polymer properties
 */
const PolymerPredictor = () => {
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  const handlePredict = async () => {
    setLoading(true);
    setError(null);
    const response = await predictPolymerProperties({ exampleData: 'sample' });
    if (response.success) {
      setData(response.data);
    } else {
      setError(response.message);
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: '20px', textAlign: 'center' }}>
      <h1>Polymer Property Predictor</h1>
      {loading && <Loader />}
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {data && (
        <div style={{ marginTop: '20px' }}>
          <h2>Prediction Result:</h2>
          <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
      )}
      <button
        onClick={handlePredict}
        style={{
          padding: '10px 20px',
          backgroundColor: '#007bff',
          color: '#fff',
          border: 'none',
          borderRadius: '5px',
          cursor: 'pointer',
        }}
      >
        Predict
      </button>
    </div>
  );
};

export default PolymerPredictor;

/**
 * Styles for the loader spinner
 */
const styleTag = document.createElement('style');
styleTag.innerHTML = `
  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
`;
document.head.appendChild(styleTag);

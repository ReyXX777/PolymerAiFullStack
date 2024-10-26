// PolymerAiFullStack/frontend/public/src/components/PolymerForm.js

import React, { useState } from 'react';
import axios from 'axios';

const PolymerForm = ({ setPredictions }) => {
  const [formData, setFormData] = useState({
    structure: '',
    additives: '',
    temperature: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/predict', {
        structure: formData.structure,
        additives: formData.additives.split(',').map(item => item.trim()),
        temperature: parseFloat(formData.temperature)
      });
      setPredictions(response.data.predictions);
    } catch (error) {
      console.error("Error fetching predictions:", error);
      alert("Failed to fetch predictions. Please check the input and try again.");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="mt-4">
      <div className="mb-3">
        <label htmlFor="structure" className="form-label">Polymer Structure</label>
        <input
          type="text"
          id="structure"
          name="structure"
          className="form-control"
          value={formData.structure}
          onChange={handleChange}
          required
        />
      </div>
      <div className="mb-3">
        <label htmlFor="additives" className="form-label">Additives (comma-separated)</label>
        <input
          type="text"
          id="additives"
          name="additives"
          className="form-control"
          value={formData.additives}
          onChange={handleChange}
          required
        />
      </div>
      <div className="mb-3">
        <label htmlFor="temperature" className="form-label">Temperature (°C)</label>
        <input
          type="number"
          id="temperature"
          name="temperature"
          className="form-control"
          value={formData.temperature}
          onChange={handleChange}
          required
        />
      </div>
      <button type="submit" className="btn btn-primary">Get Predictions</button>
    </form>
  );
};

export default PolymerForm;

// PolymerAiFullStack/frontend/public/src/components/Predictions.js

import React from "react";

const Predictions = ({ predictions }) => {
  return (
    <div className="mt-4">
      <h3>Predicted Properties</h3>
      <ul className="list-group">
        <li className="list-group-item">
          <strong>Glass Transition Temperature:</strong> {predictions.glass_transition_temp} °C
        </li>
        <li className="list-group-item">
          <strong>Mechanical Strength:</strong> {predictions.mechanical_strength} MPa
        </li>
        <li className="list-group-item">
          <strong>Thermal Stability:</strong> {predictions.thermal_stability} °C
        </li>
      </ul>
    </div>
  );
};

export default Predictions;

// PolymerAiFullStack/frontend/public/src/components/FeedbackForm.js

import React, { useState } from "react";

const FeedbackForm = () => {
  const [feedback, setFeedback] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    alert("Thank you for your feedback!");
    setFeedback("");
  };

  return (
    <div className="mt-5">
      <h4>Feedback</h4>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <textarea
            className="form-control"
            rows="4"
            placeholder="Enter your feedback here..."
            value={feedback}
            onChange={(e) => setFeedback(e.target.value)}
            required
          ></textarea>
        </div>
        <button type="submit" className="btn btn-primary mt-2">
          Submit Feedback
        </button>
      </form>
    </div>
  );
};

export default FeedbackForm;

// Commit message: "Add FeedbackForm component to gather user input"

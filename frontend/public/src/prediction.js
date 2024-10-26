// PolymerAiFullStack/frontend/public/src/components/Predictions.js

import React from 'react';

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

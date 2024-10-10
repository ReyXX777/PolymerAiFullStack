import React from 'react';

const Predictions = ({ predictions }) => {
  return (
    <div className="mt-4">
      <h3>Predicted Properties</h3>
      <ul className="list-group">
        <li className="list-group-item">Glass Transition Temperature: {predictions.glass_transition_temp.toFixed(2)} °C</li>
        <li className="list-group-item">Mechanical Strength: {predictions.mechanical_strength.toFixed(2)} MPa</li>
        <li className="list-group-item">Thermal Stability: {predictions.thermal_stability.toFixed(2)} °C</li>
      </ul>
    </div>
  );
};

export default Predictions;

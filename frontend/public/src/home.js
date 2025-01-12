// PolymerAiFullStack/frontend/public/src/pages/Home.js

import React, { useState } from "react";
import PolymerForm from "../components/PolymerForm";
import Predictions from "../components/Predictions";
import Tips from "../components/Tips";

const Home = () => {
  const [predictions, setPredictions] = useState(null);

  return (
    <div className="container mt-5">
      <h2>PolymerAI Property Prediction</h2>
      <p>Input polymer structure details to get predictions for glass transition temperature, mechanical strength, and more.</p>
      <PolymerForm setPredictions={setPredictions} />
      {predictions && <Predictions predictions={predictions} />}
      <Tips />
    </div>
  );
};

export default Home;

// PolymerAiFullStack/frontend/public/src/components/Tips.js

import React from "react";

const Tips = () => {
  return (
    <div className="mt-4">
      <h3>Tips for Accurate Predictions</h3>
      <ul>
        <li>Ensure polymer structure details are accurate and well-defined.</li>
        <li>Provide additives as comma-separated values with no spaces.</li>
        <li>Temperature values should be in degrees Celsius and numeric.</li>
      </ul>
    </div>
  );
};

export default Tips;

// PolymerAiFullStack/frontend/public/src/components/Predictions.js

import React from "react";

const Predictions = ({ predictions }) => {
  return (
    <div className="mt-4">
      <h3>Prediction Results</h3>
      <ul>
        {predictions.map((prediction, index) => (
          <li key={index}>
            <strong>{prediction.property}:</strong> {prediction.value} {prediction.unit}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Predictions;

// Commit message: "Add Tips and Predictions components to enhance Home page functionality"

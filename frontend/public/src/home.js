// PolymerAiFullStack/frontend/public/src/pages/Home.js

import React, { useState } from 'react';
import PolymerForm from '../components/PolymerForm';
import Predictions from '../components/Predictions';

const Home = () => {
  const [predictions, setPredictions] = useState(null);

  return (
    <div className="container mt-5">
      <h2>PolymerAI Property Prediction</h2>
      <p>Input polymer structure details to get predictions for glass transition temperature, mechanical strength, and more.</p>
      <PolymerForm setPredictions={setPredictions} />
      {predictions && <Predictions predictions={predictions} />}
    </div>
  );
};

export default Home;

// PolymerAiFullStack/frontend/public/src/index.js

import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter as Router } from "react-router-dom";
import App from "./App";
import ThemeProvider from "./components/ThemeProvider";
import ErrorBoundary from "./components/ErrorBoundary";

ReactDOM.render(
  <React.StrictMode>
    <Router>
      <ErrorBoundary>
        <ThemeProvider>
          <App />
        </ThemeProvider>
      </ErrorBoundary>
    </Router>
  </React.StrictMode>,
  document.getElementById("root")
);

// Commit message: "Add ThemeProvider and ErrorBoundary to enhance application structure"

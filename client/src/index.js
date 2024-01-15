import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter as Router } from "react-router-dom";
import App from "./App";

ReactDOM.render(
  <div style={{ backgroundColor: "lightblue" }}>
    <React.StrictMode>
      <Router>
        <App />
      </Router>
    </React.StrictMode>
  </div>,
  document.getElementById("root")
);

// PolymerAiFullStack/frontend/public/src/components/Header.js

import React from "react";
import { Link } from "react-router-dom";

const Header = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <div className="container">
        <Link to="/" className="navbar-brand">PolymerAI</Link>
        <div className="collapse navbar-collapse">
          <ul className="navbar-nav ml-auto">
            <li className="nav-item">
              <Link to="/" className="nav-link">Home</Link>
            </li>
            <li className="nav-item">
              <Link to="/about" className="nav-link">About</Link>
            </li>
            <li className="nav-item">
              <Link to="/gallery" className="nav-link">Gallery</Link>
            </li>
            <li className="nav-item">
              <Link to="/contact" className="nav-link">Contact</Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Header;

// PolymerAiFullStack/frontend/public/src/components/Sidebar.js

import React from "react";
import { Link } from "react-router-dom";

const Sidebar = () => {
  return (
    <aside style={styles.sidebar}>
      <ul style={styles.list}>
        <li>
          <Link to="/resources" style={styles.link}>Resources</Link>
        </li>
        <li>
          <Link to="/tutorials" style={styles.link}>Tutorials</Link>
        </li>
        <li>
          <Link to="/faq" style={styles.link}>FAQ</Link>
        </li>
      </ul>
    </aside>
  );
};

const styles = {
  sidebar: {
    width: "200px",
    padding: "20px",
    backgroundColor: "#f8f9fa",
    borderRight: "1px solid #ddd",
  },
  list: {
    listStyleType: "none",
    padding: 0,
  },
  link: {
    display: "block",
    color: "#007bff",
    textDecoration: "none",
    padding: "10px 0",
  },
};

export default Sidebar;

// Commit message: "Add Sidebar and Gallery links to the Header and navigation"

import { React } from "react";
import { Link } from "react-router-dom";
import "../styles/home.css";

const Ribbon = () => {
  //let isLoggedIn = JSON.parse(localStorage.getItem("authenticated"));if (!isLoggedIn) {
  function logout() {
    localStorage.setItem("authenticated", "false");
    localStorage.removeItem("username");
  }

  if (JSON.parse(localStorage.getItem("authenticated"))) {
    return (
      <div align="right">
        <Link to="/" onClick={logout}>
          <button style={{ marginRight: 5 }}>Logout</button>
        </Link>
        <Link to="/configpage">
          <button style={{ marginRight: 5 }}>Config</button>
        </Link>
        Welcome {JSON.parse(localStorage.getItem("username"))}
      </div>
    );
  } else {
    return (
      <div align="right">
        <Link to="/login">
          <button style={{ marginRight: 5 }}>Login</button>
        </Link>
      </div>
    );
  }
};

export default Ribbon;

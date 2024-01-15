import { React } from "react";
import { Link } from "react-router-dom";
import "../styles/home.css";

const Ribbon = () => {
  //let isLoggedIn = JSON.parse(localStorage.getItem("authenticated"));if (!isLoggedIn) {
  function logout() {
    localStorage.setItem("authenticated", "false");
    localStorage.removeItem("username");
    window.location.reload(false);
  }

  if (JSON.parse(localStorage.getItem("authenticated"))) {
    return (
      <div style={{ display: "flex", justifyContent: "space-between" }}>
        <img
          src={require("../styles/icons/logo.jpg")}
          alt="logo"
          width={"4%"}
          height={"4%"}
        />
        <div align="right">
          <Link to="/" onClick={logout}>
            <button style={{ marginRight: 5 }}>Logout</button>
          </Link>
          <Link to="/configpage">
            <button style={{ marginRight: 5 }}>Config</button>
          </Link>
          Welcome {JSON.parse(localStorage.getItem("username"))}
        </div>
      </div>
    );
  } else {
    return (
      <div style={{ display: "flex", justifyContent: "space-between" }}>
        <img
          src={require("../styles/icons/logo.jpg")}
          alt="logo"
          width={"4%"}
          height={"4%"}
        />
        <div align="right">
          <Link to="/login">
            <button style={{ marginRight: 5 }}>Login</button>
          </Link>
        </div>
      </div>
    );
  }
};

export default Ribbon;

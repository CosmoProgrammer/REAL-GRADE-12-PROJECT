import { React } from "react";
import { Link } from "react-router-dom";
import "../styles/home.css";

const Ribbon = () => {
  let isLoggedIn = JSON.parse(localStorage.getItem("authenticated"));
  if (!isLoggedIn) {
    return <div> Ribbon </div>;
  }
};

export default Ribbon;

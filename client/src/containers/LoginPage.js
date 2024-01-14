import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../styles/InventorySchemaEditor.css";

const LoginPage = ({ client }) => {
  const navigate = useNavigate();

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    client.get(`/login/${username}/${password}`).then((response) => {
      if (response.data) {
        localStorage.setItem("username", JSON.stringify(username));
        localStorage.setItem("authenticated", "true");
        navigate("/home");
      } else {
        alert("Credentials failed");
      }
    });
  };

  return (
    <>
      <br />
      <br />
      <fieldset>
        <legend>Login Form</legend>
        <form onSubmit={handleSubmit}>
          <label>
            Username:
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
          </label>
          <br />
          <label>
            Password:
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </label>
          <br />
          <br />
          <button type="submit">Login</button>
        </form>
      </fieldset>
    </>
  );
};

export default LoginPage;

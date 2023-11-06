import "./App.css";
import "react-toastify/dist/ReactToastify.css";
import { Routes as Switch, Route } from "react-router-dom";
import axios from "axios";
import NoPageFound from "./containers/NoPageFound";
import Ribbon from "./containers/Ribbon";
import HomePage from "./containers/Home";
import ConfigPage from "./containers/ConfigPage";

const client = axios.create({
  baseURL: "http://127.0.0.1:5000/",
});

function App() {
  return (
    <>
      <Ribbon />
      <Switch>
        <Route path="/" exact element={<HomePage />} />
        <Route
          path="/configpage"
          exact
          element={<ConfigPage client={client} />}
        />
        <Route path="*" element={<NoPageFound />} />
      </Switch>
    </>
  );
}

export default App;

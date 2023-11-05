import "./App.css";
import "react-toastify/dist/ReactToastify.css";
import { Routes as Switch, Route } from "react-router-dom";
import NoPageFound from "./containers/NoPageFound";
import Ribbon from "./containers/Ribbon";
import HomePage from "./containers/Home";
import InventorySchemaEditor from "./containers/InventorySchemaEditor";
import UserCreation from "./containers/UserCreation";

function App() {
  return (
    <>
      <Ribbon />
      <Switch>
        <Route path="/" exact element={<HomePage />} />
        <Route path="/schematester" exact element={<InventorySchemaEditor />} />
        <Route path="/usercreationtester" exact element={<UserCreation />} />
        <Route path="*" element={<NoPageFound />} />
      </Switch>
    </>
  );
}

export default App;

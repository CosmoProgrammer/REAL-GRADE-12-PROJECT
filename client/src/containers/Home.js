import React, { useEffect, useState } from "react";
import Table from "./DynamicTable";
import { useNavigate } from "react-router-dom";
import SearchBar from "./SearchBar";

const HomePage = ({ client }) => {
  const navigate = useNavigate();
  const [tableData, setTableData] = useState([]);
  const [schema, setSchema] = useState({});
  const [isLoading, setLoading] = useState(true);

  useEffect(() => {
    console.log("USE EFFECT");
    client
      .get(`getdata`)
      .then((response) => {
        let s = eval(response.data.schema);
        setTableData(response.data.data);
        setSchema(s);
        console.log(tableData, s);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching data: ", error);
      });
  }, []);

  /*const schema = [
    { name: "ID", type: "number", subColumns: [] },
    { name: "Public/NonPublic", type: "string", subColumns: [] },
    {
      name: "Qty",
      type: "number",
      subColumns: [
        { name: "Public", type: "number" },
        { name: "Private", type: "number" },
      ],
    },
    { name: "Industry", type: "string", subColumns: [] },
    {
      name: "Types",
      type: "string",
      subColumns: [
        { name: "Taste", type: "string" },
        { name: "Colour", type: "string" },
        { name: "Smell", type: "string" },
      ],
    },
    { name: "Edit", type: "button", subColumns: [] },
    { name: "Delete", type: "button", subColumns: [] },
  ];

  const data = [
    [1, "Public", [5, 10], "Cooking", ["Sweet", "Green", "Pungent"]],
    [2, "Public", [6, 20], "Baking", ["Sour", "Blue", "Pleasant"]],
    [3, "NonPublic", [5, 5], "Cooking", ["Spicy", "Green", "None"]],
  ];*/

  const [searchQuery, setSearchQuery] = useState("");

  const handleSearch = (query) => {
    setSearchQuery(query);
  };

  const filteredData = tableData.filter((row) => {
    return row.some((item) => {
      return item.toString().toLowerCase().includes(searchQuery.toLowerCase());
    });
  });

  const onEdit = (id) => {
    navigate(`/editrow/${id}`);
  };

  const onDelete = (id) => {
    client
      .post(`deleterow/${id}`)
      .then((response) => {
        console.log("Row delete: ", response.data);
        navigate("/home");
      })
      .catch((error) => {
        console.error("Error updating row: ", error);
      });
  };

  const onAdd = (id) => {
    navigate(`/addrow/9348023840293848230948`);
  };

  if (isLoading) {
    return <div className="loadingContainer">Loading</div>;
  }
  return (
    <>
      <br />
      <br />
      <SearchBar onSearch={handleSearch} />
      <br />
      <br />
      <Table
        schema={schema}
        data={filteredData}
        onEdit={onEdit}
        onDelete={onDelete}
      />
      <br />
      <button onClick={() => onAdd()} align="right">
        Add Entry
      </button>
    </>
  );
};

export default HomePage;

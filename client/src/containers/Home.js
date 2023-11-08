import React from "react";
import Table from "./DynamicTable";

const HomePage = (props) => {
  //Insert method to retrieve data from the server here
  const schema = [
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
  ];

  const data = [
    [1, "Public", [5, 10], "Cooking", ["Sweet", "Green", "Pungent"]],
    [2, "Public", [6, 20], "Baking", ["Sour", "Blue", "Pleasant"]],
    [3, "NonPublic", [5, 5], "Cooking", ["Spicy", "Green", "None"]],
  ];

  return <Table schema={schema} data={data} />;
};

export default HomePage;

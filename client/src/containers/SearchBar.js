import React, { useState } from "react";
import "../styles/SearchBar.css";

const SearchBar = ({ onSearch }) => {
  const [query, setQuery] = useState("");

  const handleChange = (e) => {
    setQuery(e.target.value);
    onSearch(e.target.value);
  };

  return (
    <input
      className="search-bar"
      type="search"
      value={query}
      onChange={handleChange}
      placeholder="Search..."
    />
  );
};

export default SearchBar;

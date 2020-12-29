import { React, useState } from "react";
import "./App.css";
import SearchBar from "./SearchBar";
import Movie from "./Movie";

function App() {
  const data = ["Thor", "Thor: The Dark World", "Thor 2", "Thor 3"];
  const [searchText, setSearchText] = useState("");
  const handleSearch = async (e) => {
    e.preventDefault();
    const response = await fetch("http://127.0.0.1:5000/search-movie", {
      method: "POST", // *GET, POST, PUT, DELETE, etc.
      mode: "no-cors", // no-cors, *cors, same-origin
      // cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
      // credentials: "same-origin", // include, *same-origin, omit
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ keyword: searchText }), // body data type must match "Content-Type" header
    });
    // const data = await response.json();
    // console.log(data);
  };
  return (
    <div className="container">
      <h3>Movie recomander app</h3>

      <SearchBar
        searchText={searchText}
        setSearchText={setSearchText}
        handleSearch={handleSearch}
      />
      <Movie />

      <div className="search-results">
        {data.map((item) => (
          <span key={item} className="badge bg-primary m-2 p-2">
            {item}
          </span>
        ))}
      </div>
    </div>
  );
}

export default App;

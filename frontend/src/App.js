import { React, useState } from "react";
import "./App.css";
import SearchBar from "./SearchBar";
import Movie from "./Movie";

function App() {
  const [data, setData] = useState([]);
  const [searchText, setSearchText] = useState("");

  const handleSearch = async (e) => {
    e.preventDefault();
    const response = await fetch(
      `http://127.0.0.1:5000/search-movie?keyword=${searchText}`
    );
    const responseData = await response.json();
    console.log(responseData);
    setData(responseData);
  };
  const handleSelectMovie = async (movieSelected) => {
    const response = await fetch(
      `http://127.0.0.1:5000/recommended-movies?movie=${movieSelected}`,
      {
        method: "GET", // *GET, POST, PUT, DELETE, etc.
        mode: "no-cors", // no-cors, *cors, same-origin
      }
    );
    const responseData = await response.json();
    console.log(responseData);
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
        {Object.keys(data).map((key) => (
          <span
            key={key}
            onClick={() => handleSelectMovie(data[key])}
            className="badge bg-primary m-2 p-2"
          >
            {data[key]}
          </span>
        ))}
      </div>
    </div>
  );
}

export default App;

import { React, useState } from "react";
import "./App.css";
import SearchBar from "./SearchBar";
import Movie from "./Movie";

function App() {
  const [searchedMovies, setSearchedMovies] = useState([]);
  const [recommendedMovies, setRecommendedMovies] = useState([]);
  const [searchText, setSearchText] = useState("");
  const [isLoading, setLoading] = useState(false);
  const [showRecommendedMovies, setShowRecommendedMovies]=useState(false)

  const handleSearch = async (e) => {
    e.preventDefault();
    const response = await fetch(
      `http://127.0.0.1:5000/search-movie?keyword=${searchText}`
    );
    const responseData = await response.json();
   setShowRecommendedMovies(false)
    setSearchedMovies(responseData);
  };

  const handleSelectMovie = async (movieSelected) => {
    setLoading(true);
    const response = await fetch(
      `http://127.0.0.1:5000/recommended-movies?movie=${movieSelected}`
    );
    const responseData = await response.json();
    setRecommendedMovies(responseData);
    setShowRecommendedMovies(true)
    setLoading(false);
  };
  return (
    <div className="container">
      <h3>MovieMatch</h3>

      <SearchBar
        searchText={searchText}
        setSearchText={setSearchText}
        handleSearch={handleSearch}
      />
      {isLoading?
      <h2 className="text-center my-3">Please wait, we are searching the best movies for you...</h2>:
      showRecommendedMovies?
      (
      <div className="d-flex flex-wrap">
        {recommendedMovies.map(item=>(
          <Movie key={item.title} info={item} />
        ))}
      </div>
      ):(
      <div className="search-results">
        {Object.keys(searchedMovies).map((key) => (
          <span
            key={key}
            onClick={() => handleSelectMovie(searchedMovies[key])}
            className="badge bg-primary m-2 p-2"
          >
            {searchedMovies[key]}
          </span>
        ))}
      </div>

      )}

    </div>
  );
}

export default App;

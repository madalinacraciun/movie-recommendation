import React from "react";

const SearchBar = ({ searchText, setSearchText, handleSearch }) => {
  return (
    <form className="form-inline mr-auto d-flex" onSubmit={handleSearch}>
      <input
        value={searchText}
        onChange={(e) => setSearchText(e.target.value)}
        className="form-control mr-sm-2"
        type="text"
        placeholder="Search"
        aria-label="Search"
      />
      <button
        className="btn btn-outline-primary btn-rounded btn-sm my-0"
        type="submit"
      >
        Search
      </button>
    </form>
  );
};
export default SearchBar;

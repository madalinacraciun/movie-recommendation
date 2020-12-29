import React from 'react';

const SearchBar = ()=>{
    const handleSearch = async(e)=>{
        e.preventDefault();

    }
    return(
    <form className="form-inline mr-auto d-flex" onSubmit={handleSearch}>
        <input className="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search"/>
        <button className="btn btn-outline-primary btn-rounded btn-sm my-0" type="submit">Search</button>
    </form>
    )
}
export default SearchBar;
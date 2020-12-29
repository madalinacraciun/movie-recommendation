import React from "react";

const Movie = ({info}) => {
  return (
    <div className="card m-2" style={{ width: "18rem" }}>
      <div className="card-body">
        <h5 className="card-title">{info.title}</h5>
        <h6 className="card-subtitle mb-2 text-muted">{info.year}</h6>
        <p className="card-text">
          Genre: {info.genre}
        </p>
        <p className="card-text">
          Actors: {info.actors}
        </p>
        <p className="card-text">
          Director: {info.director}
        </p>
        
       
      </div>
    </div>
  );
};
export default Movie;

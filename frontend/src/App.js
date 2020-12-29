import './App.css';
import SearchBar from './SearchBar'
import Movie from './Movie';



function App() {
  const data = ["Thor","Thor: The Dark World","Thor 2","Thor 3"]
  return (
    <div className="container">
      <h3>Movie recomander app</h3>
      
      <SearchBar/>
      <Movie/>
      
      <div className="search-results">
        {data.map(item=>(
          <span key="item" className="badge bg-primary m-2 p-2">{item}</span>
        )
        )}
       
      </div>
      
    </div>
  );
}

export default App;

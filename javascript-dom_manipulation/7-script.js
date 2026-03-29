async function getMovies() {
  const response = await fetch("https://swapi-api.hbtn.io/api/films/?format=json");
  const data = await response.json();
  const myMovieList = document.getElementById("list_movies");
  
  for (const movie of data.results) {
    const newListItem = document.createElement("li");
    newListItem.textContent = movie.title;
    myMovieList.appendChild(newListItem);
  }
}
getMovies();

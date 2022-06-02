const btnSearch = document.querySelector(".btn-search-movie");
const movieNameInput = document.querySelector("#movie-name");
const moviesDiv = document.querySelector(".movies");
const errorMessage = document.querySelector(".error-message");

const API_URL = 'http://localhost:5000';

let movies = [];
let filteredMovies = [];

window.addEventListener('load', () => {
    loadMovies()
})

function searchMovie(e) {
    e.preventDefault();
    let searchValue = e.target.value.trim().toLowerCase();
    if (!!searchValue && searchValue.length > 0) {
        filteredMovies = movies.filter(movie => movie.titulo.toLowerCase().includes(searchValue))
        clearMovies();
        displayMovies(filteredMovies);
    } else {
        clearMovies();
        displayMovies(movies);
    }
}

async function loadMovies() {
    try {
        let response = await fetch(`${API_URL}/filmes`)
        movies = await response.json()
        console.log(movies)
        displayMovies(movies)
    } catch (error) {
        errorMessage.classList.toggle('error-message');
    }
}

function displayMovies(movies) {
    movies.forEach(movie => {
        const box = document.createElement('div');
        box.setAttribute('class', 'box');
        box.dataset.id = movie.filme_id
        box.innerHTML = `
            <img src="${movie.imagem}" alt="Foto do filme: ${movie.titulo}">
            <div class="box-divider">
              <p><span>${movie.titulo}</span> <span>Likes ${movie.likes}</span></p>
              <p>${movie.descricao}</p>
            </div>`
        moviesDiv.appendChild(box);
    })
}

function clearMovies() {
    while(moviesDiv.firstChild) {
        moviesDiv.firstChild.remove()
    }
}

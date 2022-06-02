const btnSearch = document.querySelector(".btn-search-movie");
const movieNameInput = document.querySelector("#movie-name");
const moviesDiv = document.querySelector(".movies");
const errorMessage = document.querySelector(".error-message");
const userLabel = document.querySelector('#user-label');
const loginLogout = document.querySelector('#login-logout')
const listaLabel = document.querySelector('#minha-lista-label')
const API_URL = 'http://localhost:5000';

let movies = [];
let filteredMovies = [];
let userMovies = [];
let user = JSON.parse(localStorage.getItem('user')) || null;

window.addEventListener('load', () => {
    loadMovies()
    if (user) {
        userLabel.textContent = `Olá ${user.nome}`;
        loginLogout.textContent = 'logout'
        listaLabel.style.display = 'block'
    }
})

loginLogout.addEventListener('click', (event) => {
    if (loginLogout.textContent == 'logout') {
        // loginLogout.href == "/views/index.html"
        limparConteudo();
        clearMovies();
        return;
    }
})

function limparConteudo() {
    localStorage.clear();
    userLabel.textContent = ''
    listaLabel.textContent = ''
    loginLogout.textContent = 'login'
}

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

function clearMovies() {
    while (moviesDiv.firstChild) {
        moviesDiv.firstChild.remove()
    }
}

async function loadMovies() {
    try {
        let response = await fetch(`${API_URL}/user/${user.user_id}/filmes`)
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
              <div class="box-footer">
                <button id="like" onclick="curtir(${movie.filme_id})">Curtir</button>
              </div>
            </div>`
        moviesDiv.appendChild(box);
    })
}

function curtir(filme_id) {
    return fetch(`${API_URL}/filmes/${filme_id}/curtir`, {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    })
}

const API_URL = 'http://localhost:5000';
const form = document.querySelector('form')
const button = document.querySelector('button')

function login(email, senha) {
    return fetch(`${API_URL}/user/login`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email,
            senha
        })
    })
}

button.addEventListener('click', async (event) => {
    const email = form.email.value
    const senha = form.senha.value
    let response = await login(email, senha)
    let data = await response.json()

    if (data.autorizado !== true) {
        alert('Usuário ou senha inválidos')
        return;
    }
    
    localStorage.setItem('user', JSON.stringify(data))
    button.onclick = history.back()
})

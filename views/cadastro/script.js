const button = document.querySelector("button");
const API_URL = 'http://localhost:5000'

function cadastrar(nome, email, senha) {
    return fetch(`${API_URL}/user/cadastrar`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            nome,
            email,
            senha,
        })
    })
}

button.addEventListener("click", async (event) => {    
    event.preventDefault();
    try {
        const nome = document.getElementById("name").value;
        const email = document.getElementById("email").value;
        const senha = document.getElementById("password").value;
        
        let response = await cadastrar(nome, email, senha)
        let data = await response.json()
        console.log(data)
        
        document.getElementById("message").textContent = "Cadastro feito com Sucesso!! :)"
    } catch (error) {
        document.getElementById("message").textContent = "Não foi possível cadastrar. Tente novamente."
    }
})
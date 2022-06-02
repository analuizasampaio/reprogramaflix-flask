# reprogramaflix-flask

### Grupo: 
- Nome: Ana Luiza Sampaio RA: 2101183

- Nome: Guilherme Portes Bebiano 
RA: 2101494

- Nome: Ingrid Priscila Alves de Sousa
RA: 2101204

- Nome: Charles Eduardo Felipe de Souza
RA:  2100038

- Nome: Vitor Augusto Silva
RA:2100534 

- Nome: Kauê Ribeiro Varjão
RA: 1904284

## Rotas 

- [GET] /filmes
    - retorna todos os filmes    
- [GET] /filmes/<id>
    - retorna filmes por id
- [GET] /filmes/?q={titulo}
    - retorna filmes por titulo   
- [POST] /filmes/cadastrar
    - cdastra um filme    
- [PUT] /filmes/<id>/curtir
    - curte um filme    
- [DELETE] /filmes/<id>/curtir
    - descurte um filme
- [DELETE] /filmes/<id>
    - deleta um filme
- [GET] /users/all
    - retorna todos os usuarios    
- [GET] /user/<id>
    - retorna usuario por id
- [POST] /user/cadastrar
    - cadastra um usuario   
- [POST] /user/<id>/login
    - loga um usuario    
- [PUT] /user/<id>/logout
    - desloga um usuario   
- [GET] /user/<id>/filmes
    - retorna todos os filmes a lista de um dado usuário
- [PUT] /user/<user_id>/filmes/favorite
    - adiciona filme a lista de favoritos de um dado usuario   
- [PUT] /user/<user_id>/filmes/unfavorite
    - retira filme a lista de favoritos de um dado usuario  
- [DELETE] /filmes/<id>
    - deleta um filme
- [POST] /reset
    - deleta todos os bancos de dado

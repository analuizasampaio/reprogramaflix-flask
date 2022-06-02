from dbConfig import get_db
import sqlite3

def get_all_filmes():
    filmes = []
    conn = get_db()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM filme ")
    rows = cursor.fetchall()
    
    for i in rows:
        filme = {}
        filme['filme_id'] = i['filme_id']
        filme['titulo'] = i['titulo']
        filme['descricao'] = i['descricao']
        filme['imagem'] = i['imagem']
        filme['likes'] = i['likes']
        filmes.append(filme)
    
    return filmes

def get_filme_by_id(id):
    conn = get_db()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    statement = "SELECT * FROM filme WHERE filme_id = ?"
    cursor.execute(statement, [id])
    row = cursor.fetchone()
    
    filme = {}
    filme['filme_id'] =row['filme_id']
    filme['titulo'] =row['titulo']
    filme['descricao'] =row['descricao']
    filme['imagem'] =row['imagem']
    filme['likes'] =row['likes']
        
    return filme

def get_filme_by_titulo(titulo):
    filmes = []
    conn = get_db()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM filme WHERE titulo LIKE ?", ( '%'+titulo+'%', ))
    rows = cursor.fetchall()
    
    for i in rows:
        filme = {}
        filme['filme_id'] = i['filme_id']
        filme['titulo'] = i['titulo']
        filme['descricao'] = i['descricao']
        filme['imagem'] = i['imagem']
        filme['likes'] = i['likes']
        filmes.append(filme)
    
    return filmes

def insert_filme(filme):
    conn = get_db()
    cursor = conn.cursor()
    titulo = filme['titulo']
    descricao = filme['descricao']
    imagem = filme['imagem']
    likes = 0

    query = (f"""
                INSERT INTO filme (titulo, descricao, imagem, likes)
                VALUES(?,?,?,?)
            """)

    cursor.execute(query, (titulo, descricao, imagem, likes))
    conn.commit()
    
    # cursor.execute(f"SELECT * FROM filme WHERE titulo='{titulo}'")
    # criado = (cursor.fetchone()) 
             
    return get_filme_by_titulo(titulo)

def curtir(id):
    filme = get_filme_by_id(id)
    like = int(filme['likes']) +1
    conn = get_db()
    cursor = conn.cursor()
    query = (f"""
            UPDATE filme SET 
            likes={like}
            WHERE filme_id={id}
                            """)
    
    cursor.execute(query)
    conn.commit()
    return get_filme_by_id(id)

def descurtir(id):
    filme = get_filme_by_id(id)
    like = int(filme['likes']) -1
    conn = get_db()
    cursor = conn.cursor()
    query = (f"""
            UPDATE filme SET 
            likes={like}
            WHERE filme_id={id}
                            """)
    
    cursor.execute(query)
    conn.commit()
    return get_filme_by_id(id)

def insert_user(user):
    conn = get_db()
    cursor = conn.cursor()
    nome = user['nome']
    email = user['email']
    senha = user['senha']


    query = (f"""
                INSERT INTO user (nome, email, senha)
                VALUES(?,?,?)
            """)

    cursor.execute(query, (nome, email, senha))
    conn.commit()
    
    cursor.execute(f"SELECT * FROM user WHERE nome='{nome}'")
    criado = (cursor.fetchone()) 
             
    return criado

def get_user_by_id(id):
    conn = get_db()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    statement = "SELECT * FROM user WHERE user_id = ?"
    cursor.execute(statement, [id])
    row = cursor.fetchone()
    
    user = {}
    user['user_id'] =row['user_id']
    user['nome'] =row['nome']
    user['email'] =row['email']
    user['senha'] =row['senha']
        
    return user

def login(user):
    conn = get_db()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    email = user['email']
    senha = user['senha']
    statement = "SELECT * FROM user WHERE email = ?"
    cursor.execute(statement, [email])
    criado = cursor.fetchone()
    
    encontrado = get_user_by_id(criado[0])
    
    usuario = {}
    usuario['user_id'] = encontrado['user_id']
    usuario['nome'] = encontrado['nome']
    usuario['email'] = encontrado['email']
    
    if senha == encontrado['senha']:
        usuario['autorizado'] = True
    else:
        usuario['autorizado'] = False   
    return usuario

def logout(id):
    encontrado = get_user_by_id(id)
    
    usuario = {}
    usuario['user_id'] = encontrado['user_id']
    usuario['nome'] = encontrado['nome']
    usuario['email'] = encontrado['email']
    usuario['autorizado'] = False   
    return usuario

def favorite(filme, user_id):
    conn = get_db()
    cursor = conn.cursor()
    filme_id = filme['filme_id']



    query = (f"""
                INSERT INTO userFilmes (user_id, filme_id)
                VALUES(?,?)
            """)

    cursor.execute(query, (user_id, filme_id))
    conn.commit()
             
    return get_filmes_user(user_id)

def get_filmes_user(user_id):
    filmes = []
    conn = get_db()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    query = (f"""

            SELECT filme.filme_id AS 'filme_id', filme.titulo AS 'titulo', filme.descricao AS 'descricao', filme.imagem AS imagem, filme.likes AS likes
            FROM filme
            JOIN userFilmes
            ON filme.filme_id = userFilmes.filme_id
            WHERE userFilmes.user_id = {user_id}  
                            """)
    
    cursor.execute(query)
    conn.commit()

    rows = cursor.fetchall()
    
    for i in rows:
        filme = {}
        filme['filme_id'] = i['filme_id']
        filme['titulo'] = i['titulo']
        filme['descricao'] = i['descricao']
        filme['imagem'] = i['imagem']
        filme['likes'] = i['likes']
        filmes.append(filme)
    
    return filmes

def unfavorite(filme, user_id):
    conn = get_db()
    cursor = conn.cursor()
    filme_id = filme['filme_id']



    query = (f"""
                DELETE FROM userFilmes 
                WHERE userFilmes.filme_id = {filme_id} AND
                userFilmes.user_id = {user_id}
            """)

    cursor.execute(query)
    conn.commit()
             
    return get_filmes_user(user_id)
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
    
    cursor.execute(f"SELECT * FROM filme WHERE titulo='{titulo}'")
    criado = (cursor.fetchone()) 
             
    return get_filme_by_id(criado[0])

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
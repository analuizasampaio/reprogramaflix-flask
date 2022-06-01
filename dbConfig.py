import sqlite3

def get_db():
    conn = sqlite3.connect("database.db")
    return conn
        
def create_tables():
    tables = [

        """CREATE TABLE IF NOT EXISTS filme(
                filme_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                titulo VARCHAR(50) NOT NULL,
				descricao VARCHAR(50) NOT NULL,
                imagem VARCHAR(50) NOT NULL,
				likes INTEGER  NULL
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
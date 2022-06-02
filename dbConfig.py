import sqlite3

def get_db():
    conn = sqlite3.connect("database.db")
    return conn
        
def create_tables():
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
                """CREATE TABLE IF NOT EXISTS filme(
                filme_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                titulo VARCHAR(50) NOT NULL,
				descricao VARCHAR(50) NOT NULL,
                imagem VARCHAR(50) NOT NULL,
				likes INTEGER  NULL
            )
            """
                   )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS user(
                user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(50) NOT NULL,
				email VARCHAR(50) NOT NULL UNIQUE,
                senha VARCHAR(50) NOT NULL
            )
            """
    )
    
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS userFilmes(
                user_id INTEGER NOT NULL,
                filme_id INTEGER NOT NULL,
                
                CONSTRAINT PK_userFilmes PRIMARY KEY (user_id, filme_id),
                CONSTRAINT FK_userFilmes_user_id FOREIGN KEY (user_id) REFERENCES user (user_id),
                CONSTRAINT FK_userFilmes_filme_id FOREIGN KEY (filme_id) REFERENCES filme (filme_id)
            )
            """
                   )
    # tables = [

    #     """CREATE TABLE IF NOT EXISTS filme(
    #             filme_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    #             titulo VARCHAR(50) NOT NULL,
	# 			descricao VARCHAR(50) NOT NULL,
    #             imagem VARCHAR(50) NOT NULL,
	# 			likes INTEGER  NULL
    #         )
    #         """
            
    #     """CREATE TABLE IF NOT EXISTS user(
    #             user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    #             nome VARCHAR(50) NOT NULL,
	# 			email VARCHAR(50) NOT NULL,
    #             senha VARCHAR(50) NOT NULL
    #         )
    #         """
    #     """CREATE TABLE IF NOT EXISTS userFilmes(
    #             user_id INTEGER NOT NULL,
    #             filme_id INTEGER NOT NULL,
                
    #             CONSTRAINT PK_userFilmes PRIMARY KEY (user_id, filme_id),
    #             CONSTRAINT FK_userFilmes_user_id FOREIGN KEY (user_id) REFERENCES user (user_id),
    #             CONSTRAINT FK_userFilmes_filme_id FOREIGN KEY (filme_id) REFERENCES filme (filme_id)
    #         )
    #         """
    #  ]

    # db = get_db()
    # cursor = db.cursor()
    # for table in tables:
    #     cursor.execute(table)
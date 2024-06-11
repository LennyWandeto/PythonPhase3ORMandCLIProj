from models.__init__ import CONN, CURSOR

def create_tables():
    CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS woodwork (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        type TEXT NOT NULL,
        carpenter_id INTEGER,
        owner_id INTEGER,
        FOREIGN KEY (carpenter_id) REFERENCES carpenter (id)
        FOREIGN KEY (owner_id) REFERENCES owner (id)
    );""")

    CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS carpenters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        number INTEGER
    );""")

    CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS owners(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL
        );""")
    CONN.commit()
    # CONN.close()


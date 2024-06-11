from __init__ import CONN, CURSOR

def create_tables():
    CURSOR.execute("""
    CREATE TABLE woodwork (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        type TEXT NOT NULL,
        carpenter_id INTEGER NOT NULL,
        owner_id INTEGER NOT NULL,
        FOREIGN KEY (carpenter_id) REFERENCES carpenter (id)
        FOREIGN KEY (owner_id) REFERENCES owner (id)
    );""")

    CURSOR.execute("""
    CREATE TABLE carpenters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
    );""")

    CURSOR.execute("""
    CREATE TABLE owners(
        id INTEGER PRIMARY KEY AUTOINCREMENT
        name TEXT NOT NULL
        description TEXT NOT NULL
        );""")
    CONN.commit()
    CONN.close()


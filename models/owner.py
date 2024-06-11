from __init__ import CONN, CURSOR

class Owner:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        CURSOR.execute('INSERT INTO owners (name, description) VALUES (?, ?)', (self.name, self.description))
        CONN.commit()
    
    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM owners')
        return CURSOR.fetchall()

    @classmethod
    def get_by_id(cls, id):
        CURSOR.execute('SELECT * FROM owners WHERE id =?', (id,))
        return CURSOR.fetchone()
    
    @classmethod
    def get_all_carpenter_under_owner(cls):
        CURSOR.execute("""
            SELECT carpenter.name, woodwork.id
            FROM carpenter
            LEFT JOIN woodwork
            ON woodwork.owner_id = owner.id
        """)
        return CURSOR.fetchall()
    
    @classmethod
    def delete_owner(cls, name):
        CURSOR.execute('DELETE FROM owners WHERE name =?', (name,))
        CONN.commit()
from __init__ import CONN, CURSOR
from set import create_tables
class Woodwork:
    def __init__(self, name, type, price, carpenter_id=None):
        self.name = name
        self.type = type
        self.carpenter_id = carpenter_id
        self.price = price
        CURSOR.execute('INSERT INTO woodwork (name, type) VALUES (?, ?)', (self.name, self.type))
        CONN.commit()
    
    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM woodwork')
        return CURSOR.fetchall()

    @classmethod
    def get_by_id(cls, id):
        CURSOR.execute('SELECT * FROM woodwork WHERE id =?', (id,))
        return CURSOR.fetchone()
    
    @classmethod
    def get_by_name(cls, name):
        CURSOR.execute('SELECT * FROM woodwork WHERE name =?', (name,))
        return CURSOR.fetchone()
    
    @classmethod
    def get_by_type(cls, type):
        CURSOR.execute('SELECT * FROM woodwork WHERE type =?', (type,))
        return CURSOR.fetchall()
    
    @classmethod
    def get_by_carpenter(cls, carpenter_name):
        CURSOR.execute("""
            SELECT *
            FROM woodwork
            LEFT JOIN carpenters
            ON carpenter.name = ?
        """, (carpenter_name,))
        return CURSOR.fetchall()
    
    @classmethod
    def delete_by_id(cls, id):
        CURSOR.execute('DELETE FROM woodwork WHERE id =?', (id,))
        CONN.commit()
    
    @classmethod
    def get_by_carpenter_id(cls, carpenter_id):
        CURSOR.execute('SELECT * FROM woodwork WHERE carpenter_id =?', (carpenter_id,))
        return CURSOR.fetchall()
    
    @classmethod
    def assign_woodwork_to_carpenter(cls, woodwork_id, carpenter_id):
        CURSOR.execute('UPDATE woodwork SET carpenter_id =? WHERE id =?', (carpenter_id, woodwork_id))
        CONN.commit()
    

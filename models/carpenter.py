from __init__ import CONN, CURSOR

class Carpenter:
    def __init__(self, name, number=None):
        self.name = name
        self.number = number
    
    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM carpenter')
        return CURSOR.fetchall()
    
    @classmethod
    def get_by_id(cls, id):
        CURSOR.execute('SELECT * FROM carpenter WHERE id =?', (id,))
        return CURSOR.fetchone()
    
    @classmethod
    def get_by_name(cls, name):
        CURSOR.execute('SELECT * FROM carpenter WHERE name =?', (name,))
        return CURSOR.fetchone()
    
    @classmethod
    def delete_carpenter(cls, name):
        CURSOR.execute('DELETE FROM carpenter WHERE name =?', (name,))
        CONN.commit()
    
        
        
from models.__init__ import CONN, CURSOR

class Carpenter:
    def __init__(self, name, number=None):
        self.name = name
        self.number = number
        CURSOR.execute('INSERT INTO carpenters (name, number) VALUES (?, ?)', [self.name, self.number])
        CONN.commit()
    
    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM carpenters')
        return CURSOR.fetchall()
    
    @classmethod
    def get_by_id(cls, id):
        CURSOR.execute('SELECT * FROM carpenters WHERE id =?', (id,))
        return CURSOR.fetchone()
    
    @classmethod
    def get_by_name(cls, name):
        CURSOR.execute('SELECT * FROM carpenters WHERE name =?', (name,))
        return CURSOR.fetchone()
    
    @classmethod
    def delete_carpenter(cls, name):
        CURSOR.execute('DELETE FROM carpenters WHERE name =?', (name,))
        CONN.commit()
    
        
        
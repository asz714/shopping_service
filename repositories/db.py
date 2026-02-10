import sqlite3

class DB:
    def __init__(self) -> None:
        self.conn_str = sqlite3.connect('shopping-system.db')
        self.cursor = self.conn_str.cursor()
        
    def add(self, query: str)->bool:
        self.cursor.execute(query)
        self.conn_str.commit()
    
        return True
    
    def fetch(self, query: str)->list:
        return self.cursor.execute(query).fetchall()
    
    
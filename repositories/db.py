import sqlite3
from domains import product
class DB:
    def __init__(self,dbname:str) -> None:
        self.conn_str = sqlite3.connect(dbname)
        self.cursor = self.conn_str.cursor()
        
    def add(self, query: str)->bool:
        self.cursor.execute(query)
        self.conn_str.commit()
        return True
    
    def fetch(self, query: str)->list:
        return self.cursor.execute(query).fetchone()
    
    def fetchall_(self, query: str)->list:
        return self.cursor.execute(query).fetchall()
    
    def clear(self,table_name:str)->bool:
        self.cursor.execute(f"DELETE FROM '{table_name}' ")
        self.conn_str.commit()
        
    # f'DELETE FROM fk_users_products WHERE name = {product.name}'
    
    def update(self,query:str)->bool:
        self.cursor.execute(query)
        self.conn_str.commit()
    
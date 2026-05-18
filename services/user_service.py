from domains import User
from repositories import DB

class UserService:
    @staticmethod
    def add_user(user: User,dbname):
        db = DB(dbname)        
        db.add(f"INSERT INTO users (uname) VALUES ('{user.uname}')")
        user.user_id = db.cursor.lastrowid
        return True
    
    @staticmethod
    def fetch_users(dbname):
        db = DB(dbname)
        return db.fetchall_(f'SELECT * FROM users')
        
        
    @staticmethod
    def fetchall_users(dbname):
        db = DB(dbname)
        return db.fetch(f'SELECT * FROM users')
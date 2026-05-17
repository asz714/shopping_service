from domains import User
from repositories import DB

class UserService:
    @staticmethod
    def add_user(user: User):
        db = DB()        
        db.add(f"INSERT INTO users (uname) VALUES ('{user.uname}')")
        user.user_id = db.cursor.lastrowid
        return True
    
    @staticmethod
    def fetch_users():
        db = DB()
        return db.fetchall_(f'SELECT * FROM users')
        
        
    @staticmethod
    def fetchall_users():
        db = DB()
        return db.fetch(f'SELECT * FROM users')
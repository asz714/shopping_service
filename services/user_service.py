from domains import User
from repositories import DB

class UserService:
    @staticmethod
    def add_user(user: User):
        db = DB()
        db.add(f"INSERT INTO users (uname) VALUES ('{user.uname}')")
        
        return True
    
    @staticmethod
    def fetch_users():
        db = DB()
        return db.fetch(f'SELECT * FROM users')
        
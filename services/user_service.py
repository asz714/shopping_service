from domains import User
from repositories import DB

class UserService:
    @staticmethod
    def add_user(user: User):
        db = DB()
        db.add(f"INSERT INTO users (uname) VALUES ('{user.uname}')")
        
        return True
    
    def show_user():...
        # conn_str = sqlite3.connect()
        # cursor = conn_str.cursor()
        # cursor.execute(select * from users).fetchall()
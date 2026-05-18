from domains import User
from services import UserService
from random import randint
from repositories import DB

def test_add_user():
    former_users_len = len(UserService.fetch_users(dbname="shopping-system.db")) 
    
    user= User(uname="customer03")
    UserService.add_user(user,dbname="shopping-system.db")
    
    current_users_len = len(UserService.fetch_users(dbname="shopping-system.db")) 
    
    assert current_users_len == former_users_len + 1

def test_user_service():

    db=DB(dbname= "testdb.db")
    db.add("""
        CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uname VARCHAR(25)
        )""")

    db.clear('users')

    user= User(uname="customer03")

    UserService.add_user(user,dbname="testdb.db")

    users=UserService.fetch_users(dbname="testdb.db")

    assert len(users) == 1
    assert users[0][1] == "customer03"
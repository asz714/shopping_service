from domains import User
from services import UserService
from random import randint

def test_add_user():
    former_users_len = len(UserService.fetch_users()) 
    
    user = User(f'test_user{randint(0,1000)}')
    UserService.add_user(user)
    
    current_users_len = len(UserService.fetch_users()) 
    
    assert current_users_len == former_users_len + 1
    
from domains import User
from utilities.logger import logger
from services import UserService
from random import randint

user = User(f'customer {randint(0,100)}')

UserService.add_user(user)

print(UserService.fetch_users())


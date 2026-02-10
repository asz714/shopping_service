from domains import User
from utilities.logger import logger
from services import UserService

user = User('customer03')

UserService.add_user(user)

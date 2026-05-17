from domains import User, Product
from utilities.logger import logger
from services import ProductService,UserService,ShoppingService 
from random import randint

user = User(uname=f'customer {randint(0,100)}')
product=Product( name='mobile', price=2.5, quantity_in_stock = 5)
UserService.add_user(user)
ProductService.add_product(product)

shopping_service = ShoppingService(user=user)
shopping_service.add_items(product=product)
shopping_service.remove_item(product=product)
shopping_service.add_items(product=product)
shopping_service.add_items(product=product)
shopping_service.add_items(product=product)

print(ShoppingService.fetch_items())




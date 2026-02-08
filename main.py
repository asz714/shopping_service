from domains import User, Product
from services import ShoppingService

user = User(120, 'customer01')

product = Product(product_id=101,name='Mobile', price=2.50, quantity_in_stock=2)

shopping_service = ShoppingService(user)

shopping_service.add_items(product=product)
shopping_service.add_items(product=product)
shopping_service.add_items(product=product)



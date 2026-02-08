from domains import User, Product, Shopping_Card

user = User(120, 'customer01')

mobile = Product(101,'Mobile', 2.50)
tv = Product(102,'TV', 20.50)

shopping_card = Shopping_Card(100, user)

shopping_card.add_items(mobile, 2)
shopping_card.add_items(tv, 1)

print(shopping_card.total)


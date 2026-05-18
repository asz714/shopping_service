from services import ShoppingService,UserService,ProductService
from domains import User, Product
from repositories import DB
import pytest


def test_quantity_in_stock():
    user = User('test_user')
    product = Product(product_id=12, name='test_item', 
                      price=25.5, quantity_in_stock=1)
    
    shopping_service = ShoppingService(user)
    
    shopping_service.add_items(product=product,dbname= "shopping-system.db")
    
    assert product.quantity_in_stock == 0
    
def test_out_of_stack():

    user = User('test_user')
    product = Product(product_id=12, name='test_item', 
                      price=25.5, quantity_in_stock=1)
    
    shopping_service = ShoppingService(user)
    
    ShoppingService.add_items(shopping_service,product=product,dbname= "shopping-system.db")
     
    with pytest.raises(ValueError):
        shopping_service.add_items(product=product,dbname= "shopping-system.db")


def test_shopping_service():
    db=DB(dbname="testdb.db")
    db.add("""
        CREATE TABLE IF NOT EXISTS fk_users_products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id int,
            product_id int,
            quantity integer,

            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (product_id) REFERENCES product(id)
        )
        """)
    
    db.clear(table_name="fk_users_products")
    db.clear(table_name="users")
    db.clear(table_name="product")
    
    user = User('test_user')
    product = Product(name='test_item', 
                      price=25.5, quantity_in_stock=1)


    UserService.add_user(user,dbname="testdb.db")
    ProductService.add_product(product,dbname="testdb.db")
    shopping__service= ShoppingService(user)
    ShoppingService.add_items(shopping__service,product,dbname="testdb.db")
    
    products=ProductService.fetchall_product(dbname="testdb.db")
    users=UserService.fetch_users(dbname='testdb.db')
    items=ShoppingService.fetch_items(dbname='testdb.db')
    
    
   
    assert items[-1]== 1
    assert items[0] == 'test_user'
    assert items[1] == 'test_item'
    assert items[2] == 25.5
   
    
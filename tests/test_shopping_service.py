from services import ShoppingService
from domains import User, Product
import pytest


def test_quantity_in_stock():
    user = User('test_user')
    product = Product(product_id=12, name='test_item', 
                      price=25.5, quantity_in_stock=1)
    
    shopping_service = ShoppingService(user)
    
    shopping_service.add_items(product=product)
    
    assert product.quantity_in_stock == 0
    
def test_out_of_stack():

    user = User('test_user')
    product = Product(product_id=12, name='test_item', 
                      price=25.5, quantity_in_stock=1)
    
    shopping_service = ShoppingService(user)
    
    shopping_service.add_items(product=product)
     
    with pytest.raises(ValueError):
        shopping_service.add_items(product=product)
    
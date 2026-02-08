from domains.user import User
from domains.product import Product
from typing import Dict, List

class ShoppingService:
    def __init__(self, user: User) -> None:
        self.user = user
        self.items = {}
        
    def add_items(self, product: Product):
        if product.quantity_in_stock <= 0:
            raise ValueError('out of stock')
        else:            
            product.quantity_in_stock -= 1
        # self.items[product.name] = [product.price]
    
    def get_items(self)->dict:
        return self.items
    
    @property
    def total(self)->float:
        total = 0
        for _, sub_total in self.items.items():
            total += sub_total[0] * sub_total[1]
            
        return total
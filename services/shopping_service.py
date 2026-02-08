from domains.user import User
from domains.product import Product
from typing import Dict, List

class ShoppingService:
    def __init__(self, user: User) -> None:
        self.user = user
        self.items = {}
        self.quantity: int = 0
        
    def add_items(self, product: Product):
        if product.quantity_in_stock <= 0:
            raise ValueError('out of stock')
        
        product.quantity_in_stock -= 1
        self.quantity += 1
        
        self.items[product.name] = product.price
    
    def get_items(self)->dict:
        return self.items
    
    @property
    def total(self)->float:
        total = 0
        for _, sub_total in self.items.items():
            total += sub_total[0] * sub_total[1]
            
        return total
    
    def __str__(self) -> str:
        return f'item: {self.items}, # of items: {self.quantity}'
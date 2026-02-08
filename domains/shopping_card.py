from .user import User
from .product import Product
from typing import Dict, List

class Shopping_Card:
    def __init__(self, card_id: int, user: User) -> None:
        self.card_id = card_id
        self.user = user
        self.items = {}
        
    def add_items(self, product: Product, quantity: int)->Dict[List[str, float]]:
        self.items[product.name] = [quantity, product.price]
    
    def get_items(self)->dict:
        return self.items
    
    @property
    def total(self)->float:
        total = 0
        for _, sub_total in self.items.items():
            total += sub_total[0] * sub_total[1]
            
        return total
from dataclasses import dataclass
from repositories import DB
from typing import Optional

@dataclass
class Product:
    name: str
    price: float
    quantity_in_stock: int
    product_id: Optional[int]  =None
    
    def __str__(self):
        return f'quantity in stock: {self.quantity_in_stock}\n'
   
   
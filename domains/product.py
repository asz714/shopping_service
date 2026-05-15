from dataclasses import dataclass
from repositories import DB

@dataclass
class Product:
    product_id: int
    name: str
    price: float
    quantity_in_stock: int
    
    def __str__(self):
        return f'quantity in stock: {self.quantity_in_stock}\n'
   

db=DB()
product=Product()
db.add(f"INSERT PINTO product (name , price , quantity_in_stock) VALUES ('{product.name},{Product.price},{Product.quantity_in_stock}') ") 
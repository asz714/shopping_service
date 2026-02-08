from dataclasses import dataclass

@dataclass
class Product:
    product_id: int
    name: str
    price: float
    quantity_in_stock: int
    
    def __str__(self):
        return f'quantity in stock: {self.quantity_in_stock}\n'
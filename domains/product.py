from dataclasses import dataclass

@dataclass
class Product:
    product_id: int
    name: str
    price: float
    quantity_in_stock: int
    
    def __str__(self):
        return str(self.quantity_in_stock)
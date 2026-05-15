from domains import User
from domains import Product
from typing import Dict, List
from repositories import DB

class ShoppingService:
    def __init__(self, user: User) -> None:
        self.user = user
        self.items = {}
        self.quantity: int = 0
        
    def add_items(self, product: Product,user:User)->bool:
        db=DB()
        if db.fetch("SELECT quantity_in_stock FROM product") <=0:
            raise ValueError('out of stock')
        db.update(f"UPDATE product SET quantity_in_stock -=1 WHERE id = product_id")
        db.update(f"UPDATE fk_users_product SET quantity +=1 WHERE product_id ='{product.id}'")        
        db.add(f"INSERT INTO fk_users_product (user_id,product_id,quantity) VALUES ('{user.id},{product.id},{self.quantity} ')")        

        return True
            
    
    def remove_item(self, product: Product)->bool:
        if self.quantity > 0:
            self.quantity -= 1
        else:
            db=DB()
            db.delete(product.name)
            if self.quantity == 0:
           
                self.items.clear()
            product.quantity_in_stock += 1
    
        return True
    
    @property
    def total(self)->float:
        total = 0
        for _, price in self.items.items():
            total += price * self.quantity
            
        return total
    
    def __str__(self) -> str:
        return f'item: {self.items}, # of items: {self.quantity}'
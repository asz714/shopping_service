from domains import User
from domains import Product
from typing import Dict, List
from repositories import DB

class ShoppingService:
    def __init__(self, user: User) -> None:
        self.user = user
        self.quantity: int = 0
        
    def add_items(self, product: Product,dbname:str)->bool:
        self.quantity += 1
        db=DB(dbname)
        if self.quantity ==1:
            db.add(f"INSERT INTO fk_users_products (user_id,product_id,quantity) VALUES ('{self.user.user_id}','{product.product_id}','{self.quantity} ')")        
        
        db.fetch("SELECT quantity_in_stock FROM product")
        if product.quantity_in_stock <=0:
            raise ValueError('out of stock')
        else:
            product.quantity_in_stock-=1
            db.update(f"UPDATE product SET quantity_in_stock ='{ product.quantity_in_stock}' WHERE name ='{product.name}'")
            db.update(f"UPDATE fk_users_products SET quantity ='{self.quantity}'")        

        return True
    
   
    def fetch_items(dbname:str):
        db=DB(dbname)
        return db.fetch(f"""
        SELECT                  
        users.uname,
        product.name,
        product.price,
        fk_users_products.quantity
        FROM fk_users_products

        JOIN users
        ON users.id = fk_users_products.user_id

        JOIN product
        ON product.id = fk_users_products.product_id """)
    
    def remove_item(self, product: Product,dbname:str)->bool:
        db=DB(dbname)
        if self.quantity > 0:
            self.quantity -= 1
            db.update(f"UPDATE fk_users_products SET quantity ='{self.quantity}' WHERE product_id ='{product.product_id}'")
            
        else:
            db.delete("f'DELETE FROM fk_users_products WHERE product_id ='{product.product_id}")
            if self.quantity == 0:
                db.delete("DELETE FROM fk_users_products ")
                product.quantity_in_stock += 1
                db.update(f"UPDATE product SET quantity_in_stock ='{ product.quantity_in_stock}' WHERE name ='{product.name}'")
                
    
        return True
    
    @property
    def total(self)->float:
        total = 0
        for _, price in self.items.items():
            total += price * self.quantity
            
        return total
    
    def __str__(self) -> str:
        return f'item: {self.items}, # of items: {self.quantity}'
from domains import Product
from repositories import DB

class ProductService:
    @staticmethod
    def add_product(product:Product,dbname):
        db = DB(dbname)
        db.add(f"INSERT INTO product (name,price,quantity_in_stock) VALUES ('{product.name}','{product.price}','{product.quantity_in_stock}')")
        product.product_id = db.cursor.lastrowid
        return True
    
    @staticmethod
    def fetch_product(adname):
        db = DB(adname)
        return db.fetchone_(f'SELECT * FROM product')
    
    @staticmethod
    def fetchall_product(dbname):
        db = DB(dbname)
        return db.fetchall_(f'SELECT * FROM product')
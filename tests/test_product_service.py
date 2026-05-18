import sqlite3

from domains import Product
from services import ProductService
from random import randint
from repositories import DB

db=DB(dbname= "testdb.db")
db.add("""
    CREATE TABLE IF NOT EXISTS product(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(25),
        price float,
        quantity_in_stock INTEGER
    )
    """)

db.clear('product')

product= Product(name=" TV 43 intch LG ",price=500 , quantity_in_stock= 6  )

ProductService.add_product(product,dbname="testdb.db")

products=ProductService.fetchall_product(dbname="testdb.db")

def test_product_service():
    assert len(products) == 1
    assert products[0][1] == " TV 43 intch LG "
    assert products[0][2] == 500
    assert products[0][3] == 6
 
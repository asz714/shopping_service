CREATE TABLE if NOT EXISTS users (
    id PRIMARY KEY AUTOINCREMENT,
    uname VARCHAR(25)
);

CREATE TABLE if NOT EXISTS product (
    id PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(25),
    price FLOAT
    quantity_in_stock INT 
);

CREATE TABLE if NOT EXISTS fk_users_products(
    id PRIMARY KEY AUTOINCREMENT,
    user_id INT,
    product_id INT,
    quantity INTEGER,
    Foreign Key (user_id) REFERENCES users(id)
    Foreign Key (product_id) REFERENCES product(id)
);

CREATE TABLE users (
    id PRIMARY KEY AUTOINCREMENT,
    uname VARCHAR(25)
);

CREATE TABLE product (
    id PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(25),
    price FLOAT
    quantity_in_stock INT 
);

CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    store_id INT,
    timestamp TIMESTAMP,
    item TEXT,
    category TEXT,
    quantity INT,
    price FLOAT
);  
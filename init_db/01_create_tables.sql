CREATE TABLE users (
    user_id TEXT PRIMARY KEY,
    signup_date DATE,
    country TEXT
);

CREATE TABLE products (
    product_id TEXT PRIMARY KEY,
    category TEXT,
    price NUMERIC
);

CREATE TABLE events (
    user_id TEXT,
    event_type TEXT,
    product_id TEXT,
    timestamp TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);


COPY users(user_id, signup_date, country)
FROM '/data/users.csv'
DELIMITER ','
CSV HEADER;

COPY products(product_id, category, price)
FROM '/data/products.csv'
DELIMITER ','
CSV HEADER;

COPY events(user_id, event_type, product_id, timestamp)
FROM '/data/events.csv'
DELIMITER ','
CSV HEADER;

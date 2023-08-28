DROP TABLE IF EXISTS cars;
DROP TABLE IF EXISTS brands;

CREATE TABLE brands (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE cars(
    id SERIAL PRIMARY KEY,
    make VARCHAR(255),
    model VARCHAR(255),
    buying_cost FLOAT,
    selling_cost FLOAT,
    quantity INT,
    sold BOOLEAN DEFAULT FALSE,
    brand_id INT REFERENCES brands(id) ON DELETE CASCADE

);


-- INSERT INTO brands (name) VALUES ('Mercedes Benz');
-- INSERT INTO brands (name) VALUES ('BMW');

-- INSERT INTO cars(name, model, buying_cost, selling_cost,  quantity) VALUES ('Mercedes', 'C300', 25000.00, 27500.00, 4 );
-- INSERT INTO cars(name, model, buying_cost, selling_cost,  quantity) VALUES ('BMW', 'A1', 20000.00, 22500.00, 5 );
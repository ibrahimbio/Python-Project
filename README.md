# Python-Project

# Brief

My client asked me to build a full stack application that would be used by the staff to check inventory of vehicle they have in stock using Python, Flask, HTML, CSS and PostgreSQL.

# MVP

- A staff should be able to view a list of vehicles in the investory
- A staff should be a able to see the vehicle make, model, buying cost, selling cost, quantity available in store.
- A staff should be able to know if a brand/make of vehicle is high, low or out of stock.
- A staff should be about to add new vehicle into the database
- A staff should be able to edit the details of a vehicle in the list.  


# Learnings

## PostgreSQL 

- Practically learnt how to add create     tables with a one to many relationship and have it to communicate with my app to new information added by a user.

## Python 

- Learnt how to build a repository and a controller from scratch and also debug any issue encounter while running my program. 

## Flask

- I now have a better understanding of how flask works. 
 

## CSS

- I research a few ways on how to implement styling of forms and background image on my app. Also discovered color palette that relief of the stress using primary colors to style the app.


# SET UP 

1 - Git clone my repo locally

- In terminal
```
git clone git@github.com:ibrahimbio/Python-Project.git
````

2 - Setup Database


```                                                                                                                              DROP TABLE IF EXISTS cars;
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

```
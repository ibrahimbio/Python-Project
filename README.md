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
    #terminal 
git clone git@github.com:ibrahimbio/Python-Project.git
````
2 - Setup Database

 - In terminal 
    ```
    #terminal 
    createdb car_inventory

    ```

3 -  Create Tables


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

4 - Created a run_sql file that connects my database to my app. Kept in the same folder with the databse file. 
  
```
import psycopg2  #imported psycopg2, allows python to access databse
import psycopg2.extras as ext

def run_sql(sql, values = None):
    conn = None
    results = []

    try:
        conn=psycopg2.connect("dbname='car_inventory'")
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return results

```


5 - Checked if the table was created successfully.
- In terminal
```
 #terminal 

psql -d car_inventory -f db/car_inventory.sql
```

6 - Created a '.flaskenv' file to run the flask app, debug and port. 

```
FLASK_APP =app.py
FLASK_DEBUG =true
FLASK_RUN_HOST=127.0.0.1
FLASK_RUN_PORT =4999

```

7 - Created Class models for the app in two different files but in the same "models" folder

```
 class Brand:
    def __init__(self, name, id=None):
        self.name = name
        self.id = id
        
class Car:
    def __init__(self, brand,  make, model, buying_cost, selling_cost, quantity,  sold = False, id = None):
        self.brand = brand
        self.make = make
        self.model = model
        self.buying_cost = buying_cost
        self.selling_cost = selling_cost
        self.quantity = quantity
        self.sold = sold
        self.id = id


    def mark_sold(self):
        self.sold = True

```

8 - Created a Repository file for each class and imported the run_sql function, and required classes

```
#for brand_reposiitory folder:

from db.run_sql import run_sql
from models.brand import Brand
from models.car import Car

#for car_reposiitory folder:

from db.run_sql import run_sql
from models.car import Car
from models.brand import Brand
import repositories.brand_repository as brand_repository


``` 

9 - Created a controller file to create instances of brand and cars.
    - Here all class and repos were imported
    
```
    import pdb # a trace, this indicates where our program stops after running it
    import repositories.brand_repository as brand_repository
    import repositories.car_repository as car_repository
    from models.brand import Brand
    from models.car import Car
    ```

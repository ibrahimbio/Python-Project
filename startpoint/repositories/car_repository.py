# import pdb
from db.run_sql import run_sql
from models.car import Car
from models.brand import Brand
import repositories.brand_repository as brand_repository


##CRUD functions

#Save() function; this saves an input into the table.
def save(car):
    sql = "INSERT INTO cars ( brand_id, make, model, buying_cost, selling_cost, quantity) VALUES (%s, %s, %s, %s, %s, %s) RETURNING*"
    values = [car.brand.id, car.make, car.model, car.buying_cost, car.selling_cost, car.quantity]
    results = run_sql(sql, values)
    car.id = results[0]['id']
    return car

#Select_all() function: This returns all the items in a given table.
def select_all():
    cars = []

    sql = "SELECT * FROM cars"
    results = run_sql(sql)

    for row in results:
        brand =  brand_repository.select(row['brand_id'])
        car = Car( brand, row['make'], row['model'], row['buying_cost'], row['selling_cost'], row['quantity'], row['sold'], row['id'])
        cars.append(car)
    return cars


#Select(id) function: This return a specific(single) item in a table using the id.
def select(id):
    car = None
    sql = "SELECT * FROM cars WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        brand = brand_repository.select(result['brand_id'])
        car = Car( brand, result['make'], result['model'], result['buying_cost'], result['selling_cost'], result['quantity'], result['id'])
    return car


#delete_all() function: This returns an empty table.
def delete_all():
    sql = "DELETE FROM cars"
    run_sql(sql)

#delete one function: this targets a specific item us the id and removes it from the table.
def delete(id):
    sql = "DELETE FROM cars WHERE id= %s"
    values = [id]
    run_sql(sql, values)


#Update function:
def update(car):
    sql = "UPDATE cars SET (brand, make, model, buying_cost, selling_cost, quantity) = (%s, %s, %s, %s, %s, %s) WHERE id =%s"
    values = [car.brand.id, car.make, car.model, car.buying_cost, car.selling_cost, car.quantity]
    run_sql(sql,values)


#Return a list of car brand and their specifications
def cars_in_inventory(brand):
    # pdb.set_trace()
    cars = []

    sql = "SELECT * FROM cars WHERE brand_id = %s"
    values = [brand.id]
    results = run_sql(sql, values)

    for row in results:
    
        car = Car(row['make'], row['model'], row['buying_cost'], row['selling_cost'], row['quantity'], row['id'])
        cars.append(car)
    return cars

    

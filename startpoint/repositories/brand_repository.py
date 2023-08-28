from db.run_sql import run_sql
from models.brand import Brand
from models.car import Car

##CRUD functions

#Save() function; this saves an input into the table.
def save(brand):
    sql = "INSERT INTO brands (name) VALUES (%s) RETURNING*"
    values = [brand.name]
    results = run_sql(sql, values)
    brand.id = results[0]['id']
    return brand

#Select_all() function: This returns all the items in a given table.
def select_all():
    brands = []

    sql = "SELECT * FROM brands"
    results = run_sql(sql)

    for row in results:
        brand = (row['name'], row['id'])
        brands.append(brand)
    return brands


#Select(id) function: This return a specific(single) item in a table using the id.
def select(id):
    brand = None
    sql = "SELECT * FROM brands WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        brand = Brand(result['name'], result['id'])
    return brand


#delete_all() function: This returns an empty table.
def delete_all():
    sql = "DELETE FROM brands"
    run_sql(sql)


#Update function:
def update(brand):
    sql = "UPDATE brands SET (name) = (%s) WHERE id =%s"
    values  = [brand.name, brand.id]
    run_sql(sql,values)

    



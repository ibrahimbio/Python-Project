import pdb
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.car import Car
import repositories.brand_repository as brand_repository
import repositories.car_repository as car_repository


cars_blueprint = Blueprint("car", __name__)

##CRUD Routes

#INDEX 
#GET '/cars'

@cars_blueprint.route('/cars')
def cars():
    cars = car_repository.select_all()
    sorted_cars = sorted(cars, key=lambda car:car.brand.name)
    return render_template('cars/index.html', all_cars = sorted_cars)


# SHOW
# GET '/cars/<id>'

@cars_blueprint.route('/cars/<id>', methods =['GET'])
def show_car(id):
    # brand = brand_repository.select(id)
    # car = car_repository.cars_in_inventory(brand)
    car = car_repository.select(id)
    return render_template('cars/show.html', car=car)

#NEW
#GET 'cars/new'

@cars_blueprint.route('/cars/new')
def new_cars():
    brands = brand_repository.select_all()
    # pdb.set_trace()
    return render_template('cars/new.html', all_brands = brands)


#CREATE
#POST '/cars'

@cars_blueprint.route('/cars/', methods =['POST'])
def add_car():
    brand_id= request.form['brand_id']
    make = request.form['make']
    model = request.form['model']
    buying_cost = request.form['buying_cost']
    selling_cost = request.form['selling_cost']
    quantity = request.form['quantity']
    sold = request.form['sold']
    brand = brand_repository.select(brand_id)
    car = Car(brand, make, model,buying_cost, selling_cost, quantity,sold)
    car_repository.save(car)
    return redirect('/cars')


#EDIT
#GET '/cars/<id>/edit'

@cars_blueprint.route('/cars/<id>/edit')
def edit_car(id):
    car = car_repository.select(id)
    brands = brand_repository.select_all()
    return render_template('cars/edit.html', car =car, all_brands = brands) 

@cars_blueprint.route('/cars/<id>', methods =['POST'])
def update_car(id):
    # pdb.set_trace()
    brand_id= request.form['brand']
    make = request.form['make']
    model = request.form['model']
    buying_cost = request.form['buying_cost']
    selling_cost = request.form['selling_cost']
    quantity = int(request.form['quantity'])
    sold = request.form['sold']
    brand = brand_repository.select(brand_id)
    car = Car(brand, make, model,buying_cost, selling_cost, quantity,sold, id)
    car_repository.update(car)
    return redirect('/cars')






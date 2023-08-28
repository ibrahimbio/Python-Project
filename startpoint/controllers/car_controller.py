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
    # pdb.set_trace()
    return render_template('cars/index.html', all_cars = cars)

# SHOW
# GET '/cars/<id>'

@cars_blueprint.route('/cars/<id>', methods =['GET'])
def show_car(id):
    # brand = brand_repository.select(id)
    # car = car_repository.cars_in_inventory(brand)
    car = car_repository.select(id)
    return render_template('cars/show.html', car=car)

#CREATE
#GET 'cars/new'

@cars_blueprint.route('/cars/new')
def new_cars():
    brands = brand_repository.select_all()
    return render_template('cars/new.html', all_brands = brands)





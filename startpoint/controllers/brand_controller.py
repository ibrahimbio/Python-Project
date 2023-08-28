from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.brand import Brand
import repositories.brand_repository as brand_repository
import repositories.car_repository as car_repository

brands_blueprint = Blueprint("brand", __name__)


@brands_blueprint.route('/brands')
def brands():
    brands = brand_repository.select_all()
    return render_template('/brands/index.html', title='Car Bands in Stock', all_brands =brands)

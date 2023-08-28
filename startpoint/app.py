from flask import Flask, render_template
from controllers.brand_controller import brands_blueprint
from controllers.car_controller import cars_blueprint


app = Flask(__name__)

app.register_blueprint(brands_blueprint)
app.register_blueprint(cars_blueprint)


@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/viz')
# def viz():
#     img_url = url_for('static', filename='logo.png')
#     return render_template('index.html', image_url =img_url)

if __name__ == '__main__':
    app.run(debug=True)
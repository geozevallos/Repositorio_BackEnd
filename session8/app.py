from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
import json

from flask import jsonify

from flask import request

from utils import collections

app = Flask(__name__)
Bootstrap(app)


raw = open("data/products.json", "r")
products = json.load(raw)



@app.route('/api/add_products', methods = ['POST'])
def create_product():
    product = request.json
    products.append(product)
    return jsonify(product)


@app.route('/api/products')
def get_products():
    return jsonify(products)

@app.route('/api/types')
def get_types():
    products_types = collections.unique_by_key(products, "type")
    return jsonify(products_types)


@app.route('/api/types/<type>/products')
def get_products_by_type(type):
    filtered_products = collections.filter_by(products, "type", type)
    return jsonify(filtered_products)


@app.route('/<type>/products')
def search_by_product(type):
    filtered_products = collections.filter_by(products, "type", type)
    products_types = collections.unique_by_key(products, "type")
    return render_template("index.html", products = filtered_products,
    types = products_types)

@app.route("/")
def index():


    products_types = collections.unique_by_key(products, "type")

    return render_template("index.html", 
    products = products, types = products_types)
#Source: https://stackoverflow.com/questions/49222033/raise-typeerrorrepro-is-not-json-serializable
from flask import Flask, jsonify, request
from server.model.product import Product, ProductSchema

app = Flask(__name__)

products=[Product('a','b','c','d')]


@app.route("/")
def hello_world():
      return "Hello, World!"

@app.route("/products", methods=['POST'])
def add_product():
    product = ProductSchema().load(request.get_json())
    products.append(product.data)
    return "", 204

@app.route("/products")
def get_products():
    schema = ProductSchema(many=True)
    return jsonify(products)

if __name__ == "__main__":
    app.run()
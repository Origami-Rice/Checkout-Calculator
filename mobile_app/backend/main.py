from flask import Flask, jsonify, request
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)


@app.route('/getCatalogue', methods=['GET'])
def get_catalogue():
    with open('mobile_app/backend/catalogue.json') as f:
        catalogue = json.load(f)
    f.close
    return jsonify(catalogue)


@app.route('/', methods=['GET'])
def get_hello():
    return 'Hello World!'


@app.route('/getTotal/<int:price>/<int:quantities>', methods=['GET'])
def get_total(price, quantities):
    return str(price * quantities)


@app.route('/submit', methods=['POST', 'GET'])
def post_order():
    print('it is called!')
    jsonData = request.get_json()
    with open('order.json', 'w') as outfile:
        json.dump(jsonData, outfile)
    return jsonify(jsonData)


@app.route('/getOrder', methods=['GET'])
def get_order():
    with open('order.json') as f:
        order = json.load(f)
    f.close
    return jsonify(order)


if __name__ == "__main__":
    app.run(debug=True)

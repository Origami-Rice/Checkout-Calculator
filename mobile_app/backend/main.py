from flask import Flask, jsonify
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)

@app.route('/getCatalogue', methods=['GET'])
def get_catalogue():
    with open('catalogue.json') as f:
        catalogue=json.load(f)
    f.close
    return jsonify(catalogue)

@app.route('/', methods=['GET'])
def get_hello():
    return 'Hello World!'

@app.route('/getTotal/<int:price>/<int:quantities>', methods=['GET'])
def get_total(price, quantities):
    print('it is called!')
    return str(price * quantities)

if __name__=="__main__":
    app.run(debug=True)

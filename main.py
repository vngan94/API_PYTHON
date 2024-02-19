# main.py
from flask import Flask, request
from services.CustomerService import (
    get_customers_route, create_customer_route,
    update_customer_route, delete_customer_route,
    get_customer_route
)
from db_connector import get_db_connection

app = Flask(__name__)

# ... (previous code remains the same)

# Customer routes

@app.route('/customers', methods=['GET'])
def get_customers():
    return get_customers_route()

@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    return get_customer_route(customer_id)

@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    return create_customer_route(data)

@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    data = request.get_json()
    return update_customer_route(customer_id, data)

@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    return delete_customer_route(customer_id)

if __name__ == '__main__':
    app.run(debug=True)

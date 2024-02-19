# service.py
from flask import jsonify
from db_connector import execute_query, commit_query

def get_customers_route():
    query = "SELECT * FROM customer"
    result = execute_query(query, fetchall=True)

    customers = [
        {
            "id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "email": row[3],
            "phone_number": row[4],
            "company_name": row[5],
            "created_at": row[6].strftime("%a, %d %b %Y %H:%M:%S GMT") if row[6] else None
        }
        for row in result
    ]

    return jsonify(customers), 200

def get_customer_route(customer_id):
    query = "SELECT * FROM customer WHERE customer_id=%s"
    result = execute_query(query, (customer_id,))

    if result:
        customer = {
            "id": result[0],
            "first_name": result[1],
            "last_name": result[2],
            "email": result[3],
            "phone_number": result[4],
            "company_name": result[5],
            "created_at": result[6].strftime("%a, %d %b %Y %H:%M:%S GMT") if result[6] else None
        }
        return jsonify(customer), 200
    else:
        return jsonify({"message": "Customer not found"}), 404

def create_customer_route(data):
    query = "INSERT INTO customer (first_name, last_name, email, phone_number, company_name) VALUES (%s, %s, %s, %s, %s)"
    params = (data['first_name'], data['last_name'], data['email'], data['phone_number'], data['company_name'])

    try:
        commit_query(query, params)
        return jsonify({"message": "Customer created successfully", "data": ""}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_customer_route(customer_id, data):
    query = "UPDATE customer SET first_name=%s, last_name=%s, email=%s, phone_number=%s, company_name=%s WHERE customer_id=%s"
    params = (data['first_name'], data['last_name'], data['email'], data['phone_number'], data['company_name'], customer_id)

    try:
        commit_query(query, params)
        return jsonify({"message": "Customer updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def delete_customer_route(customer_id):
    query = "DELETE FROM customer WHERE customer_id=%s"
    params = (customer_id,)

    try:
        commit_query(query, params)
        return jsonify({"message": "Customer deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

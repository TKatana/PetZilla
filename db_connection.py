from flask import Flask, render_template, jsonify
import pymysql

app = Flask(__name__)

# Database connection parameters (update with your actual details)
db_config = {
    'host': 'localhost',     # XAMPP MySQL runs on localhost
    'user': 'root',          # Default MySQL user in XAMPP
    'password': '',          # Default MySQL password is empty in XAMPP
    'database': 'pet_zilla'    # The name of the database you created in phpMyAdmin
}

# Create a function to connect to the database
def get_db_connection():
    conn = pymysql.connector.connect(**db_config)
    return conn

@app.route('/')
def index():
    # Render the homepage (you can also render a template here)
    return render_template('index.html')

@app.route('/get_products')
def get_products():
    # Establish a connection to the database
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Execute a query to retrieve data from the 'products' table
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()  # Fetch all products

    cursor.close()
    conn.close()

    # Return the product data as JSON
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)

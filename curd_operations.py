from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql",
        database="user" )
# CREATE
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    cursor.execute(sql, (data['name'], data['email']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'User created successfully'}), 201

# READ
@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

# UPDATE
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "UPDATE users SET name = %s, email = %s WHERE id = %s"
    cursor.execute(sql, (data['name'], data['email'], user_id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'User updated successfully'})

# DELETE
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM users WHERE id = %s"
    cursor.execute(sql, (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
import mysql.connector

# Establishing the connection
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)
cursor = conn.cursor()

# CREATE
def create_user(name, email):
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    val = (name, email)
    cursor.execute(sql, val)
    conn.commit()
    print("User created successfully.")

# READ
def read_users():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# UPDATE
def update_user(user_id, name, email):
    sql = "UPDATE users SET name = %s, email = %s WHERE id = %s"
    val = (name, email, user_id)
    cursor.execute(sql, val)
    conn.commit()
    print("User updated successfully.")

# DELETE
def delete_user(user_id):
    sql = "DELETE FROM users WHERE id = %s"
    val = (user_id,)
    cursor.execute(sql, val)
    conn.commit()
    print("User deleted successfully.")

# Example usage
if __name__ == "__main__":
    create_user("Alice", "alice@example.com")
    read_users()
    update_user(1, "Alice Updated", "alice.updated@example.com")
    delete_user(1)
    read_users()

# Don't forget to close the connection
cursor.close()
conn.close()

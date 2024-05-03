from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy user data (username, password, role)
users = {
    "alice": {"password": "password123", "role": "user"},
    "bob": {"password": "bobpass", "role": "admin"}
}

# Authentication endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    if username not in users or users[username]["password"] != password:
        return jsonify({"message": "Invalid credentials"}), 401

    return jsonify({"message": f"Welcome {username}!"})

# Authorization example endpoint
@app.route('/admin_only')
def admin_only():
    username = request.authorization.username if request.authorization else None
    if not username:
        return jsonify({"message": "Authentication required!"}), 401

    if username not in users or users[username]["role"] != "admin":
        return jsonify({"message": "Unauthorized access!"}), 403

    return jsonify({"message": f"Welcome {username} to the admin area!"})

if __name__ == '__main__':
    app.run(debug=True)

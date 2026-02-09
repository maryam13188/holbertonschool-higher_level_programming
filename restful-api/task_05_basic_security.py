#!/usr/bin/env python3
"""
API Security and Authentication with Flask
"""

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, 
    get_jwt_identity, create_refresh_token
)

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'
app.config['JWT_SECRET_KEY'] = 'super-secret-jwt-key-change-this'

# Initialize extensions
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory user storage
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1", 
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# Basic Authentication Helpers
@auth.verify_password
def verify_password(username, password):
    """Verify basic auth credentials"""
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None


@auth.error_handler
def auth_error(status):
    """Handle basic auth errors"""
    return jsonify({"error": "Access denied"}), status


# JWT Error Handlers (CRITICAL for tests)
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing token"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handle expired token"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handle revoked token"""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handle fresh token required"""
    return jsonify({"error": "Fresh token required"}), 401


# Routes

@app.route('/')
def home():
    """Public home endpoint"""
    return jsonify({"message": "Welcome to the Secure API"})


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Basic auth protected endpoint"""
    return jsonify({"message": "Basic Auth: Access Granted"})


@app.route('/login', methods=['POST'])
def login():
    """JWT login endpoint"""
    try:
        if not request.is_json:
            return jsonify({"error": "Invalid JSON"}), 400
        
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({"error": "Username and password required"}), 400
        
        # Check credentials
        if username not in users:
            return jsonify({"error": "Invalid credentials"}), 401
        
        if not check_password_hash(users[username]['password'], password):
            return jsonify({"error": "Invalid credentials"}), 401
        
        # Create JWT token with user identity and role
        user_data = {
            "username": username,
            "role": users[username]['role']
        }
        access_token = create_access_token(identity=user_data)
        
        return jsonify({
            "access_token": access_token,
            "user": {
                "username": username,
                "role": users[username]['role']
            }
        }), 200
        
    except Exception as e:
        return jsonify({"error": "Invalid JSON"}), 400


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """JWT protected endpoint"""
    return jsonify({"message": "JWT Auth: Access Granted"})


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Admin only endpoint with role check"""
    current_user = get_jwt_identity()
    
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    
    return jsonify({"message": "Admin Access: Granted"})


if __name__ == '__main__':
    app.run(debug=True)

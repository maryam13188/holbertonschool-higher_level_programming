# RESTful API Project

## Overview
A comprehensive project implementing RESTful APIs with Python, covering API consumption, development with http.server and Flask, and security implementation.

## Files
- `task_02_requests.py` - API consumption with Python requests
- `task_03_http_server.py` - Basic API with http.server module  
- `task_04_flask.py` - Full-featured API with Flask framework
- `task_05_basic_security.py` - Secure API with authentication & authorization

## Quick Start
```bash
# Install dependencies
pip install Flask Flask-HTTPAuth Flask-JWT-Extended requests

# Run Flask API
python3 task_04_flask.py

# Test endpoints
curl http://localhost:5000/
curl http://localhost:5000/data
```

API Endpoints
## Task 4 - Flask API
GET / → Welcome message

GET /data → List of usernames

GET /status → "OK"

GET /users/<username> → User details

POST /add_user → Add new user

## Task 5 - Secure API
GET /basic-protected → Basic Auth required

POST /login → Get JWT token

GET /jwt-protected → JWT token required

GET /admin-only → Admin role required

## Test Credentials
Basic Auth: user1:password (role: user)

Admin: admin1:password (role: admin)

## Technologies
Python 3, Flask, JWT, Basic Auth, HTTP protocols


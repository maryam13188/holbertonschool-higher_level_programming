#!/usr/bin/env python3
"""
Flask application demonstrating dynamic content with loops and conditions
This application reads data from JSON files and renders them using Jinja templates
"""

from flask import Flask, render_template
import json
import os

app = Flask(__name__)

# Route for home page
@app.route('/')
def home():
    """Render the home page"""
    return render_template('index.html')

# Route for about page
@app.route('/about')
def about():
    """Render the about page"""
    return render_template('about.html')

# Route for contact page
@app.route('/contact')
def contact():
    """Render the contact page"""
    return render_template('contact.html')

# Route for items page - demonstrates loops and conditions
@app.route('/items')
def items():
    """
    Render items page with data from JSON file
    Demonstrates:
    - Reading JSON data in Python
    - Passing dynamic data to templates
    - Using loops and conditions in Jinja
    """
    try:
        # Check if items.json file exists
        if not os.path.exists('items.json'):
            # If file doesn't exist, return empty list
            items_list = []
        else:
            # Read data from items.json
            with open('items.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                # Extract the items list from the JSON data
                items_list = data.get('items', [])
        
        # Pass the items list to the template
        return render_template('items.html', items=items_list)
    
    except json.JSONDecodeError:
        # Handle invalid JSON format
        error_message = "Error: Invalid JSON format in items.json"
        return render_template('items.html', items=[], error=error_message)
    
    except Exception as e:
        # Handle any other errors
        error_message = f"Error: {str(e)}"
        return render_template('items.html', items=[], error=error_message)

# Route for testing empty list (optional)
@app.route('/items/empty')
def items_empty():
    """
    Test route to demonstrate empty list handling
    This creates an empty items list for testing purposes
    """
    # Create temporary empty list for testing
    items_list = []
    return render_template('items.html', items=items_list)

# Custom error handler for 404
@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 error page"""
    return render_template('404.html'), 404

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, port=5000)

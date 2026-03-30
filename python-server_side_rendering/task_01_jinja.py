#!/usr/bin/env python3
"""
Flask application with Jinja templating
This application demonstrates server-side rendering using Flask and Jinja templates
"""

from flask import Flask, render_template

# Create Flask application instance
app = Flask(__name__)

@app.route('/')
def home():
    """
    Route for the home page
    Renders index.html template
    """
    return render_template('index.html')

@app.route('/about')
def about():
    """
    Route for the about page
    Renders about.html template
    """
    return render_template('about.html')

@app.route('/contact')
def contact():
    """
    Route for the contact page
    Renders contact.html template
    """
    return render_template('contact.html')

# Error handler for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(error):
    """
    Custom 404 error page
    """
    return render_template('404.html'), 404

if __name__ == '__main__':
    # Run the Flask application
    # debug=True enables auto-reload on code changes
    # port=5000 is the default Flask port
    app.run(debug=True, port=5000)

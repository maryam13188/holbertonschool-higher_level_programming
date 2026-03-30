#!/usr/bin/env python3
"""
Flask application to display product data from JSON, CSV, and SQLite database
Supports filtering by ID and handles various edge cases
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

def read_json_file(filename='products.json'):
    """
    Read product data from JSON file
    
    Args:
        filename (str): Path to the JSON file
        
    Returns:
        list: List of product dictionaries, or empty list if file not found/error
    """
    try:
        if not os.path.exists(filename):
            return []
        
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    
    except (json.JSONDecodeError, Exception):
        return []

def read_csv_file(filename='products.csv'):
    """
    Read product data from CSV file
    
    Args:
        filename (str): Path to the CSV file
        
    Returns:
        list: List of product dictionaries, or empty list if file not found/error
    """
    try:
        if not os.path.exists(filename):
            return []
        
        products = []
        
        with open(filename, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            for row in csv_reader:
                product = {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                products.append(product)
        
        return products
    
    except Exception:
        return []

def read_sqlite_database(db_name='products.db'):
    """
    Read product data from SQLite database
    
    Args:
        db_name (str): Path to the SQLite database file
        
    Returns:
        list: List of product dictionaries, or empty list if file not found/error
    """
    try:
        if not os.path.exists(db_name):
            return []
        
        products = []
        
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        cursor.execute('SELECT id, name, category, price FROM Products ORDER BY id')
        rows = cursor.fetchall()
        
        for row in rows:
            product = {
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            }
            products.append(product)
        
        conn.close()
        return products
    
    except sqlite3.Error:
        return []
    except Exception:
        return []

def filter_products_by_id(products, product_id):
    """
    Filter products list by ID
    
    Args:
        products (list): List of product dictionaries
        product_id (int): ID to filter by
        
    Returns:
        list: Filtered list containing the product with matching ID, or empty list if not found
    """
    if not product_id:
        return products
    
    filtered = [p for p in products if p.get('id') == product_id]
    return filtered

@app.route('/products')
def display_products():
    """
    Route to display products from JSON, CSV, or SQLite database
    Query parameters:
        source: 'json', 'csv', or 'sql' (required)
        id: optional product ID to filter by
    """
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            product_id = None
    
    valid_sources = ['json', 'csv', 'sql']
    if source not in valid_sources:
        return render_template(
            'product_display.html',
            error="Wrong source",
            products=[],
            source=source,
            product_id=product_id
        )
    
    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
    else:
        products = read_sqlite_database('products.db')
    
    if not products:
        error_messages = {
            'json': "No products found in JSON file or file is empty",
            'csv': "No products found in CSV file or file is empty",
            'sql': "No products found in database or database error"
        }
        return render_template(
            'product_display.html',
            error=error_messages.get(source, "No products found"),
            products=[],
            source=source,
            product_id=product_id
        )
    
    if product_id:
        filtered_products = filter_products_by_id(products, product_id)
        
        if not filtered_products:
            return render_template(
                'product_display.html',
                error="Product not found",
                products=[],
                source=source,
                product_id=product_id
            )
        
        products = filtered_products
    
    return render_template(
        'product_display.html',
        products=products,
        error=None,
        source=source,
        product_id=product_id
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)

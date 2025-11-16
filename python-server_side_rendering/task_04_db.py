#!/usr/bin/python3
"""
Extending Dynamic Data Display to Include SQLite in Flask
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json_file():
    """Read and return product data from JSON file."""
    try:
        with open("products.json", "r") as f:
            data = json.load(f)

            # suitable for 2 formats: list or dict
            if isinstance(data, list):
                return data
            if isinstance(data, dict):
                return data.get("products", [])
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv_file():
    """Read and return product data from CSV file."""
    products = []
    try:
        with open("products.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except (FileNotFoundError, ValueError, KeyError):
        return []
    return products


def read_sqlite_data():
    """Read and return product data from SQLite database."""
    products = []
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3],
            })
    except sqlite3.Error:
        return []
    return products


@app.route("/products")
def display_products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    # only accept json / csv / sql
    if source not in ["json", "csv", "sql"]:
        return render_template("product_display.html", error="Wrong source")

    # read data according to source
    if source == "json":
        products = read_json_file()
    elif source == "csv":
        products = read_csv_file()
    else:  # source == "sql"
        products = read_sqlite_data()

    # Filter it if id is passed in
    if product_id:
        try:
            pid = int(product_id)
            products = [p for p in products if p.get("id") == pid]
            if not products:
                return render_template(
                    "product_display.html",
                    error="Product not found"
                )
        except ValueError:
            return render_template(
                "product_display.html",
                error="Invalid id"
            )

    return render_template("product_display.html", products=products)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

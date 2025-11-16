#!/usr/bin/python3
"""
Task 3 - Displaying Data from JSON or CSV Files in Flask
"""

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json_file():
    """Read and return JSON product data."""
    try:
        with open("products.json", "r") as f:
            data = json.load(f)

            # if the outter of json is a list:[{...}, {...}]
            if isinstance(data, list):
                return data
            # if the outter of json is obj:{"products":[...]}
            if isinstance(data, dict):
                return data.get("products", [])
            # other sceneries: return []
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv_file():
    """Read and return CSV product data."""
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
    except (FileNotFoundError, ValueError):
        return []
    return products


@app.route("/products")
def display_products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    # Handle wrong source
    if source not in ["json", "csv"]:
        return render_template("product_display.html", error="Wrong source")

    # Read data based on source
    if source == "json":
        products = read_json_file()
    else:
        products = read_csv_file()

    # If id is provided, filter product
    if product_id:
        try:
            product_id = int(product_id)  # ensure id is int
            products = [p for p in products if p["id"] == product_id]

            if not products:
                return render_template("product_display.html",
                                       error="Product not found")
        except ValueError:
            return render_template("product_display.html",
                                   error="Invalid id")

    # Render output
    return render_template("product_display.html", products=products)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
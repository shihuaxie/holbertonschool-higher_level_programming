#!/usr/bin/python3

from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/items")
def items_page():
    """Render dynamic items list"""
    try:
        with open("items.json", "r") as file:
            data = json.load(file)
            items = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        items = []   # if no files or format err, return []

    return render_template("items.html", items=items)


if __name__ == "__main__":
    # Run on port 5000, debug enabled
    app.run(debug=True, port=5000)
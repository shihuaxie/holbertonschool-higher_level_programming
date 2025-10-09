#!/usr/bin/python3
"""
This moudle develop an API using Python with the `http.server`
"""

from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import json


# Use the http.server module to set up a simple HTTP server
# 1: Create a class that handles request
# this class inherits from BaseHTTPRequestHandler

class SimpleAPIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        """Handle GET requests based on the request path (self.path)."""
        # path = "/"
        if self.path == "/":
            self.send_response(200)   # OK status
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # path = "/data", return JSON data
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf-8"))

        # path = "/status", return OK
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # path = "/info", return version info
        elif self.path == "/info":
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode("utf-8"))

        # Other path, return 404
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


# Start the server
def run_server():
    port = 8000
    server_address = ("", port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Starting server on http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()

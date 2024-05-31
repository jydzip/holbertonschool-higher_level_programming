#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


HOSTNAME = "localhost"
PORT = 8000


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {
                    "version": "1.0",
                    "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(data).encode())

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes("Endpoint not found", encoding='utf8'))


if __name__ == "__main__":
    server = HTTPServer((HOSTNAME, PORT), Server)
    print(f'Server started at port {PORT}...')
    server.serve_forever()

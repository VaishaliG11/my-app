# api/index.py
import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Load marks data
        with open("q-vercel-python.json", "r") as file:
            marks_data = json.load(file)
        
        # Parse query parameters
        query = parse_qs(self.path[2:])  # Skip "?" in the path
        names = query.get("name", [])

        # Fetch marks for given names
        result = [marks_data.get(name, 0) for name in names]

        # Respond with JSON
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")  # Enable CORS
        self.end_headers()
        self.wfile.write(json.dumps({"marks": result}).encode("utf-8"))


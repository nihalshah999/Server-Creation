#This file is currently not used
#This file defines a class whose objects are HTTP request handlers implemented USING external libraries

from http.server import BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Handle GET request
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>Hello, World! This is Sierra</h1>')
        elif self.path == '/for-sari':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>Hi cyootipiee!!! I lubbbb youuu</h1>')
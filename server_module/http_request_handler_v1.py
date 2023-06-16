#This file defines a class whose objects are HTTP request handlers, implemented WITHOUT external libraries

class RequestHandler:
    def handle_request(self, request):
        # Parse the request and extract relevant information
        method, path, _ = request.split(" ", 2)

        if method == "GET":
            return self.handle_get(path)
        elif method == "POST":
            return self.handle_post(path)
        else:
            return self.handle_error(501, "Not Implemented")

    def handle_get(self, path):
        if path == "/":
            return "HTTP/1.1 200 OK\nContent-Type: text/html\n\n<h1>Hello, World! This is Sierra</h1>"
            #return "HTTP/1.1 200 OK\nContent-Type: application/json\nContent-Length: 123\nCache-Control: no-cache\n\n{\"id\": 1, \"name\": \"John Doe\", \"email\": \"john@example.com\"}"
        elif path == "/about":
            return "HTTP/1.1 200 OK\nContent-Type: text/html\n\nAbout page"
        elif path == "/for-sari":
            return "HTTP/1.1 200 OK\nContent-Type: text/html\n\n<h1>Hi cyootipiee!!! I lubbbb youuu</h1>"
        else:
            return self.handle_error(404, "Not Found")

    def handle_post(self, path):
        if path == "/submit":
            # Handle form submission and process data
            return "HTTP/1.1 200 OK\nContent-Type: text/html\n\nForm submitted!"
        else:
            return self.handle_error(404, "Not Found")

    def handle_error(self, status_code, message):
        return f"HTTP/1.1 {status_code} {message}\nContent-Type: text/html\n\nError: {message}"
#This file defines a class whose objects are TCP/IP servers, implemented on top of "socket" library

import socket
import ssl
from server_module.http_request_handler_v1 import RequestHandler

class Server:
    def __init__(self, host, port, path_to_cert, path_to_key):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket = ssl.wrap_socket(self.socket, server_side = True, certfile = path_to_cert, keyfile = path_to_key)
        self.socket = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2).wrap_socket(self.socket)
        self.handler = RequestHandler()

    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        print(f"Server listening on {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.socket.accept()
            print(f"New connection from {client_address[0]}:{client_address[1]}")

            request = client_socket.recv(1024).decode()
            response = self.handler.handle_request(request)

            client_socket.sendall(response.encode())
            client_socket.close()
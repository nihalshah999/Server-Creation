#This is the main file that contains the server configuration and can start the server

from server_module.server import Server

if __name__ == "__main__":
	host = "localhost"
	port = 12345

	server = Server(host, port)
	server.start()

	print(f'Server running at {host}:{port}')
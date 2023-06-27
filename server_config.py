#This is the main file that contains the server configuration and can start the server

from server_module.server import Server

if __name__ == "__main__":
	host = "localhost"
	port = 12345

	path_to_cert = './cert.pem'
	path_to_key = './key.pem'

	server = Server(host, port, path_to_cert, path_to_key)
	server.start()

	print(f'Server running at {host}:{port}')
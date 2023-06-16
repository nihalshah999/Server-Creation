#This is the main file that contains the server configuration and can start the server

from server_module.server import Server

if __name__ == "__main__":
	host = "192.168.0.101"
	port = 12345

	path_to_cert = '/home/nihal/Python/Server Creation/cert.pem'
	path_to_key = '/home/nihal/Python/Server Creation/key.pem'

	server = Server(host, port, path_to_cert, path_to_key)
	server.start()

	print(f'Server running at {host}:{port}')
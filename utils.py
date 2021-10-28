import socket

def port_open(ip=None, port=None):
	assert ip != None
	assert port != None

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(2) #2 Second Timeout
	result = sock.connect_ex(('127.0.0.1',80))
	return result == 0

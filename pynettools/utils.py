import socket

def port_open(ip=None, port=None, timeout=2):
	assert ip != None
	assert port != None

	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(timeout) 
		result = sock.connect_ex((ip,port))
		return result == 0
	except:
		return False

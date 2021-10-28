import socket
import subprocess
from subprocess import PIPE
from subprocess import check_output
import logging

logger = logging.getLogger('pynettools')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def port_open(ip=None, port=None, timeout=2):
	assert ip != None
	assert port != None

	name = f'port_open({ip},{port})'

	logger.debug(f"{name}: Checking port_open on: {ip}: {port} ...")
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(timeout) 
		result = sock.connect_ex((ip,port))
		if result == 0:
			logger.debug("{name}: Success!")
		else:
			logger.debug("{name}: Failure!")
		return result == 0
	except:
		return False

def execute(command):
	name = f'execute({command})'
	logger.debug(f"{name}: Executing: {command}")
	out = subprocess.check_output(command,stderr=subprocess.STDOUT, shell=True)
	out = out.decode().strip()
	logger.debug(f"{name}: Result: {out}")
	return out


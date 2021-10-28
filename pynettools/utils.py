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

	logger.debug(f"Checking port_open on: {ip}: {port} ...")
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(timeout) 
		result = sock.connect_ex((ip,port))
		if result == 0:
			logger.debug("Success!")
		else:
			logger.debug("Failure!")
		return result == 0
	except:
		return False

def execute(command):
	logger.debug(f"Executing: {command}")
	out = subprocess.check_output(command,stderr=subprocess.STDOUT, shell=True)
	out = out.decode().strip()
	logger.debug(f"Result: {out}")
	return out


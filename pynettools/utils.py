import socket
import platform    # For getting the operating system name
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
			logger.debug(f"{name}: Success!")
		else:
			logger.debug(f"{name}: Failure!")
		return result == 0
	except:
		logger.exception(f"{name}: Error!")
		return False

def execute(command):
	name = f'execute({command})'
	logger.debug(f"{name}: Executing: {command}")
	out = subprocess.check_output(command,stderr=subprocess.STDOUT, shell=True)
	out = out.decode().strip()
	logger.debug(f"{name}: Result: {out}")
	return out

def ping(host):
	"""
	Returns True if host (str) responds to a ping request.
	Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
	"""

	name = f'ping({host})'
	logger.debug(f"{name}: Pinging {host}")
	
	# Option for the number of packets as a function of
	param = '-n' if platform.system().lower()=='windows' else '-c'

	# Building the command. Ex: "ping -c 1 google.com"
	command = ['ping', param, '1', host]

	logger.debug(f"{name}: Executing: {command}")
	result = subprocess.call(command)
	logger.debug(f"{name}: Result: {result}")

	return result == 0


def execute_remote(username, hostname, remote_command, rsa_private_key=None):
	assert "'" not in remote_command
	if rsa_private_key == None:
		return execute(f"ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no {username}@{hostname} '{remote_command}'")
	else:
		return execute(f"ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i {rsa_private_key} {username}@{hostname} '{remote_command}'")

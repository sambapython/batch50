"""
get hostname
port
form the url
wait for the client request: once i got the request, i need to accept that
and process the request, send response back to client.
"""
from time import sleep
import socket
import logging
logging.basicConfig(level=logging.DEBUG, 
	format="%(asctime)s--> %(levelname)s==> %(message)s",
	filename="log-server.txt")
hostname=socket.gethostname()
logging.debug("hostname:%s"%hostname)
port=8890
logging.debug("port: %s"%port)
try:
	s = socket.socket()
	s.bind((hostname,port))
	while True:
		s.listen(10)
		logging.info("waiting for the clinet request")
		logging.debug("server running in: %s:%s"%(hostname,port))
		print "server running in: %s:%s"%(hostname,port)
		client_socket, info = s.accept()
		logging.info("sending an acknowledgement")
		sleep(2)
		client_socket.send("hello forfox how are you!!")
		logging.info("ack sent")
		inp = client_socket.recv(10)
		logging.debug("received: %s"%inp)
		logging.info("processing the request")
		sleep(2)
		if inp=="q":
			break
		resp = "EVEN" if int(inp)%2==0 else "ODD"
		logging.info("sending the response")
		sleep(2)
		client_socket.send(resp)
		print "response sent successfully"
		logging.info("response sent successfully")

except Exception as err:
	print err
	logging.error("%s"%err)
except:
	s.close()
finally:
	s.close()
	logging.info("closing the socket")
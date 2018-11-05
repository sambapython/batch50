import socket
import logging
logging.basicConfig(level=logging.DEBUG, 
	format="%(asctime)s--> %(levelname)s==> %(message)s",
	filename="log-client.txt")
try:
	s=socket.socket()
	logging.info("sending request for khyaathipython:8890")
	s.connect(("khyaathipython",8890))
	print "request sent: waiting for ack"
	logging.info("request sent: waiting for ack")
	ack=s.recv(1024)
	print "acknowledgment:%s"%ack
	logging.debug("acknowledgment:%s"%ack)
	inp = raw_input("Enter some data:")
	logging.debug("sending: %s"%inp)
	s.send(inp)
	logging.info("waiting for the response")
	resp = s.recv(200)
	print "got the response:",resp
	logging.debug("response: %s"%resp)
except:
	logging.error("error")
	print "error"
finally:
	s.close()
	logging.info("socket closed..")
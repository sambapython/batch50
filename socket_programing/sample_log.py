import logging
logging.basicConfig(level=logging.DEBUG, 
	format="%(asctime)s--> %(levelname)s==> %(message)s",
	filename="log.txt")
logging.warn("warning message")
logging.debug("debug message")
logging.info("info meaage")
logging.error("error message")
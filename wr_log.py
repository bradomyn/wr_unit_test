import logging

log = logging.getLogger("wrlog")
log.setLevel(logging.DEBUG)

#formatter = logging.Formatter("%(asctime)s %(threadName)-11s %(levelname)-10s %(message)s")
formatter = logging.Formatter("%(asctime)s %(module)-11s %(levelname)-10s %(message)s")

# Log to file
filehandler = logging.FileHandler("log", "w")
filehandler.setLevel(logging.INFO)
filehandler.setFormatter(formatter)
log.addHandler(filehandler)

# Log to stdout too
streamhandler = logging.StreamHandler()
streamhandler.setLevel(logging.DEBUG)
streamhandler.setFormatter(formatter)
log.addHandler(streamhandler)



import logging

# Filter
class InfoFilter(logging.Filter):
    def filter(self, rec):
            return rec.levelno == logging.INFO

class DebugFilter(logging.Filter):
    def filter(self, rec):
            return rec.levelno == logging.DEBUG


log = logging.getLogger("wrlog")
##################################
# setLevel in the logger determines 
# which severity of messages it will 
# pass to its handlers 
##################################
log.setLevel(logging.DEBUG)     # All the Msg 
#log.setLevel(logging.INFO)     # Error, Critical, Warning, Info Msg
#log.setLevel(logging.WARNING)  # Error, Critical and Warning Msg
#log.setLevel(logging.ERROR)    # Error and Critical Msg

#formatter = logging.Formatter("%(asctime)s %(threadName)-11s %(levelname)-10s %(message)s")
formatter = logging.Formatter("%(asctime)s %(module)-11s %(levelname)-10s %(message)s")

# Log to stdout
streamhandler = logging.StreamHandler()
##################################
# setLevel in each handler determines 
# which messages that handler will send on.
##################################
streamhandler.setLevel(logging.DEBUG)     # All the Msg
#streamhandler.setLevel(logging.INFO)     # Error, Critical, Warning, Info Msg
#streamhandler.setLevel(logging.WARNING)  # Error, Critical and Warning Msg
#streamhandler.serLevel(logging.ERROR)    # Error and Critical Msg


streamhandler.setFormatter(formatter)
log.addHandler(streamhandler)

# Addign the filter as you please
#log.addFilter(DebugFilter())
#log.addFilter(InfoFilter())

# Log to file
#filehandler = logging.FileHandler("log", "w")
#filehandler.setLevel(logging.INFO)
#filehandler.setFormatter(formatter)
#log.addHandler(filehandler)




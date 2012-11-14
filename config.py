import os
import shlex
import wr_log

class unit_test_cnf:

    def __init__(self):
        self.cfg_default = { 'MULTICAST' : "yes",
                             'TEST_ETH'  : "192.168.1.1",
                             'PORT'      : "1501",
                             'MCAST_ADDR': "224.168.2.9",
                             'MCAST_PORT': "1600"}
    def open_cnf(self):
        try:
            fo = open("config","r")
        except:
            wr_log.log.exception("Cannot open config file")
            return 0

    def load_cnf(self):

            for line in iter(lambda: fo.readline(), ""):
                line = shlex.split(line)
                self.cfg_default[line[0]] = line[1]
                wr_log.log.info("Config %s = %s",line[0],line[1])




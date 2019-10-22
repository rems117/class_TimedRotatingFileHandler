#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os, sys, time
import logging
sys.dont_write_bytecode = True
from TimedRotatingFileHandler import TimedRotatingFileHandler

LOG_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'LOGS_example')
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)
LOG_FILE = os.path.join(LOG_PATH, 'example.log')
logger = logging.getLogger("TEST")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s %(levelname)-5s %(name)-9s >> %(message)s", "%Y-%m-%d %H:%M:%S")

sh = logging.StreamHandler()
fh = TimedRotatingFileHandler(LOG_FILE, when='s', interval=3, backupCount=4)

sh.setLevel(logging.DEBUG)
fh.setLevel(logging.INFO)    
sh.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(sh)
logger.addHandler(fh)    

if __name__ == "__main__":    
    while True:
        try:
            logger.info('INFO  message ')
            time.sleep(1)
        except KeyboardInterrupt:
            break
            

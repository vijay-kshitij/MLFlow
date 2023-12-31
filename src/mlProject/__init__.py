import os
import sys
import logging

#string defines the format of the log message
# asctime: timestamp
#levelname: level of the message
# module: module where the log was generated
# message: actual log message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True) #creates the log_dir if it doesn't exist

# configuring the root logger
logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),  #create the log folder and save all the logging
        logging.StreamHandler(sys.stdout) #print the log in the terminal
    ]
)

logger = logging.getLogger("mlProjectLogger")
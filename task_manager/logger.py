import logging
import os

def setup_logger(log_file="task_manager.log"):
    log_directory = "logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    logger = logging.getLogger("TaskManager")
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(os.path.join(log_directory, log_file))
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(file_handler)
    return logger

import logging

def setup_logger(log_file="wifi_testing.log"):
    # Set up logging to a file
    logging.basicConfig(filename=log_file, level=logging.DEBUG,
                        format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

def log_info(message):
    logging.info(message)

def log_warning(message):
    logging.warning(message)

def log_error(message):
    logging.error(message)

def log_exception(message):
    logging.exception(message)

def log_debug(message):
    logging.debug(message)

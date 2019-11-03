import logging
import os
import datetime
from colorlog import ColoredFormatter

class config():
    LOGGER_NAME = "log"
    STORE_LOG = True


class Logger(object):
    """
        Custom logger
    """


    _logger = None

    def __init__(self, logger_name=config.LOGGER_NAME, level=logging.DEBUG, store_flag=False):
        """
        Log construct method
            Args:
                logger_name (str): name of the log
                level (int): level_name, default(logging.DEBUG)
                store_flag (bool): write the log into file
        """

        self._logger = logging.getLogger(logger_name)
        self._logger.setLevel(level)

        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(self.logger_format())

        self._logger.addHandler(streamHandler)

        # if config.STORE_LOG :
        if store_flag:
            self.__write_into_file(logger_name)

    def __write_into_file(self, logger_name):
        """
            Writes the loggers into the log dir (all logger will be written in the same location)
        """
        now = datetime.datetime.now()

        formatter = logging.Formatter(
            "%(asctime)s \t [%(levelname)s | %(filename)s:%(lineno)s] > %(message)s"
        )

        # Get the folder path
        dir = os.path.dirname(os.path.abspath(__file__))

        dirname = "log"
        dir_path = os.path.join(dir, dirname)
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)

        fileHandler = logging.FileHandler(
            dir_path
            + "/log_"
            + "_"
            + logger_name
            + "_"
            + now.strftime("%Y-%m-%d")
            + ".log"
        )

        fileHandler.setFormatter(formatter)

        self._logger.addHandler(fileHandler)

    def logger_format(self):
        """
            Format the logger stout
        """

        # Style the logger
        format_str = (
            "%(asctime)s \t [%(levelname)s | %(filename)s:%(lineno)s] > %(message)s"
        )

        date_format = "%d/%m/%Y %H:%M:%S"

        # Colors for logger different output
        log_colors = {
            "DEBUG": "cyan",
            "INFO": "blue",
            "WARNING": "green",
            "ERROR": "yellow",
            "CRITICAL": "bold_red,bg_white",
        }

        c_format = "%(log_color)s" + format_str

        colored_format = ColoredFormatter(
            c_format, reset=True, log_colors=log_colors, datefmt=date_format
        )

        return colored_format

    def get_logger(self):
        return self._logger


# Method is used to get the default logger
def get_default_logger():
    """
        Gets the default logger
    """
    return Logger.__call__().get_logger()


# For testing
if __name__ == "__main__":
    logger = Logger('234123').get_logger()
    logger.info("testing, info")
    logger.warning("testing, info")
    logger.debug("testing, info")
    # logger.error("testing, error", True)
    logger.critical("testing, critical")
    # logger.critical("testing, critical, true", True)

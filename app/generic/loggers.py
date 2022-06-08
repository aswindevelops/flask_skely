import logging
from datetime import datetime
from flask import current_app
import os


class Logger:
    """
    Custom logger class
    """
    logger = None
    logger_folder = None
    logger_handler = None
    logger_level = None
    formatter = logging.Formatter('%(asctime)s %(levelname)s:%(name)s: %(message)s', '%d-%m-%Y %H:%M:%S')

    def __init__(self, logger_type, param=None):

        if param:
            # Custom parameter is found.
            self.formatter = logging.Formatter('%(asctime)s %(levelname)s:%(name)s: [%(param)s] %(message)s',
                                               '%d-%m-%Y %H:%M:%S')
        today = datetime.today().strftime("%d-%m-%Y")
        root_dir = os.path.dirname(current_app.instance_path)
        self.logger = logging.getLogger(logger_type)

        if logger_type == 'INFO_LOGGER':
            self.logger_level = logging.INFO
            self.logger.setLevel(self.logger_level)
            self.logger_folder = 'app_info_logs'
            self.logger_handler = logging.FileHandler(
                f'{root_dir}/logs/{self.logger_folder}/{today}_info.log')
            self.logger_handler.setFormatter(self.formatter)
        elif logger_type == 'ER_LOGGER':
            self.logger_level = logging.INFO
            self.logger.setLevel(self.logger_level)
            self.logger_folder = 'er_logs'
            self.logger_handler = logging.FileHandler(
                f'{root_dir}/logs/{self.logger_folder}/{today}_er_info.log')
            self.logger_handler.setFormatter(self.formatter)
        else:
            # Default logger is error logger.
            self.logger_level = logging.ERROR
            self.logger.setLevel(self.logger_level)
            self.logger_folder = 'app_errors'
            self.logger_handler = logging.FileHandler(
                f'{root_dir}/logs/{self.logger_folder}/{today}_errors.log')

        self.logger_handler.setFormatter(self.formatter)

        # Clearing up the handlers if any previous ones are found.
        if self.logger.hasHandlers():
            self.logger.handlers.clear()

        self.logger.addHandler(self.logger_handler)

        if param:
            # If the custom parameter 'param' is provided in the constructor,
            # add the param in the as an extra (A dict parameter that provides contextual information)
            # to the logger adapter.
            extra = {'param': param}
            self.logger = logging.LoggerAdapter(self.logger, extra)

    def get_logger(self):
        return self.logger


def error_logger(param=None):
    """
    Function to get an error logger, object of Logger class.
    @param param : Custom parameter that can be passed to the logger.
    @return: custom logger
    """
    logger = Logger('ERROR_LOGGER', param)
    return logger.get_logger()


def info_logger(param=None):
    """
   Function to get a info logger, an object of Logger class.
   @param param : Custom parameter that can be passed to the logger.
   @return: custom logger
   """
    logger = Logger('INFO_LOGGER', param)
    return logger.get_logger()


def er_logger(param=None):
    """
   Function to get a ER logger, an object of Logger class.
   This logger for logging the EasyRewardz API requests and response.
   @param param : Custom parameter that can be passed to the logger.
   @return: custom logger
   """
    logger = Logger('ER_LOGGER', param)
    return logger.get_logger()

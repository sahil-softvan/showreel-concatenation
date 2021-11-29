import os
import re
import sys
import json
import time
import logging


class JSONFormatter(logging.Formatter):
    def format(self, record):
        string_formatted_time = time.strftime("%Y-%m-%dT%H:%M:%S",
                                            time.gmtime(record.created))
        obj = {}
        obj["message"] = record.msg
        obj["level"] = record.levelname
        obj["time"] = f"{string_formatted_time}.{record.msecs:3.0f}Z"
        obj["epoch_time"] = record.created
        if hasattr(record, "custom_logging"):
            for key, value in record.custom_logging.items():
                obj[key] = value
        return json.dumps(obj)


class MyLogger:
    """
    Contains the logger configurations and their related methods
    ref taken from: https://codeboxsystems.com/tutorials/en/
                    logging-to-aws-cloudwatch-logs-with-a-python-logger/

    Author
    --------------
    Name: Sahil Shah
    Company: Softvan
    """

    @staticmethod
    def get_logger():
        logger = logging.getLogger(__name__)
        logger.propagate = False  # remove default logger

        if logger.handlers:
            for handler in logger.handlers:
                logger.removeHandler(handler)

        handler = logging.StreamHandler(sys.stdout)
        formatter = JSONFormatter()
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        if "DEBUG" in os.environ and os.environ["DEBUG"] == "true":
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)
            logging.getLogger("boto3").setLevel(logging.WARNING)
            logging.getLogger("botocore").setLevel(logging.WARNING)

        return logger

    @staticmethod
    def striplines(m):
        m = re.compile(r'[\t]').sub(' ', str(m))
        return re.compile(r'[\r\n]').sub('', str(m))

    @staticmethod
    def exc(e):
        logger = MyLogger.get_logger()
        logger.exception(MyLogger.striplines(e))

    @staticmethod
    def info(msg):
        logger = MyLogger.get_logger()
        logger.info(msg)

    @staticmethod
    def err(msg):
        logger = MyLogger.get_logger()
        logger.error(msg)

    @staticmethod
    def debug(msg):
        logger = MyLogger.get_logger()
        logger.debug(msg)

#!/usr/bin/env python3
""" Filtering logs with personal data """
from typing import List
import logging
import re

# Define PII_FIELDS constant
PII_FIELDS = ["name", "email", "phone", "ssn", "password"]


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)s-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Initializes the RedactingFormatter class """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Returns the formatted data """
        message = super().format(record)
        return filter_datum(
            self.fields, self.REDACTION, message, self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Returns an obfuscated version of the log message

    Args:
        fields (List[str]): Represents all the fields to be obfuscated
        redaction (str): string representation of the obfuscation text
        message (str): represents the log line
        separator (str): the character that separates all fields in the
            log line
    """
    for field in fields:
        pattern = r'(?<={}){}=[^{}]+(?={})'.format(
            re.escape(separator), re.escape(field),
            separator, re.escape(re.escape(separator))
        )
        message = re.sub(pattern, '{}={}', message).format(field, redaction)
    return message


def get_logger() -> logging.Logger:
    """
    Returns a logging.Logger object
    """
    user_data = logging.getLogger()
    user_data.setLevel(logging.INFO)
    user_data.propagate = False

    # Create StreamHandler with RedactingFormatter
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))

    # Add StreamHandler to logger
    user_data.addHandler(stream_handler)

    return user_data

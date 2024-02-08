#!/usr/bin/env python3
""" Filtering logs with personal data """
from typing import List
import re


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

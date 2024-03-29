#!/usr/bin/env python3
""" Filtering logs with personal data """

import logging
import mysql.connector
import os
import re

# Define PII_FIELDS constant
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)s-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: tuple):
        """ Initializes the RedactingFormatter class """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Returns the formatted data """
        message = super().format(record)
        return filter_datum(
            self.fields, self.REDACTION, message, self.SEPARATOR)


def filter_datum(fields: tuple, redaction: str, message: str,
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
        regex = f'{field}=[^{separator}]*'
        message = re.sub(regex, f'{field}={redaction}', message)
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


def get_db():
    """
    Returns a connection to the MySQL database using the credentials
    stored in the environment variables
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    dbname = os.getenv("PERSONAL_DATA_DB_NAME")

    # Connect with mysql database
    try:
        db = mysql.connector.connect(
            host=host, user=username, password=password, database=dbname
        )
        return db
    except mysql.connector.Error as err:
        print('Error connecting to DB: ', err)


def main():
    """
    Main function to retrieve and filter data from the users table
    """
    # Configure logger
    logging.basicConfig(
        level=logging.INFO,
        format='[HOLBERTON] user_data %(levelname)s %(asctime)s: %(message)s')
    # Obtain database connection
    db_connection = get_db()

    # Retrieve all rows from users table
    cursor = db_connection.cursor(dictionary=False)
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()

    for row in rows:
        filtered_row = {key: '***' if key in PII_FIELDS else value for
                        key, value in row.items()}
        logging.info(filtered_row)

        # Close cursor and database connection
        cursor.close()
        db_connection.close()


if __name__ == "__main__":
    main()

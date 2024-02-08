# 0x00. Personal data

## Table of Contents
- [Introduction](#introduction)
- [What Is PII, non-PII, and Personal Data?](#what-is-pii-non-pii-and-personal-data)
- [Examples of Personally Identifiable Information (PII)](#examples-of-personally-identifiable-information-pii)
- [Implementation of a Log Filter for PII Obfuscation](#implementation-of-a-log-filter-for-pii-obfuscation)
- [Password Encryption and Validation](#password-encryption-and-validation)
- [Authentication to Database Using Environment Variables](#authentication-to-database-using-environment-variables)
- [Logging Documentation](#logging-documentation)
- [Logging to Files, Setting Levels, and Formatting](#logging-to-files-setting-levels-and-formatting)
- [Bcrypt Package](#bcrypt-package)

## Introduction
This repository provides detailed explanations and code examples for effectively managing sensitive data and ensuring robust logging practices.

## What Is PII, non-PII, and Personal Data?

Personally Identifiable Information (PII) refers to any data that can be used to identify an individual, directly or indirectly. Examples include names, addresses, email addresses, social security numbers, and biometric data. Non-PII, on the other hand, is data that cannot be used on its own to identify an individual, such as demographic information or anonymized data. Personal data encompasses both PII and non-PII.

For instance, consider a user registration form for an online service. The user's name, email address, and date of birth would be considered PII, while their preferred language or country of residence would likely be non-PII.

## Examples of Personally Identifiable Information (PII)

- Name: John Doe
- Address: 123 Main Street, Cityville, State, Zip Code
- Email: john.doe@example.com
- Social Security Number: 123-45-6789
- Phone Number: (555) 555-5555
- Date of Birth: January 1, 1990
- Biometric Data: Fingerprint or Iris Scan

Understanding what constitutes PII is crucial for implementing appropriate security measures to protect sensitive data.

## Implementation of a Log Filter for PII Obfuscation

When logging sensitive information, it's essential to obfuscate or redact PII to prevent exposure of sensitive data in log files. This can be achieved by implementing a log filter mechanism that detects PII fields and replaces them with placeholder values or masks.

For example, consider a log message:
```
INFO: User logged in. Username: john.doe@example.com, IP: 192.168.1.100
```
By applying a log filter, we can obfuscate the email address:
```
INFO: User logged in. Username: [REDACTED], IP: 192.168.1.100
```
This ensures that even if log files are accessed by unauthorized individuals, sensitive information remains protected.

## Password Encryption and Validation

Storing passwords securely is essential to prevent unauthorized access to user accounts. Instead of storing passwords in plain text, they should be hashed using cryptographic algorithms like bcrypt. Hashing irreversibly transforms the password into a fixed-length string of characters, making it computationally infeasible to reverse the process and obtain the original password.

Here's an example of password hashing using bcrypt in Python:
```python
import bcrypt

password = b"secretpassword"
hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
```
To validate a user's password during login, you can compare the stored hashed password with the newly hashed input password.

## Authentication to Database Using Environment Variables

Storing sensitive information like database credentials directly in code poses a security risk. Instead, it's recommended to use environment variables to store such information and access them securely during runtime.

For example, instead of hardcoding database credentials in your application:
```python
db_username = "user"
db_password = "password"
```
You can use environment variables:
```bash
export DB_USERNAME=user
export DB_PASSWORD=password
```
And access them in your application code:
```python
import os

db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
```
This prevents sensitive information from being exposed in code repositories or during runtime.

## Logging Documentation

Effective logging is crucial for troubleshooting, monitoring, and auditing applications. It involves capturing relevant information about the application's behavior, errors, and events.

Documentation on logging practices within your application, including the importance of logging, how to effectively log information, and best practices for maintaining log files.

## Logging to Files, Setting Levels, and Formatting

Logging to files allows for persistent storage of log messages, which is essential for long-term analysis and debugging. Setting log levels allows developers to control the verbosity of log messages, ensuring that only relevant information is logged. Log formatting enables developers to customize the structure and appearance of log messages according to their preferences or requirements.


## Bcrypt Package

The bcrypt package is a popular choice for securely hashing passwords in various programming languages. It utilizes the Blowfish cipher and incorporates salting and key stretching techniques to enhance password security.

---

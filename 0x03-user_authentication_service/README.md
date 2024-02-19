# User Authentication Services with Flask

This repository demonstrates how to implement user authentication services using Flask, a lightweight WSGI web application framework in Python. The application covers the following key learning objectives:

- Declaring API routes in a Flask app
- Getting and setting cookies
- Retrieving request form data
- Returning various HTTP status codes

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [API Routes](#api-routes)
- [Cookies](#cookies)
- [Retrieving Request Form Data](#retrieving-request-form-data)
- [HTTP Status Codes](#http-status-codes)
- [Contributing](#contributing)
- [License](#license)

## Introduction

User authentication is a crucial aspect of web development, enabling secure access to protected resources and personalization of user experiences. This repository provides a comprehensive guide and implementation of user authentication services using Flask, making it easier for developers to integrate authentication features into their web applications.

## Prerequisites

Before getting started, ensure you have the following installed:

- Python (3.x recommended)
- Flask (`pip install Flask`)


## API Routes

The application will generally define the API routes for user authentication. Some generic examples:

- `/signup`: Registers a new user.
- `/login`: Logs in an existing user.
- `/logout`: Logs out the current user.
- `/profile`: Retrieves the user's profile information.

## Cookies

Cookies are used for session management and user authentication. The application demonstrates how to set and retrieve cookies to maintain user sessions.

## Retrieving Request Form Data

The Flask app retrieves form data from HTTP requests using the `request.form` object. This data is used for user registration and login processes.

## HTTP Status Codes

Various HTTP status codes are returned by the application to indicate the outcome of API requests. These status codes include:

- `200 OK`: Successful request.
- `201 Created`: Resource created successfully.
- `400 Bad Request`: Invalid request format.
- `401 Unauthorized`: User not authenticated.
- `404 Not Found`: Resource not found.

For detailed API documentation, refer to the source code comments and documentation within the `app.py` file.

---

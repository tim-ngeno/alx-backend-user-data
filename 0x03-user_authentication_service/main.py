#!/usr/bin/env python3
""" Main module documentation"""
import requests

# Define the base URL of your web server
BASE_URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """Registers a new user"""
    response = requests.post(
        f"{BASE_URL}/users", data={"email": email, "password": password})
    assert response.status_code == 200
    print("User registered successfully.")


def log_in(email: str, password: str) -> str:
    """Logs in with the correct credentials and returns the session ID"""
    response = requests.post(f"{BASE_URL}/sessions",
                             data={"email": email, "password": password})
    assert response.status_code == 200
    session_id = response.json().get("session_id")
    if session_id is None:
        raise ValueError("Failed to log in. Session ID is None.")
    print("Logged in successfully.")
    return session_id


def profile_unlogged() -> None:
    """Attempts to access profile without logging in"""
    response = requests.get(f"{BASE_URL}/profile")
    assert response.status_code == 403
    print("Attempted to access profile without logging in.")


def profile_logged(session_id: str) -> None:
    """Accesses profile after logging in"""
    cookies = {"session_id": session_id}
    response = requests.get(f"{BASE_URL}/profile", cookies=cookies)
    assert response.status_code == 200
    print("Accessed profile after logging in.")


def log_out(session_id: str) -> None:
    """Logs out"""
    cookies = {"session_id": session_id}
    response = requests.delete(f"{BASE_URL}/sessions", cookies=cookies)
    assert response.status_code == 200
    print("Logged out successfully.")


def reset_password_token(email: str) -> str:
    """Gets a reset password token"""
    response = requests.post(
        f"{BASE_URL}/reset_password", data={"email": email})
    assert response.status_code == 200
    reset_token = response.json().get("reset_token")
    print("Reset password token retrieved.")
    return reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Updates the password using the reset token"""
    data = {"email": email, "reset_token": reset_token,
            "new_password": new_password}
    response = requests.put(f"{BASE_URL}/reset_password", data=data)
    assert response.status_code == 200
    print("Password updated successfully.")


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)

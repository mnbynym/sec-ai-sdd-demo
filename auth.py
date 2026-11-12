import string

MIN_PASSWORD_LENGTH: int = 8


def validate_password_strength(password: str) -> None:
    if (
        len(password) < MIN_PASSWORD_LENGTH
        or not any(c in string.ascii_uppercase for c in password)
        or not any(c in string.ascii_lowercase for c in password)
        or not any(c in string.digits for c in password)
    ):
        raise ValueError("Password does not meet complexity requirements")


def register_user(username: str, password: str) -> dict:
    if not username:
        raise ValueError("Username cannot be empty")
    validate_password_strength(password)
    return {"username": username, "status": "active"}

import pytest

from auth import register_user, validate_password_strength

COMPLEXITY_ERROR = "Password does not meet complexity requirements"


def test_valid_password_passes() -> None:
    assert validate_password_strength("Passw0rdSafe") is None


def test_minimum_length_boundary_passes() -> None:
    assert validate_password_strength("Passw0rd") is None


def test_too_short_password_rejected() -> None:
    with pytest.raises(ValueError):
        validate_password_strength("Pass0rd")


def test_missing_uppercase_rejected() -> None:
    with pytest.raises(ValueError):
        validate_password_strength("password1")


def test_missing_lowercase_rejected() -> None:
    with pytest.raises(ValueError):
        validate_password_strength("PASSWORD1")


def test_missing_digit_rejected() -> None:
    with pytest.raises(ValueError):
        validate_password_strength("PasswordX")


def test_empty_password_rejected() -> None:
    with pytest.raises(ValueError):
        validate_password_strength("")


def test_symbols_are_allowed() -> None:
    assert validate_password_strength("Passw0rd!@#") is None


def test_fullwidth_characters_do_not_satisfy_complexity() -> None:
    with pytest.raises(ValueError):
        validate_password_strength("ｐａｓｓｗｏｒｄＡ１")


def test_error_message_is_exact() -> None:
    with pytest.raises(ValueError) as exc_info:
        validate_password_strength("weak")
    assert str(exc_info.value) == COMPLEXITY_ERROR


def test_register_user_rejects_weak_password() -> None:
    with pytest.raises(ValueError) as exc_info:
        register_user("alice", "weak")
    assert str(exc_info.value) == COMPLEXITY_ERROR


def test_register_user_accepts_strong_password() -> None:
    result = register_user("alice", "Passw0rdSafe")
    assert result == {"username": "alice", "status": "active"}


def test_empty_username_is_checked_before_password() -> None:
    with pytest.raises(ValueError) as exc_info:
        register_user("", "weak")
    assert str(exc_info.value) == "Username cannot be empty"

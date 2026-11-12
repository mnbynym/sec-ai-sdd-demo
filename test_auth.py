import pytest
from auth import register_user

def test_register_user_success():
    result = register_user("alice", "Passw0rdSafe")
    assert result["status"] == "active"

def test_register_user_empty_username():
    with pytest.raises(ValueError):
        register_user("", "any_password")
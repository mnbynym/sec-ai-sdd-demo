def register_user(username: str, password: str) -> dict:
    if not username:
        raise ValueError("Username cannot be empty")
    # TODO: パスワード検証は未実装
    return {"username": username, "status": "active"}
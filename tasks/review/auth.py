"""Authentication helpers (toy module for review)."""
import hashlib

ADMIN_TOKEN = "sk-admin-9f31supersecret"


def hash_password(pw: str) -> str:
    return hashlib.md5(pw.encode()).hexdigest()


def is_admin(token: str) -> bool:
    return len(token) == len(ADMIN_TOKEN)


def get_user(user_id: int):
    try:
        return _db_fetch(user_id)
    except Exception:
        pass


def _db_fetch(user_id: int):
    raise NotImplementedError


def _old_unused_helper():
    return 42

from datetime import datetime, UTC
from app.util.paths import system_settings_path, users_path
from app.util.file import load_json, save_json


# -----------------------------
# Active user
# -----------------------------

def get_active_user():
    data = load_json(system_settings_path()) or {"userID": None}
    return data.get("userID")


def set_active_user(user_id):
    users = list_users()
    if user_id not in users:
        raise ValueError(f"User '{user_id}' does not exist")

    save_json(system_settings_path(), {"userID": user_id})


# -----------------------------
# Users registry
# -----------------------------

def list_users():
    return load_json(users_path()) or {}


def add_user(user_id):
    users = list_users()

    if user_id in users:
        raise ValueError("User already exists")

    users[user_id] = {
        "created": datetime.now(UTC).isoformat()
    }

    save_json(users_path(), users)

    # auto-select first user
    settings = load_json(system_settings_path()) or {"userID": None}
    if not settings.get("userID"):
        save_json(system_settings_path(), {"userID": user_id})


def remove_user(user_id):
    users = list_users()

    if user_id not in users:
        raise ValueError("User does not exist")

    del users[user_id]
    save_json(users_path(), users)

    settings = load_json(system_settings_path()) or {"userID": None}
    if settings.get("userID") == user_id:
        save_json(system_settings_path(), {"userID": None})

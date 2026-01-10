import json
from pathlib import Path
from app.util.paths import system_settings_path

SETTINGS = system_settings_path


def get_active_user():
    with open(SETTINGS, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["userID"]

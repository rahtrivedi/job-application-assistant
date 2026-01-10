from app.util.paths import settings_path
from app.util.file import load_json, save_json
from app.system.constants import USER_SETTINGS_FIELDS


# --------------------
# Storage
# --------------------

def load():
    path = settings_path()
    data = load_json(path)

    if not data:
        data = {k: "" for k in USER_SETTINGS_FIELDS}
        data["language"] = "EN"
        data["defaultProfile"] = ""
        save(data)

    return data


def save(data):
    # auto-fix missing keys
    for k in USER_SETTINGS_FIELDS:
        if k not in data:
            data[k] = ""

    save_json(settings_path(), data)


# --------------------
# Services
# --------------------

def get(key):
    return load().get(key)


def set(key, value):
    if key not in USER_SETTINGS_FIELDS:
        raise ValueError(f"Unknown setting: {key}")

    data = load()
    data[key] = value
    save(data)


def get_all():
    return load()

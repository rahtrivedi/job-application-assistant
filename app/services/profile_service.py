from app.util.paths import profiles_path
from app.util.file import load_json, save_json
from .profile_validator import validate_profiles
from app.system.constants import PROFILE_FIELDS


# --------------------
# Storage
# --------------------

def load():
    return load_json(profiles_path()) or {}


def save(data):
    validate_profiles(data)
    save_json(profiles_path(), data)


# --------------------
# CRUD
# --------------------

def add_profile(profile_id):
    data = load()

    if profile_id in data:
        raise ValueError("Profile already exists")

    data[profile_id] = {}
    save(data)


def add_language(profile_id, lang, name=""):
    data = load()

    if profile_id not in data:
        raise ValueError("Profile not found")

    if lang in data[profile_id]:
        raise ValueError("Language already exists")

    data[profile_id][lang] = {
        "name": name,
        "Exprience": "",
        "Motivation": ""
    }

    save(data)


def set_field(profile_id, lang, field, value):
    if field not in PROFILE_FIELDS:
        raise ValueError("Invalid field")

    data = load()

    if profile_id not in data:
        raise ValueError("Profile not found")

    if lang not in data[profile_id]:
        raise ValueError("Language not found")

    data[profile_id][lang][field] = value
    save(data)


def get_profile(profile_id, lang):
    data = load()

    if profile_id not in data:
        raise ValueError("Profile not found")

    if lang not in data[profile_id]:
        raise ValueError("Language not found")

    return data[profile_id][lang]


def delete_profile(profile_id):
    data = load()

    if profile_id not in data:
        raise ValueError("Profile not found")

    del data[profile_id]
    save(data)
def get_profile_text(profile_id, lang):
    profile = get_profile(profile_id, lang)

    return {
        "name": profile.get("name", ""),
        "experience": profile.get("Exprience", ""),
        "motivation": profile.get("Motivation", "")
    }
# Backward-compatibility for tests & external callers
def set_text(profile_id, lang, field, value):
    return set_field(profile_id, lang, field, value)

def get_profile(profile_id, lang=None):
    data = load()

    if profile_id not in data:
        raise ValueError("Profile not found")

    if lang:
        if lang not in data[profile_id]:
            raise ValueError(f"Profile '{profile_id}' has no language '{lang}'")
        return data[profile_id][lang]

    return data[profile_id]

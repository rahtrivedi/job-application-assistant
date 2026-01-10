import os
from pathlib import Path


# --------------------------------------------------
# Root handling (allows pytest sandboxing)
# --------------------------------------------------

def root() -> Path:
    """
    Returns the base folder for all app data.

    In production:
        APP_ROOT is not set → uses project root.

    In pytest:
        APP_ROOT is set → uses a temp folder.
    """
    return Path(os.environ.get("APP_ROOT", "."))


# --------------------------------------------------
# System paths
# --------------------------------------------------

def system_root() -> Path:
    path = root() / "app" / "system"
    path.mkdir(parents=True, exist_ok=True)
    return path


def users_path() -> Path:
    path = system_root() / "users.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def system_settings_path() -> Path:
    path = system_root() / "system_settings.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def languages_path() -> Path:
    path = system_root() / "languages.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


# --------------------------------------------------
# User paths
# --------------------------------------------------

def user_root() -> Path:
    path = root() / "app" / "user"
    path.mkdir(parents=True, exist_ok=True)
    return path


def _active_user_root() -> Path:
    from app.system.system_service import get_active_user

    uid = get_active_user()
    if not uid:
        raise RuntimeError("No active user")

    path = user_root() / uid
    path.mkdir(parents=True, exist_ok=True)
    return path


def profiles_path() -> Path:
    path = _active_user_root() / "profiles.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def settings_path() -> Path:
    path = _active_user_root() / "settings.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def applications_root() -> Path:
    path = _active_user_root() / "applications"
    path.mkdir(parents=True, exist_ok=True)
    return path

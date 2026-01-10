import json
from pathlib import Path
import pytest

from app.system.system_service import (
    add_user,
    remove_user,
    list_users,
    get_active_user,
    set_active_user
)

USERS_FILE = Path("app/system/users.json")
SYSTEM_SETTINGS = Path("app/system/system_settings.json")


@pytest.fixture(autouse=True)
def clean_system():
    # Backup existing files
    users_backup = USERS_FILE.read_text() if USERS_FILE.exists() else None
    settings_backup = SYSTEM_SETTINGS.read_text() if SYSTEM_SETTINGS.exists() else None

    # Start clean
    USERS_FILE.parent.mkdir(parents=True, exist_ok=True)
    USERS_FILE.write_text("{}")
    SYSTEM_SETTINGS.write_text(json.dumps({"userID": None}))

    yield

    # Restore after tests
    if users_backup is not None:
        USERS_FILE.write_text(users_backup)
    else:
        USERS_FILE.unlink(missing_ok=True)

    if settings_backup is not None:
        SYSTEM_SETTINGS.write_text(settings_backup)
    else:
        SYSTEM_SETTINGS.unlink(missing_ok=True)


def test_add_user_and_list():
    add_user("user_001")
    add_user("user_002")

    users = list_users()
    assert "user_001" in users
    assert "user_002" in users


def test_add_user_sets_first_active():
    add_user("user_001")
    assert get_active_user() == "user_001"


def test_set_active_user():
    add_user("user_001")
    add_user("user_002")

    set_active_user("user_002")
    assert get_active_user() == "user_002"


def test_set_invalid_user():
    with pytest.raises(ValueError):
        set_active_user("ghost")


def test_remove_user():
    add_user("user_001")
    add_user("user_002")

    remove_user("user_001")
    users = list_users()

    assert "user_001" not in users
    assert "user_002" in users


def test_removing_active_user_unsets_it():
    add_user("user_001")
    remove_user("user_001")
    assert get_active_user() is None

import os
import pytest
from app.system.system_service import add_user, set_active_user

@pytest.fixture(autouse=True)
def setup_user(tmp_path):
    os.environ["APP_ROOT"] = str(tmp_path)
    add_user("user_001")
    set_active_user("user_001")
    yield
    os.environ.pop("APP_ROOT", None)

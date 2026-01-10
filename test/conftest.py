import os
import shutil
import pytest
from pathlib import Path

import app.util.paths as paths

TEST_ROOT = Path("test_runtime")


@pytest.fixture(autouse=True)
def isolate_fs():
    # Use a separate folder for all file I/O during tests
    os.environ["APP_ROOT"] = str(TEST_ROOT)

    if TEST_ROOT.exists():
        shutil.rmtree(TEST_ROOT)

    TEST_ROOT.mkdir(parents=True)

    yield

    shutil.rmtree(TEST_ROOT)




@pytest.fixture(autouse=True)
def isolated_fs(tmp_path):
    paths.ROOT = tmp_path / "app"
    yield

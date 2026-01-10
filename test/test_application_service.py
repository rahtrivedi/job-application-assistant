import json
from pathlib import Path
import pytest

from app.services.application_service import generate
from app.system.system_service import add_user, set_active_user, list_users, remove_user
from app.services.settings_service import set
from app.services.profile_service import add_profile, add_language, set_text
from app.system.language_service import add_language_pack


@pytest.fixture(autouse=True)
def setup():
    if "user_001" in list_users():
        remove_user("user_001")

    add_user("user_001")
    set_active_user("user_001")

    set("first name", "Rahul kumar")
    set("last name", "Trivedi")

    add_profile("cad")
    add_language("cad", "en")
    set_text("cad", "en", "Exprience", "10 years CAD")
    set_text("cad", "en", "Motivation", "I love engineering")

    add_language_pack("en", {
        "attributes": {
            "salutation": {"none": "Dear Sir or Madam"},
            "application_sentence": {
                "before": "I saw {wensite} for {job_title}",
                "after": ""
            },
            "signature_head": "Best regards"
        }
    })


def test_generate_application():
    data = {
        "company": {
            "company_name": "Siemens AG",
            "company_address": "Munich",
            "wensite": "linkedin",
            "job_title": "CAD engineer"
        },
        "meta": {
            "language": "en",
            "profile_id": "cad",
            "date": "2026-01-10"
        }
    }

    path = generate(data)

    assert path.exists()
    text = path.read_text()

    assert "Siemens AG" in text
    assert "Dear Sir or Madam" in text
    assert "10 years CAD" in text
    assert "Rahul Kumar" in text

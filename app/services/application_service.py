import json
from pathlib import Path
from datetime import date

from app.system.system_service import get_active_user
from app.services.settings_service import get_all as get_settings
from app.services.profile_service import get_profile
from app.system.language_service import get_language
from app.services.profile_service import get_profile_text
from app.services.scrape_service import scrape_linkedin


TEMPLATE = """{{company_name}}
{{company_address}}

{{salutation}}

{{application_sentence}}

{{experience}}

{{motivation}}

{{signature_head}}
{{user_name}}
"""


def _safe(text):
    return "".join(c for c in text if c.isalnum() or c in " _-").strip().replace(" ", "_")


def generate(application_data: dict) -> Path:
    user = get_active_user()
    if not user:
        raise ValueError("No active user")

    settings = get_settings()
    lang = application_data["meta"]["language"]
    profile_id = application_data["meta"]["profile_id"]

    profile_lang = get_profile(profile_id, lang)
    language_pack = get_language(lang)


    company = application_data["company"]

    # Build values
    user_name = f"{settings['first name']} {settings['last name']}".strip()

    salutation = language_pack["attributes"]["salutation"]["none"]

    app_sentence = language_pack["attributes"]["application_sentence"]["before"] \
        .replace("{website}", company.get("website", "")) \
        .replace("{job_title}", company.get("job_title", ""))

    values = {
        "company_name": company["company_name"],
        "company_address": company["company_address"],
        "salutation": salutation,
        "application_sentence": app_sentence,
        "experience": profile_lang.get("Exprience", ""),
        "motivation": profile_lang.get("Motivation", ""),
        "signature_head": language_pack["attributes"]["signature_head"],
        "user_name": user_name
    }

    text = TEMPLATE
    for k, v in values.items():
        text = text.replace(f"{{{{{k}}}}}", v)

    # Save
    folder = Path(f"app/user/{user}/applications")
    folder.mkdir(parents=True, exist_ok=True)

    filename = f"{date.today()}_{_safe(company['company_name'])}_{_safe(company['job_title'])}.txt"
    path = folder / filename
    path.write_text(text, encoding="utf-8")

    return path

def generate_from_url(url: str, profile_id: str, language: str):
    job = scrape_linkedin(url)

    data = {
        "company": job,
        "meta": {
            "profile_id": profile_id,
            "language": language,
            "date": str(date.today())
        }
    }

    return generate(data)

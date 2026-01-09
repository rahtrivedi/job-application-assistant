import json
from pathlib import Path

LANGUAGE_DIR = Path("src/languages")


def load_language(code: str) -> dict:
    path = LANGUAGE_DIR / f"{code.lower()}.json"
    if not path.exists():
        raise ValueError(f"Language not found: {code}")

    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except UnicodeDecodeError:
        raise ValueError(
            f"Language file {path} must be UTF-8 encoded"
        )



def build_salutation(lang: dict, gender: str, last_name: str = "") -> str:
    template = lang["salutation"].get(gender, lang["salutation"]["none"])
    return template.replace("{{last_name}}", last_name or "")


def build_title_sentence(
    lang: dict,
    job_title: str,
    variant: str = "formal"
) -> str:
    app_block = lang.get("application_sentence", {})

    if variant not in app_block:
        raise ValueError(f"Unknown application sentence variant: {variant}")

    before = app_block[variant].get("before", "")
    after = app_block[variant].get("after", "")

    sentence = f"{before} {job_title}"
    if after:
        sentence += f" {after}"

    return sentence.strip()

def list_languages() -> list[dict]:
    """
    Returns metadata of all available languages
    """
    languages = []

    for file in LANGUAGE_DIR.glob("*.json"):
        try:
            data = json.loads(file.read_text(encoding="utf-8-sig"))
            languages.append({
                "code": data.get("code"),
                "name": data.get("name"),
                "file": file
            })
        except Exception:
            continue

    return languages
# src/core/language.py
from pathlib import Path

TEMPLATE_DIR = Path(__file__).parents[1] / "generators" / "templates"

def load_template(language_code: str) -> str:
    template_path = TEMPLATE_DIR / f"{language_code.lower()}.md"

    if not template_path.exists():
        raise ValueError(f"Language template not found: {language_code}")

    return template_path.read_text(encoding="utf-8")

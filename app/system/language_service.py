from app.util.paths import languages_path
from app.util.file import load_json, save_json


def load():
    return load_json(languages_path()) or {}


def save(data):
    save_json(languages_path(), data)


def get_language(lang_code):
    data = load()

    if lang_code not in data:
        raise ValueError(f"Language not found: {lang_code}")

    return data[lang_code]


def add_language_pack(lang_code, lang_data):
    data = load()

    data[lang_code] = lang_data
    save(data)

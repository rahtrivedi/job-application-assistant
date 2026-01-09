from src.core.language_loader import (
    load_language,
    build_salutation,
    build_title_sentence
)

def test_load_language_en():
    lang = load_language("EN")
    assert lang["code"] == "EN"
    assert "salutation" in lang


def test_build_salutation_male():
    lang = load_language("EN")
    result = build_salutation(lang, "male", "Smith")
    assert result == "Dear Mr Smith,"


def test_build_salutation_none():
    lang = load_language("EN")
    result = build_salutation(lang, "none", "")
    assert result == "Dear Sir or Madam,"


def test_build_title_sentence():
    lang = load_language("EN")
    sentence = build_title_sentence(lang, "CAD Engineer")
    assert sentence == "Application for the position of CAD Engineer"

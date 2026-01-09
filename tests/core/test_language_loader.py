from src.core.language_loader import load_language, build_salutation, build_title_sentence

def test_load_language():
    lang = load_language("EN")
    assert lang["code"] == "EN"
    assert "salutation" in lang
    print (lang)
    lang = load_language("DE")
    assert lang["code"] == "DE"
    assert "salutation" in lang
    print (lang)

def test_salutation_male():
    lang = load_language("EN")
    result = build_salutation(lang, "male", "Smith")
    assert "Smith" in result
    assert result.startswith("Dear")


def test_salutation_none():
    lang = load_language("EN")
    result = build_salutation(lang, "none", "")
    assert result == lang["salutation"]["none"]


def test_title_sentence():
    lang = load_language("EN")
    sentence = build_title_sentence(lang, "CAD Engineer")
    assert "CAD Engineer" in sentence

def test_title_sentence_email_variant():
    lang = load_language("EN")
    sentence = build_title_sentence(lang, "CAD Engineer", variant="email")
    assert sentence.startswith("Regarding")

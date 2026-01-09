def test_generate_cover_letter_basic():
    lang = {
        "salutation": {
            "male": "Dear Mr {{last_name}},",
            "none": "Dear Sir or Madam,"
        },
        "application_sentence": {
            "formal": {
                "before": "Application for the position of",
                "after": ""
            }
        },
        "closing": "Kind regards"
    }


    job_data = {
        "job_title": "CAD Engineer",
        "contact": {
            "gender": "male",
            "last_name": "Smith"
        }
    }

    profile = {
        "paras": [
            "I have 10 years of CAD experience.",
            "I enjoy automation and BIM."
        ],
        "signature": "Rahul Kumar Trivedi\n+0000000000"
    }

    from src.generators.cover_letter import generate_cover_letter
    letter = generate_cover_letter(lang, profile, job_data)

    assert "Dear Mr Smith" in letter
    assert "CAD Engineer" in letter
    assert "10 years of CAD experience" in letter
    print ("\n",letter)

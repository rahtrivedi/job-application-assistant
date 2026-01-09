from pathlib import Path
from src.generators.template_renderer import render_template


def test_render_template(tmp_path):
    template = tmp_path / "template.md"
    template.write_text(
        "{{salutation}}\n\n{{title_sentence}}\n\n{{closing}}\n\n{{signature}}",
        encoding="utf-8"
    )

    context = {
        "salutation": "Dear Mr Smith,",
        "title_sentence": "Application for the position of CAD Engineer",
        "closing": "Kind regards",
        "signature": "Rahul Kumar Trivedi"
    }

    result = render_template(template, context)

    assert "Dear Mr Smith" in result
    assert "CAD Engineer" in result
    assert "Kind regards" in result
    print (result)

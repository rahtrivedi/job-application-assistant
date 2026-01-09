def test_render_template_basic(tmp_path):
    template_file = tmp_path / "template.md"
    template_file.write_text(
        "{{salutation}}\n\n{{title_sentence}}\n\n{{closing}}",
        encoding="utf-8"
    )

    context = {
        "salutation": "Dear Mr Smith,",
        "title_sentence": "Application for CAD Engineer",
        "closing": "Kind regards"
    }

    from src.generators.template_renderer import render_template
    result = render_template(template_file, context)

    assert "Dear Mr Smith," in result
    assert "CAD Engineer" in result
    assert "Kind regards" in result

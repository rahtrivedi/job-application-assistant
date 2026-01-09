from src.core.parser import parse_job_title, parse_company_name

def test_parse_job_title():
    html = """
    <html>
        <div id="job-title">CAD Engineer</div>
    </html>
    """

    title = parse_job_title(html)

    assert title == "CAD Engineer"


def test_parse_company_name():
    html = """
    <html>
        <div class="company">ACME GmbH</div>
    </html>
    """

    company = parse_company_name(html)

    assert company == "ACME GmbH"


def test_parse_missing_elements():
    html = "<html></html>"

    assert parse_job_title(html) is None
    assert parse_company_name(html) is None

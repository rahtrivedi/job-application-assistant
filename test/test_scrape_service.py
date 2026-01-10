from app.scrape.scrape_service import scrape_from_file

def test_linkedin():
    data = scrape_from_file("app/scrape/pages/linkedin.html")
    assert data["company_name"]
    assert data["job_title"]

import requests
from bs4 import BeautifulSoup


def scrape_linkedin(url: str) -> dict:
    """
    Extract job data from a LinkedIn job posting
    Returns normalized fields for the application engine
    """
    html = requests.get(url).text
    return scrape_linkedin_html(html, url)


def scrape_linkedin_html(html: str, url: str = "") -> dict:
    """
    Pure parser (this is what we test)
    """
    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("h1")
    company = soup.find("a", {"class": "topcard__org-name-link"})
    location = soup.find("span", {"class": "topcard__flavor--bullet"})

    return {
        "company_name": company.text.strip() if company else "",
        "company_address": location.text.strip() if location else "",
        "job_title": title.text.strip() if title else "",
        "website": "linkedin",
        "source_url": url,
    }

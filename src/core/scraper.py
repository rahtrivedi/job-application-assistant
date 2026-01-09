import requests
from src.core.parser import parse_job_title, parse_company_name

def scrape_job(url: str) -> dict:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    html = response.text

    return {
        "job_title": parse_job_title(html),
        "company": parse_company_name(html),
    }

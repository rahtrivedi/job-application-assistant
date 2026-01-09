from bs4 import BeautifulSoup

def parse_job_title(html: str) -> str | None:
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find("div", id="job-title")
    return title.get_text(strip=True) if title else None


def parse_company_name(html: str) -> str | None:
    soup = BeautifulSoup(html, "html.parser")
    company = soup.find("div", class_="company")
    return company.get_text(strip=True) if company else None

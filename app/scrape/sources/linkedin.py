def match(url: str) -> bool:
    return "linkedin.com" in url


def extract(soup) -> dict:
    return {
        "company_name": soup.select_one(".topcard__org-name-link").text.strip(),
        "job_title": soup.select_one("h1").text.strip(),
        "company_address": soup.select_one(".topcard__flavor--bullet").text.strip(),
        "website": "linkedin"
    }

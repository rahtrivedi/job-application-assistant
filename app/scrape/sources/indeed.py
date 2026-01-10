def match(url):
    return "indeed." in url

def extract(soup):
    return {
        "company_name": soup.select_one(".jobsearch-CompanyInfoContainer").text.strip(),
        "job_title": soup.select_one("h1").text.strip(),
        "company_address": soup.select_one(".jobsearch-JobInfoHeader-subtitle").text.strip(),
        "website": "indeed"
    }

def match(url):
    return "glassdoor." in url

def extract(soup):
    return {
        "company_name": soup.select_one("[data-test='employerName']").text.strip(),
        "job_title": soup.select_one("[data-test='jobTitle']").text.strip(),
        "company_address": soup.select_one("[data-test='location']").text.strip(),
        "website": "glassdoor"
    }

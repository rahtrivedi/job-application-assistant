import requests
from pathlib import Path

def save(url, filename):
    html = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0"
    }).text

    Path("app/scrape/pages").mkdir(parents=True, exist_ok=True)
    Path(f"app/scrape/pages/{filename}").write_text(html, encoding="utf-8")

    print("Saved", filename)


# Example:
# save("https://www.linkedin.com/jobs/view/...", "linkedin.html")

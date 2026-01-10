from pathlib import Path

from app.scrape.sources.linkedin import scrape as scrape_linkedin
from app.scrape.sources.indeed import scrape as scrape_indeed
from app.scrape.sources.glassdoor import scrape as scrape_glassdoor


SOURCES = {
    "linkedin": scrape_linkedin,
    "indeed": scrape_indeed,
    "glassdoor": scrape_glassdoor,
}


def scrape_from_file(source: str, path: Path) -> dict:
    html = path.read_text(encoding="utf-8")

    if source not in SOURCES:
        raise ValueError(f"Unknown source: {source}")

    return SOURCES[source](html)

from src.core.language_loader import build_salutation, build_title_sentence

def generate_cover_letter(lang: dict, profile: dict, job_data: dict) -> str:
    salutation = build_salutation(
        lang,
        job_data["contact"]["gender"],
        job_data["contact"]["last_name"]
    )

    title_sentence = build_title_sentence(
        lang,
        job_data["job_title"],
        variant="formal"   
    )

    paras = "\n\n".join(profile.get("paras", []))
    closing = lang["closing"]
    signature = profile["signature"]

    return (
        f"{salutation}\n\n"
        f"{title_sentence}\n\n"
        f"{paras}\n\n"
        f"{closing}\n\n"
        f"{signature}"
    )

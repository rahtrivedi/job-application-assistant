from pathlib import Path


def render_template(template_path: Path, context: dict) -> str:
    """
    Render a template by replacing {{placeholders}} with values from context.
    """
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")

    content = template_path.read_text(encoding="utf-8")

    for key, value in context.items():
        placeholder = "{{" + key + "}}"
        content = content.replace(placeholder, value or "")

    # Clean up excessive blank lines
    return normalize_spacing(content)


def normalize_spacing(text: str) -> str:
    """
    Normalize spacing between paragraphs.
    """
    lines = [line.rstrip() for line in text.splitlines()]
    result = []

    for line in lines:
        if line or (result and result[-1]):
            result.append(line)

    return "\n".join(result).strip()

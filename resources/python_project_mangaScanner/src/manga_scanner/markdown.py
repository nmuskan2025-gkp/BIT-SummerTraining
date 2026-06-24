# """Markdown rendering for scanner results."""

# from __future__ import annotations

# from manga_scanner.models import MangaScan


# def render_markdown(scan: MangaScan) -> str:
#     """Render a deterministic Markdown report.

#     Expected format:
#     - ``# <title>``
#     - Source metadata bullets
#     - One ``## Page N`` section per page
#     - Dimensions, OCR text, and warnings
#     - Escape Markdown-sensitive text where needed

#     TODO: Implement Markdown rendering.
#     """

#     raise NotImplementedError("TODO: implement render_markdown")

"""Markdown rendering for scanner results."""

from __future__ import annotations

from manga_scanner.models import MangaScan


def escape_markdown(text: str) -> str:
    chars = "\\*_[]#-.`"

    for ch in chars:
        text = text.replace(ch, "\\" + ch)

    return text


def render_markdown(scan: MangaScan) -> str:
    lines = []

    lines.append(f"# {escape_markdown(scan.title)}")
    lines.append("")

    lines.append(
    f"- Source: `{scan.source_path.as_posix()}`"
    )
    lines.append(f"- Type: {scan.source_type}")
    lines.append(f"- Pages: {len(scan.pages)}")
    lines.append("")

    for page in scan.pages:
        lines.append(f"## Page {page.page_number}")
        lines.append("")

        lines.append(f"- Source page: `{page.source_name}`")
        lines.append(
            f"- Dimensions: {page.width} x {page.height}"
        )
        lines.append("")

        lines.append("### OCR Text")
        lines.append("")

        if page.text_blocks:
            for idx, text in enumerate(page.text_blocks, start=1):
                lines.append(
                    f"{idx}. {escape_markdown(text)}"
                )
        else:
            lines.append("_No text detected._")

        lines.append("")

        if page.warnings:
            lines.append("### Warnings")
            lines.append("")

            for warning in page.warnings:
                lines.append(
                    f"- {escape_markdown(warning)}"
                )

            lines.append("")

    return "\n".join(lines).rstrip() + "\n"

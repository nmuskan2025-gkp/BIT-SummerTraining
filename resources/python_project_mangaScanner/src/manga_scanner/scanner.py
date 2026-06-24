# """High-level scan orchestration."""

from __future__ import annotations

from pathlib import Path

from manga_scanner.loaders import load_pages
from manga_scanner.models import MangaScan, OcrEngine, PageScan
from manga_scanner.ocr import NullOcrEngine


def scan_source(path: str | Path, ocr_engine: OcrEngine | None = None) -> MangaScan:
    path = Path(path)

    pages = load_pages(path)

    if ocr_engine is None:
        ocr_engine = NullOcrEngine()

    scanned_pages = []

    for page in pages:
        raw_blocks = ocr_engine.recognize(page)

        text_blocks = tuple(
            block.strip()
            for block in raw_blocks
            if block.strip()
        )

        warnings = []

        if not text_blocks:
            warnings.append("No OCR text detected.")

        if page.height >= 500:
            warnings.append("Long vertical manhwa-style page.")

        scanned_pages.append(
            PageScan(
                page_number=page.page_number,
                source_name=page.source_name,
                width=page.width,
                height=page.height,
                text_blocks=text_blocks,
                warnings=tuple(warnings),
            )
        )

    if path.is_dir():
        source_type = "folder"
    elif path.suffix.lower() == ".pdf":
        source_type = "pdf"
    elif path.suffix.lower() in {".cbz", ".zip"}:
        source_type = "archive"
    else:
        source_type = "image"

    return MangaScan(
        title=path.stem if path.is_file() else path.name,
        source_path=path,
        source_type=source_type,
        pages=tuple(scanned_pages),
    )
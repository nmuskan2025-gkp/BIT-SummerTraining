"""Load manga/manhwa pages from folders, CBZ/ZIP archives, and PDFs."""


from __future__ import annotations

from io import BytesIO
from pathlib import Path
from zipfile import ZipFile, BadZipFile

import fitz
from PIL import Image

from manga_scanner.errors import (
    CorruptSourceError,
    EmptySourceError,
    SourceNotFoundError,
    UnsupportedSourceError,
)
from manga_scanner.models import PageInput
from manga_scanner.sorting import natural_sort_key
  
SUPPORTED_IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
SUPPORTED_ARCHIVE_EXTENSIONS = {".cbz", ".zip"}
def load_pages(path: str | Path) -> list[PageInput]:
    path = Path(path)

    if not path.exists():
        raise SourceNotFoundError(str(path))

    pages: list[PageInput] = []

    # -------------------------
    # Folder
    # -------------------------
    if path.is_dir():
        image_files = [
            p
            for p in path.iterdir()
            if p.is_file()
            and p.suffix.lower() in SUPPORTED_IMAGE_EXTENSIONS
        ]

        image_files.sort(key=lambda p: natural_sort_key(p.name))

        if not image_files:
            raise EmptySourceError(str(path))

        for idx, image_file in enumerate(image_files, start=1):
            try:
                image = Image.open(image_file).convert("RGB")
            except Exception as exc:
                raise CorruptSourceError(str(image_file)) from exc

            pages.append(
                PageInput(
                    page_number=idx,
                    source_name=image_file.name,
                    image=image,
                    width=image.width,
                    height=image.height,
                )
            )

        return pages

    # -------------------------
    # Single Image
    # -------------------------
    if path.suffix.lower() in SUPPORTED_IMAGE_EXTENSIONS:
        try:
            image = Image.open(path).convert("RGB")
        except Exception as exc:
            raise CorruptSourceError(str(path)) from exc

        return [
            PageInput(
                page_number=1,
                source_name=path.name,
                image=image,
                width=image.width,
                height=image.height,
            )
        ]

    # -------------------------
    # Archive
    # -------------------------
    if path.suffix.lower() in SUPPORTED_ARCHIVE_EXTENSIONS:
        try:
            with ZipFile(path) as zf:
                names = [
                    n
                    for n in zf.namelist()
                    if not n.endswith("/")
                    and Path(n).suffix.lower() in SUPPORTED_IMAGE_EXTENSIONS
                ]

                names.sort(
                 key=lambda name: natural_sort_key(Path(name).name)
                           )

                if not names:
                    raise EmptySourceError(str(path))

                for idx, name in enumerate(names, start=1):
                    try:
                        data = zf.read(name)
                        image = Image.open(BytesIO(data)).convert("RGB")
                    except Exception as exc:
                        raise CorruptSourceError(name) from exc

                    pages.append(
                        PageInput(
                            page_number=idx,
                            source_name=name,
                            image=image,
                            width=image.width,
                            height=image.height,
                        )
                    )

                return pages

        except EmptySourceError:
            raise
        except BadZipFile as exc:
            raise CorruptSourceError(str(path)) from exc
    # -------------------------
    # PDF
    # -------------------------
    if path.suffix.lower() == ".pdf":
        try:
            document = fitz.open(path)

            for idx in range(len(document)):
                page = document[idx]

                pix = page.get_pixmap()
                image = Image.open(
                    BytesIO(pix.tobytes("png"))
                ).convert("RGB")

                pages.append(
                    PageInput(
                        page_number=idx + 1,
                        source_name=f"page-{idx + 1}",
                        image=image,
                        width=image.width,
                        height=image.height,
                    )
                )

            if not pages:
                raise EmptySourceError(str(path))

            return pages

        except Exception as exc:
            raise CorruptSourceError(str(path)) from exc

    raise UnsupportedSourceError(str(path))

# def load_pages(path: str | Path) -> list[PageInput]:
#     """Load pages from an image folder, CBZ/ZIP archive, or PDF.

#     Expected behavior:
#     - Raise ``SourceNotFoundError`` when the path does not exist.
#     - Raise ``UnsupportedSourceError`` for unsupported paths.
#     - Raise ``EmptySourceError`` when no readable pages are found.
#     - Return pages sorted by natural page order.

#     TODO: Implement folder, archive, and PDF loading.
#     """

#     raise NotImplementedError("TODO: implement load_pages")

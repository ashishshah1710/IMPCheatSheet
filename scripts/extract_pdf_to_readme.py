"""Extract image-based PDF content via OCR and write README.md per folder."""

from __future__ import annotations

import io
import re
import sys
from pathlib import Path

import fitz
import pytesseract
from PIL import Image

TESSERACT = Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe")
NOTES_ROOT = Path(__file__).resolve().parents[1] / "Notes"
ZOOM = 2


def clean_text(text: str) -> str:
    text = text.replace("\x0c", "")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def ocr_pdf(pdf_path: Path) -> str:
    pytesseract.pytesseract.tesseract_cmd = str(TESSERACT)
    doc = fitz.open(pdf_path)
    sections: list[str] = []

    for index in range(doc.page_count):
        page = doc[index]
        pixmap = page.get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM))
        image = Image.open(io.BytesIO(pixmap.tobytes("png")))
        page_text = pytesseract.image_to_string(image)
        page_text = clean_text(page_text)
        if page_text:
            sections.append(f"## Page {index + 1}\n\n{page_text}")
        print(f"  OCR page {index + 1}/{doc.page_count}", flush=True)

    doc.close()
    return "\n\n---\n\n".join(sections)


def write_readme(folder: Path, pdf_path: Path, body: str) -> None:
    title = pdf_path.stem.replace("_", " ").replace("-", " ").strip()
    readme = (
        f"# {title}\n\n"
        f"Source: [{pdf_path.name}](./{pdf_path.name})\n\n"
        f"> Text extracted via OCR from the PDF. Minor recognition errors may exist.\n\n"
        f"{body}\n"
    )
    (folder / "README.md").write_text(readme, encoding="utf-8")


def main() -> int:
    if not TESSERACT.exists():
        print(f"Tesseract not found at {TESSERACT}", file=sys.stderr)
        return 1

    pdf_folders: list[tuple[Path, Path]] = []
    for pdf in sorted(NOTES_ROOT.rglob("*.pdf")):
        pdf_folders.append((pdf.parent, pdf))

    if not pdf_folders:
        print("No PDF files found under Notes/")
        return 0

    for folder, pdf in pdf_folders:
        print(f"Processing {pdf}", flush=True)
        body = ocr_pdf(pdf)
        write_readme(folder, pdf, body)
        print(f"Wrote {folder / 'README.md'}", flush=True)

    index_lines = [
        "# Notes",
        "",
        "Study notes extracted from PDF sources in this folder.",
        "",
        "## Folders",
        "",
    ]
    for subfolder in sorted(p for p in NOTES_ROOT.iterdir() if p.is_dir()):
        readme = subfolder / "README.md"
        if readme.exists():
            index_lines.append(f"- [{subfolder.name}](./{subfolder.name}/README.md)")

    (NOTES_ROOT / "README.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    print(f"Wrote {NOTES_ROOT / 'README.md'}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

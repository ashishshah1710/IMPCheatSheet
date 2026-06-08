"""Extract image-based PDF content via OCR and write cleaned README.md files."""

from __future__ import annotations

import io
import re
import sys
from pathlib import Path

import fitz
import pytesseract
from PIL import Image, ImageEnhance, ImageOps

TESSERACT = Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe")
NOTES_ROOT = Path(__file__).resolve().parents[1] / "Notes"
ZOOM = 3
TESSERACT_CONFIG = "--oem 3 --psm 6"

PAGE_TOPICS: dict[str, dict[int, str | None]] = {
    "JAVADSAFullNotes.pdf": {
        1: None,
        2: None,
        3: "Introduction to DSA",
        4: "Time and Space Complexity",
        5: "Arrays",
        6: "Strings",
        7: "Recursion",
        8: "Sorting",
        9: "Searching",
        10: "Hashing",
        11: "Bit Manipulation",
        12: "Sliding Window Technique",
        13: "Two Pointers Technique",
        14: "Prefix Sum",
        15: "Stack",
        16: "Queue",
        17: "Linked List",
        18: "Trees",
        19: "Binary Search Tree (BST)",
        20: "Heap and Priority Queue",
        21: "Graphs",
        22: "Greedy Algorithms",
        23: "Dynamic Programming",
        24: "Backtracking",
        25: "Interview Patterns and Tricks",
        26: "Frequently Asked DSA Questions",
        27: "Tips and Conclusion",
    },
    "JAVAFullNOTES.pdf": {
        1: None,
        2: None,
        3: "Introduction to Java",
        4: "Introduction to Java",
        5: "Java Basics and Variables",
        6: "Operators",
        7: "Control Statements",
        8: "OOPs in Java",
        9: "Classes and Objects",
        10: "Inheritance",
        11: "Polymorphism",
        12: "Polymorphism",
        13: "Abstraction",
        14: "Encapsulation",
        15: "Constructors",
        16: "This Keyword",
        17: "Static Keyword",
        18: "Exception Handling",
        19: "String Handling",
        20: "Collections Framework",
        21: "Collections Framework",
        22: "Multithreading",
        23: "File Handling",
        24: "Java 8+ Features",
        25: "Interview Questions",
        26: "Frequently Asked Questions (FAQ)",
        27: "Practice Questions",
        28: "Programs and Practice",
        29: "Tips and Best Practices",
    },
}

OCR_FIXES: tuple[tuple[str, str], ...] = (
    ("Siabletels", "Statements"),
    ("Ob pjects", "Objects"),
    ("Chasis", "Classes"),
    ("Jawa", "Java"),
    ("S ring", "String"),
    ("REFIX SUM", "PREFIX SUM"),
    ("bosed", "based"),
    ("Greph", "Graph"),
    ("Streom", "Stream"),
    ("intl]", "int[]"),
    ("String{]", "String[]"),
    ("instanceocf", "instanceof"),
    ("COM PLEXITY", "COMPLEXITY"),
    ("Programmi", "Programming"),
    ("Programmingngng", "Programming"),
    ("{] args", "[] args"),
    ("Siabletels", "Statements"),
)

CODE_PATTERN = re.compile(
    r"(^\s*//)|"
    r"(\b(public|class|void|int|long|double|float|boolean|char|String|return|new|import|package|extends|implements)\b)|"
    r"(\b(if|for|while|switch|try|catch|finally|throw)\s*\()|"
    r"(\bSystem\.(out|in)\.)|"
    r"([a-zA-Z_][\w]*\s*[=({].*;)|"
    r"(^\s*[{}]\s*$)"
)


def preprocess_image(image: Image.Image) -> Image.Image:
    gray = ImageOps.grayscale(image)
    return ImageEnhance.Contrast(gray).enhance(1.8)


def apply_fixes(text: str) -> str:
    for old, new in OCR_FIXES:
        text = text.replace(old, new)
    return text


def letter_ratio(line: str) -> float:
    if not line:
        return 0.0
    return sum(ch.isalpha() for ch in line) / len(line)


def has_repeated_noise(line: str) -> bool:
    compact = re.sub(r"\s+", "", line)
    if len(compact) < 6:
        return False
    return bool(re.search(r"(.)\1{5,}", compact)) or "eeee" in compact.lower()


def is_garbage_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return True
    if has_repeated_noise(stripped):
        return True
    if len(stripped) <= 3 and not stripped[0].isdigit():
        return True
    if letter_ratio(stripped) < 0.3 and not CODE_PATTERN.search(stripped):
        return True
    if re.fullmatch(r"[\W_\d\s]{1,12}", stripped):
        return True
    if re.fullmatch(r"[@®©¢$%*~=_\-—–|/\\]{1,6}", stripped):
        return True
    return False


def is_code_line(line: str) -> bool:
    stripped = line.strip()
    if is_garbage_line(stripped):
        return False
    if letter_ratio(stripped) < 0.35:
        return False
    return bool(CODE_PATTERN.search(stripped))


def is_heading_line(line: str) -> bool:
    stripped = line.strip()
    if re.match(r"^TOPIC\s*\d+", stripped, re.I):
        return True
    if re.match(r"^\d+\.\s+[A-Z][A-Z\s&/()\-]{4,}", stripped):
        return True
    if re.match(r"^\(\d+\)\s+[A-Z]", stripped):
        return True
    return False


def clean_line(line: str) -> str:
    line = apply_fixes(line)
    line = line.replace("“", '"').replace("”", '"').replace("’", "'").replace("‘", "'")
    line = re.sub(r"\s*\|\s*", " ", line)
    line = re.sub(r"\s{2,}", " ", line)
    line = re.sub(r"^[©®@¢%*~>\-—–]+\s*", "", line)
    line = re.sub(r"\s*[©®@¢%*~>\-—–]+$", "", line)
    line = re.sub(r"\s+[©®@¢%*~>\-—–]+\s+", " ", line)
    return line.strip()


def format_lines(lines: list[str]) -> str:
    output: list[str] = []
    code_buffer: list[str] = []

    def flush_code() -> None:
        if len(code_buffer) >= 1 and any(";" in line or "{" in line or "}" in line for line in code_buffer):
            output.append("```java")
            output.extend(code_buffer)
            output.append("```")
        else:
            output.extend(code_buffer)
        code_buffer.clear()

    for raw in lines:
        line = clean_line(raw)
        if is_garbage_line(line):
            continue

        if is_code_line(line):
            code_buffer.append(line)
            continue

        flush_code()

        if is_heading_line(line):
            heading = re.sub(r"^TOPIC\s*\d+\s*[\{\}]?\s*", "", line, flags=re.I)
            heading = re.sub(r"^\d+\.\s*", "", heading)
            output.append(f"### {heading}")
            continue

        if re.match(r"^[%©®@¢vV✓✔•\-–—]\s+", line):
            bullet = re.sub(r"^[%©®@¢vV✓✔•\-–—]+\s*", "", line)
            if bullet and not is_garbage_line(bullet):
                output.append(f"- {bullet}")
            continue

        if line.endswith(":") and 4 < len(line) < 80 and letter_ratio(line) > 0.5:
            output.append(f"**{line}**")
            continue

        output.append(line)

    flush_code()
    return "\n".join(output)


def clean_page_text(text: str) -> str:
    text = apply_fixes(text.replace("\x0c", ""))
    return format_lines(text.splitlines())


def get_toc_items(pdf_name: str) -> list[str]:
    topic_map = PAGE_TOPICS.get(pdf_name, {})
    items: list[str] = []
    seen: set[str] = set()
    for page in sorted(topic_map):
        topic = topic_map[page]
        if topic and topic not in seen:
            items.append(topic)
            seen.add(topic)
    return items


def ocr_pdf(pdf_path: Path) -> list[tuple[int, str]]:
    pytesseract.pytesseract.tesseract_cmd = str(TESSERACT)
    doc = fitz.open(pdf_path)
    pages: list[tuple[int, str]] = []

    for index in range(doc.page_count):
        page = doc[index]
        pixmap = page.get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM))
        image = preprocess_image(Image.open(io.BytesIO(pixmap.tobytes("png"))))
        raw_text = pytesseract.image_to_string(image, config=TESSERACT_CONFIG)
        cleaned = clean_page_text(raw_text)
        pages.append((index + 1, cleaned))
        print(f"  OCR page {index + 1}/{doc.page_count}", flush=True)

    doc.close()
    return pages


def build_body(pdf_name: str, pages: list[tuple[int, str]]) -> str:
    topic_map = PAGE_TOPICS.get(pdf_name, {})
    sections: list[str] = []
    current_topic: str | None = None
    current_body: list[str] = []

    def flush_section() -> None:
        nonlocal current_topic, current_body
        if current_topic and current_body:
            body = "\n\n".join(part for part in current_body if part.strip())
            if body.strip():
                sections.append(f"## {current_topic}\n\n{body}")
        current_body = []

    for page_num, content in pages:
        topic = topic_map.get(page_num)
        if not topic:
            continue

        if topic != current_topic:
            flush_section()
            current_topic = topic

        if content.strip():
            current_body.append(content)

    flush_section()
    return "\n\n".join(sections)


def write_readme(folder: Path, pdf_path: Path, body: str, toc_items: list[str]) -> None:
    title = pdf_path.stem.replace("Full", " Full ").replace("NOTES", "Notes").replace("_", " ")
    title = re.sub(r"\s+", " ", title).strip()

    toc_block = "## Table of Contents\n\n" + "\n".join(f"- {item}" for item in toc_items) + "\n\n"

    readme = (
        f"# {title}\n\n"
        f"Source: [{pdf_path.name}](./{pdf_path.name})\n\n"
        f"> Study notes extracted from the PDF. Content is organized by topic with OCR cleanup applied.\n\n"
        f"{toc_block}"
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
        pages = ocr_pdf(pdf)
        body = build_body(pdf.name, pages)
        toc_items = get_toc_items(pdf.name)
        write_readme(folder, pdf, body, toc_items)
        print(f"Wrote {folder / 'README.md'}", flush=True)

    index_lines = [
        "# Notes",
        "",
        "Study notes extracted from PDF sources, organized by topic.",
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

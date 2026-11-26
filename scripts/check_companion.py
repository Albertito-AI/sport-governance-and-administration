"""Check the two teaching indexes and the editable files they offer readers."""

import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote
from xml.etree import ElementTree
from zipfile import BadZipFile, ZipFile


ROOT = Path(__file__).resolve().parents[1]
OFFICE_PARTS = {".xlsx": "xl/workbook.xml", ".docx": "word/document.xml"}


def check_index(directory, suffixes):
    index = directory / "README.md"
    files = {p.name for p in directory.iterdir()
             if p.is_file() and p != index and p.suffix in suffixes}
    links = []
    for line in index.read_text(encoding="utf-8").splitlines():
        if line.lstrip().startswith("|"):
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", line):
                links.append(unquote(target.partition("#")[0].strip("<>")))
    duplicates = sorted(name for name, count in Counter(links).items() if count > 1)
    missing = sorted(set(links) - files)
    unlisted = sorted(files - set(links))
    if duplicates or missing or unlisted or not files:
        raise ValueError(f"{index.relative_to(ROOT)}: {len(files)} files, "
                         f"broken links {missing}, unlisted files {unlisted}, duplicates {duplicates}")
    return [directory / name for name in sorted(files)]


def check_office_file(path):
    try:
        with ZipFile(path) as package:
            damaged = package.testzip()
            if damaged:
                raise ValueError(f"damaged ZIP member {damaged}")
            for part in ("[Content_Types].xml", OFFICE_PARTS[path.suffix]):
                ElementTree.fromstring(package.read(part))
    except (BadZipFile, KeyError, ValueError, ElementTree.ParseError) as error:
        raise ValueError(f"{path.name}: {error}") from error


if __name__ == "__main__":
    cases = check_index(ROOT / "cases", {".md"})
    tools = check_index(ROOT / "tools", OFFICE_PARTS)
    for tool in tools:
        check_office_file(tool)
    print(f"Verified {len(cases)} case links and {len(tools)} indexed Office files.")

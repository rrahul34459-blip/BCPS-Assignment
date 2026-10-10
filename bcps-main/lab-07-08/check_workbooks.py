"""Check formula results saved by LibreOffice. Run with Python 3."""
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET

NS = {"table": "urn:oasis:names:tc:opendocument:xmlns:table:1.0",
      "office": "urn:oasis:names:tc:opendocument:xmlns:office:1.0"}
ROOT = Path(__file__).resolve().parent


def cells(path, name):
    with ZipFile(path) as archive:
        doc = ET.fromstring(archive.read("content.xml"))
    table = next(t for t in doc.findall(".//table:table", NS)
                 if t.get(f"{{{NS['table']}}}name") == name)
    row = table.findall("table:table-row", NS)[1]
    result = []
    for cell in row.findall("table:table-cell", NS):
        repeat = int(cell.get(f"{{{NS['table']}}}number-columns-repeated", "1"))
        result.extend([cell] * min(repeat, 20 - len(result)))
        if len(result) >= 20:
            break
    return result


def check(row, column, expected):
    cell = row[column - 1]
    assert cell.get(f"{{{NS['table']}}}formula"), "Missing formula"
    value = float(cell.get(f"{{{NS['office']}}}value"))
    assert abs(value - expected) < 1e-8, (value, expected)


if __name__ == "__main__":
    check(cells(ROOT.parent / "lab-06/student-marksheet.ods", "Marksheet"), 7, 345)
    check(cells(ROOT.parent / "lab-06/student-marksheet.ods", "Marksheet"), 8, 86.25)
    book = ROOT / "attendance-salary-inventory.ods"
    check(cells(book, "Attendance"), 10, 0.8)
    check(cells(book, "Salary"), 11, 30875)
    check(cells(book, "Inventory"), 8, 1600)
    print("All five workbook formula checks passed.")

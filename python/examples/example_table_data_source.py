"""
    Example: use an Excel file as data source
"""
import sys
import pathlib

from yattag import indent

from data_source.table import ExcelTable
from format.bootstrap import BootstrapDoc

doc, tag, text = BootstrapDoc().tagtext()


# --- table source ---

XL = 'excel-table-source.xlsx'
TAB = 'TableData'

table_source = ExcelTable(XL, TAB)

# --- render the document ---

with tag('html'):

    doc.head("Table Source Example")

    with tag('body'):

        doc.table(
            list(map(str, table_source["A1:F1"][0])),
            list(map(lambda r: map(str, r), table_source.iter_rows("A2:F7"))),
            sort_rows=False
        )

# --- produce the document ---

file_path = pathlib.Path(__file__).resolve()
project_home_dir = file_path.resolve().parent.parent.parent
report_dir = project_home_dir / "report"
report_dir.mkdir(parents=True, exist_ok=True)
report_file = report_dir / file_path.with_suffix(".html").name
report_pages = report_dir / f"{file_path.stem}_pages"

report_file.write_text(indent(doc.getvalue()))

print(f"Output in {report_file}")

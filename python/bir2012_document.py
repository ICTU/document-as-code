"""
    example document - demonstrate how 'Document as Code' works
"""
import pathlib

from domain.compliance.model.measure import Measure
from domain.compliance.render.document_renderer import DocumentRenderer
from domain.compliance.render.bootstrap_labeler import BootstrapLabeler

from domain.bir2012 import BIR2012 as BIR


# --- specific measures ---

import bir2012_measures

# --- explained and accepted exceptions ---

Measure(
    identifier="BM Explained",
    description="Geaccepteerde afwijking",
    identifiers=[
    ],
).set_explain()

# --- declared and accepted as not applicable ---

Measure(
    identifier="Not Applicable",
    description="Niet van toepassing",
    identifiers=[
    ],
).set_not_applicable()


# --- PROCESSING STARTS HERE ---

if __name__ == "__main__":

    file_path = pathlib.Path(__file__).resolve()
    project_dir = file_path.resolve().parent.parent
    report_dir = project_dir / "report"
    report_file = report_dir / file_path.with_suffix(".html").name
    report_pages = report_dir / f"{file_path.stem}_pages"

    renderer = DocumentRenderer(BootstrapLabeler)
    renderer.link_measures_to_fragments(BIR)
    renderer.render_main_document_as_one(BIR, report_file)
    renderer.render_main_document_as_parts(BIR, report_pages)

    print(f"Output in '{report_dir}'")

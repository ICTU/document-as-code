"""
    example document - demonstrate how 'Document as Code' works
"""
import pathlib

from domain.compliance.model.measure import Measure
from domain.compliance.render.document_renderer import DocumentRenderer
from domain.compliance.render.bootstrap_labeler import BootstrapLabeler

from domain.bio2019 import BIO2019 as BIO


# --- specific measures ---

import bio2019_measures

# --- explained and accepted exceptions ---

Measure(
    identifier="Explained",
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
    project_home_dir = file_path.resolve().parent.parent.parent
    report_dir = project_home_dir / "report"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_file = report_dir / file_path.with_suffix(".html").name
    report_pages = report_dir / f"{file_path.stem}_pages"

    renderer = DocumentRenderer(BootstrapLabeler)
    renderer.link_measures_to_fragments(BIO)
    renderer.render_main_document_as_one(BIO, report_file)
    renderer.render_main_document_as_parts(BIO, report_pages)

    print(f"Output in '{report_dir}'")

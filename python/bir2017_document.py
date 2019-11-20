"""
    example document - demonstrate how 'Document as Code' works
"""
import pathlib

from domain.compliance.model.measure import Measure
from domain.compliance.render.document_renderer import DocumentRenderer
from domain.compliance.render.bootstrap_labeler import BootstrapLabeler

from domain.bir2017 import BIR2017 as BIR


# --- specific measures ---

import bir2017_measures

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

    file_path = pathlib.Path(__file__)
    report_base_name = file_path.stem
    project_dir = file_path.resolve().parent.parent
    report_dir = project_dir / "report"

    renderer = DocumentRenderer(BootstrapLabeler)
    renderer.link_measures_to_fragments(BIR)
    renderer.render_main_document_as_one(BIR, report_dir / f"{report_base_name}_document.html")
    renderer.render_main_document_as_parts(BIR, report_dir / f"{report_base_name}_pages")

    print(f"Output in '{report_dir}'")

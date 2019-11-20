"""
    example document - demonstrate how 'Document as Code' works
"""
import pathlib

from domain.bio.model.bio_measure import BioMeasure
from domain.bio.render.bio_document_renderer import BioDocumentRenderer
from domain.bio.render.bootstrap_labeler import BootstrapLabeler

from domain.bio2019 import BIO2019 as BIO


# --- specific measures ---

import bio2019_measures

# --- explained and accepted exceptions ---

BioMeasure(
    identifier="BM Explained",
    description="Geaccepteerde afwijking",
    identifiers=[
    ],
).set_explain()

# --- declared and accepted as not applicable ---

BioMeasure(
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

    renderer = BioDocumentRenderer(BootstrapLabeler)
    renderer.link_measures_to_fragments(BIO)
    renderer.render_main_document_as_one(BIO, report_dir / f"{report_base_name}_document.html")
    renderer.render_main_document_as_parts(BIO, report_dir / f"{report_base_name}_pages")

    print(f"Output in '{report_dir}'")

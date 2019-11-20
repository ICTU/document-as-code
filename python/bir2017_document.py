"""
    example document - demonstrate how 'Document as Code' works
"""
import pathlib

from domain.bir.model.bir_measure import BirMeasure
from domain.bir.render.bir_document_renderer import BirDocumentRenderer
from domain.bir.render.bootstrap_labeler import BootstrapLabeler

from domain.bir2017 import BIR2017 as BIR


# --- specific measures ---

BirMeasure(
    identifier="M01",
    description="""
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
""",
    identifiers=[
        "06",
    ],
    url="lorem-impsum",
    done=True,
)

# --- explained and accepted exceptions ---

BirMeasure(
    identifier="BM Explained",
    description="Geaccepteerde afwijking",
    identifiers=[
    ],
).set_explain()

# --- declared and accepted as not applicable ---

import bir2017_measures


# --- PROCESSING STARTS HERE ---

if __name__ == "__main__":

    file_path = pathlib.Path(__file__)
    report_base_name = file_path.stem
    project_dir = file_path.resolve().parent.parent
    report_dir = project_dir / "report"

    renderer = BirDocumentRenderer(BootstrapLabeler)
    renderer.link_measures_to_fragments(BIR)
    renderer.render_main_document_as_one(BIR, report_dir / f"{report_base_name}_document.html")
    renderer.render_main_document_as_parts(BIR, report_dir / f"{report_base_name}_pages")

    print(f"Output in '{report_dir}'")

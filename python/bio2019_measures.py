"""
    example document - demonstrate how 'Document as Code' works
"""
from domain.compliance.model.measure import Measure

# --- specific measures ---

Measure(
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

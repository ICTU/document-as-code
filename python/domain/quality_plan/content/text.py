"""
    text - text fragments for the document
"""
import datetime

project = "Document-as-code"
title = "{0} example".format(project)
version = "v0.1"
date = datetime.datetime.now().strftime("%d %B %Y")

intro = """
This is an example of a document created to illustrate the document-as-code principle. Instead of writing
structured documents using a text processor or spreadsheet, the document is generated from a simple program consisting
of a domain model, the contents of the domain model, and a document generator.
""".strip()

reading_guide = """
In this example document, we have requirements for a project. The requirements come from sources.
For each requirement, measures have been defined to ensure the requirements are actually achieved by the project.
The measures are captured in deliverables.
""".strip()

intro_sources = """
This section lists the example sources for the requirements of the {0} project.
""".strip().format(project)

intro_requirements = """
This section lists the example requirements applicable to the {0} project.
Each requirement refer back to the source it originates from and refers forward to the measures defined to
implement or support the requirement.
""".strip().format(project)

intro_measures = """
This section contains the example measures defined to implement or support the requirements of the
project.
""".strip()

intro_deliverables = """
This section contains the example deliverables that contain or implement the measures.
""".strip()

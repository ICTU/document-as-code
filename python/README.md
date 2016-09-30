Document-as-code
================

Simple self-contained examples of using document-as-code to generate a 
structured documents based on a document-specific domain model.

These examples needs Python (2.7 or newer) and a couple of libraries, 
which can be installed with: sudo pip install -r REQUIREMENTS.pip.

Document-as-code consists of four components: a domain model, the 
population of the domain model ("contents" in the example), a 
document ("example_document.py") and a way to transform the raw
document to output formats. This example uses yattag to create
a HTML output document.

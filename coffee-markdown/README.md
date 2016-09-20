Document-as-code
================

Simple self-contained example of using document-as-code to generate a
structured document based on a document-specific domain model.

This example is implemented using Markdown with inline coffeescript.
A preprocessor is run to execute the inline coffeescript code. The resulting
document is also a valid Markdown file.

## Install

    npm install -g nodemon coffee-script
    npm install

# Run

Use nodemon to watch changes to the original markdown document and automatically
regenerate the output.

    nodemon --exec "coffee doc-as-code.coffee ./document.md > \
      ./output/document.md" -e "md"

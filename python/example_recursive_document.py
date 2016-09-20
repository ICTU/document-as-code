"""
    example document - demonstrate how 'Document as Code' works
"""

from __future__ import absolute_import
from __future__ import print_function


from yattag import indent

import content
import domain
from format.bootstrap import BootstrapDoc


doc, tag, text = BootstrapDoc().tagtext()

headings = ( doc.h1, doc.h2 )

def show_fragments( headings, *fragments ):
    if headings:
        heading = headings[0]
        remaining_headings = headings[1:]
    else:
        heading = doc.p
        remaining_headings = []
    for fragment in fragments:
        heading( fragment.get_title() )
        if fragment.text:
            doc.p( fragment.text )
        show_fragments( remaining_headings, *(fragment.fragments) )


fragments = ( content.F1, content.F2 )

for nr, fragment in enumerate( fragments, 1 ):
    fragment.renumber( nr, start=1 )


with tag('html'):

    doc.head(content.title)

    with tag('body'):

        with tag('div', klass='container'):

            doc.h1(content.title, content.version + ', ' + content.date)
            doc.p(content.intro, klass='lead')
            doc.p(content.reading_guide)

            doc.h2('Fragments', doc.badge(domain.RecursiveFragment.all))

            show_fragments( headings, content.F1, content.F2 )

file('example_recursive_document.html', 'w').write(indent(doc.getvalue()))

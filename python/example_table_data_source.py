'''
    Example: use an Excel file as data source
'''
from __future__ import absolute_import
from __future__ import print_function

from yattag import indent

from data_source.table import ExcelTable
from format.bootstrap import BootstrapDoc

doc, tag, text = BootstrapDoc().tagtext()


# --- table source ---

XL  = 'excel-table-source.xlsx'
TAB = 'TableData'

table_source = ExcelTable( XL, TAB )

# --- render the document ---

with tag('html'):

    doc.head( "Table Source Example" )

    with tag('body'):

        doc.table(
            map( str, table_source["A1:F1"][0] ),
            map( lambda r: map( str, r ), table_source.iter_rows("A2:F7") ),
            sort_rows=False
        )

# --- produce the document ---

with open('example_table_data_source.html', 'w') as fout:
    fout.write( indent(doc.getvalue() ).encode('ascii',errors='xmlcharrefreplace') )


if __name__ == '__main__':
    pass

'''
    moduledocs
'''
from __future__ import absolute_import
from __future__ import print_function


import domain.iso25010.content.iso25010_en
from domain.iso25010.model import Iso25010MainCharacteristic


if __name__ == '__main__':
    name_width   = max( len(s.name) for m in Iso25010MainCharacteristic.all for s in m._sub_characteristics )
    sub_template = " * {{n:{w}}} - {{d}}".format(w=name_width)

    for m in sorted( Iso25010MainCharacteristic.all, key=lambda x: x.identifier ):
        print( m.name )
        print( '-'*len(m.name) )
        print( m.description )
        for s in m._sub_characteristics:
            print( sub_template.format( n=s.name, d=s.description ) )
        print( '' )

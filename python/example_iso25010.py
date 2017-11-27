"""
    produce the ISO 25010
"""
from __future__ import absolute_import
from __future__ import print_function


from domain.iso25010 import model as iso

# importing defines the content - no need to explicitly reference it further
import domain.iso25010.content.iso25010_en


if __name__ == '__main__':
    name_width = max(len(s.name) for m in iso.Iso25010MainCharacteristic.all for s in m.all_sub_characteristics())
    sub_template = " * {{n:{w}}} - {{d}}".format(w=name_width)

    for m in sorted(iso.Iso25010MainCharacteristic.all, key=lambda x: x.identifier):
        print(m.name)
        print('-'*len(m.name))
        print(m.description)
        for s in m.all_sub_characteristics():
            print(sub_template.format(n=s.name, d=s.description))
        print('')

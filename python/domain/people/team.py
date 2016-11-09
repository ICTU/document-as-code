'''
    team - describe a team
'''
from __future__ import absolute_import
from __future__ import print_function


from domain.base import Base


class Team( Base ):
    '''
    team
    '''


    def __init__( self, name, *persons ):
        '''
        Constructor
        '''
        self.name    = name
        self.persons = [ p for p in persons ]


    def add_person( self, person ):
        self.persons.append( person )


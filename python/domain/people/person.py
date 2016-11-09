'''
    person - describe a person
'''
from __future__ import absolute_import
from __future__ import print_function


from domain.base import Base


class Person( Base ):
    '''
    person
    '''


    def __init__( self, given_name, surname, email=None ):
        '''
        Constructor
        '''
        self.given_name = given_name
        self.surname    = surname
        self.email      = email


    @property
    def name(self):
        return "{} {}".format( self.given_name, self.surname )

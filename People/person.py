''' Python class to represent a person '''

import datetime
from traits import Sex

class Person:
    def __init__(self):
        self.name = ""
        self.dob:datetime.date = None       #Date of Birth
        self.dod:datetime.date = None       #Date of Death
        is_alive = False
        self.sex = Sex()
        # human traits

        
        
        def toggle_life(self):
            if is_alive:
                is_alive = False
            elif not is_alive:
                is_alive = True





    ''' Properties '''
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, newname):
        self._name = newname
        
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, newage):
        self._age = newage

    @property
    def sex(self):
        return self._sex
    @sex.setter
    def sex(self, newsex):
        self._sex = newsex

    @property
    def dob(self):
        return self._dob
    @dob.setter
    def dob(self, newdob):
        self._dob = newdob

    @property
    def dod(self):
        return self._dod
    @dod.setter
    def dod(self, newdod):
        self._dod = newdod

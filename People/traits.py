'''person traits'''

import os

class Sex:
    def __init__(self, sex):
        self.sex = sex
        if str.lower(sex) == "male":
            self.sex = "Male"
        if str.lower(sex) == "female":
            self.sex = "Female"
        else:
            self.sex = "Unknown"

    
    @property
    def can_have_children(self):
        if self.sex == "Female":
            return True
        else:
            return False


    
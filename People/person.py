''' Python class to represent a person '''

import datetime
from traits import Sex

class Person:
  def __init__(self):
    self.name = ""
    self.dob:datetime.date = None
    self.sex = Sex()
    # human traita
    

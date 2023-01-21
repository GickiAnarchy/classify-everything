
from person import Person
import random


# Actions Start

def action_die(person:Person):
    if person.is_alive:
        person.is_alive = False
        return

def action_born(person:Person):
    if not person.is_alive:
        person.is_alive = True
        return

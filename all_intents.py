import random  
from constants import *
def greeting_intent():    
        return random.choice(greeting_response)+random.choice(greeting_predicate)


def goodbye_intent():
    return random.choice(goodbye_response)+random.choice(goodbye_response)

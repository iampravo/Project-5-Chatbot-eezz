from constants import *
import random
from response_generators import return_org_in_text, return_person_in_text

from mapping import *


# %%

def intersect(list1, list2):
    intersect = set(list1).intersection(list2)
    if len(intersect) > 0:
        return True
    else:
        return False


def to_lower(txt):
    return str(txt).lower()


def find_intent(query):
    """
    first check for all other entities. at last check for greetings
    to do: check for words in list also
    """
    global greetings_key_word

    wordlist = list(map(to_lower, query.split(" ")))

    esg_words = ['esg', 'e s g', 'e.s.g.', 'esgrating', 'esg rating', 'esg ratings', 'esgratings']
    if intersect(wordlist, esg_words):
        company_name = return_org_in_text(query)
        if company_name is not None:
            return 'esg_with_company'
        # else:
        #     return 'esg_with_no_company'

    cap_words = ['cap', 'capital', 'market capital']
    if intersect(wordlist, cap_words):
        company_name = return_org_in_text(query)
        if company_name is not None:
            return 'market_cap_with_company'

    person_name = return_person_in_text(query)
    if person_name is not None:
        return 'person_profile_with_name'

    for words in query.split(" "):
        if words.lower() in goodbye_key_word:
            return 'good_bye'

    for words in query.split(" "):
        if words.lower() in greetings_key_word:
            return 'greetings'


def get_response(query):
    intent = find_intent(query)
    try:
        return intent_activity[intent](query)
    except KeyError:
        return random.choice(sorry_response)

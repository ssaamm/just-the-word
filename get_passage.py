import sqlite3
import itertools
import requests
from datetime import date

NUM_DAYS_IN_PLAN = 720

class BibleService(object):
    def __init__(self):
        self.API_BASE_URL = 'http://www.esvapi.org/v2/rest/passageQuery'

    def get_passage_text(self, reference):
        payload = {
            'key': 'IP',
            'passage' : reference,
            'include-headings': 'false',
            'output-format': 'plain-text',
            'include-passage-references': 'false',
            'include-first-verse-numbers': 'false',
            'include-verse-numbers' : 'false',
            'include-footnotes': 'false',
            'include-passage-horizontal-lines': 'false',
            'include-heading-horizontal-lines': 'false',
            'line-length': '0'
        }
        r = requests.get(self.API_BASE_URL, params = payload)
        return r.text

bible_service = BibleService()

def get_day_number():
    initial_date = date(2014, 11, 25)
    delta = date.today() - initial_date
    return delta.days % NUM_DAYS_IN_PLAN

def get_references(day_num):
    conn = sqlite3.connect('plan.db')
    c = conn.cursor()
    day_num_tuple = (day_num,)
    c.execute('''SELECT passages FROM plan WHERE day_id = ? LIMIT 1;''', day_num_tuple)
    refs = c.fetchone()
    conn.commit()
    conn.close()
    return refs

def get_passage(reference):
    return bible_service.get_passage_text(reference)

def get_passages(day_number):
    days_references = get_references(day_number)
    references = [x.strip() for x in days_references[0].split(";")]
    passages = [get_passage(r) for r in references]
    return itertools.izip(references, passages)

def get_passages_for_today():
    return get_passages(get_day_number())

if __name__ == "__main__":
    passages = get_passages_for_today()
    for ref, pas in passages:
        print ref
        print pas

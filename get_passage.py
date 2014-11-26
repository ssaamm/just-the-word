import sqlite3
import itertools
import BibleService
from models import Passage
from common import DB_NAME
from datetime import date

NUM_DAYS_IN_PLAN = 720
INITIAL_DATE = date(2014, 11, 25)

bible_service = BibleService.BibleService()

def get_day_number():
    delta = date.today() - INITIAL_DATE
    return delta.days % NUM_DAYS_IN_PLAN

def get_references(day_num):
    conn = sqlite3.connect(DB_NAME)
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
    passages = []
    for reference in references:
        passages.append(Passage(reference, get_passage(reference).split('\n')))
    return passages 

def get_passages_for_today():
    return get_passages(get_day_number())

if __name__ == "__main__":
    passages = get_passages_for_today()
    for ref, pas in passages:
        print ref
        print pas

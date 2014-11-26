import requests
import sqlite3
from common import DB_NAME

class BibleService(object):
    def __init__(self):
        self.API_BASE_URL = 'http://www.esvapi.org/v2/rest/passageQuery'

    def get_passage_text(self, reference):
        cached_text = self.get_cached_text(reference)
        if cached_text:
            return cached_text
        passage_text = self.get_api_text(reference)
        self.set_cached_text(reference, passage_text)
        return passage_text

    def set_cached_text(self, reference, passage_text):
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('INSERT INTO passage_text (reference,passage) VALUES (?,?)',
                (reference, passage_text))
        conn.commit()
        conn.close()

    def get_cached_text(self, reference):
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('SELECT passage FROM passage_text WHERE reference = ?',
                (reference,))
        text = c.fetchone()
        conn.close()
        return None if not text else text[0]

    def get_api_text(self, reference):
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

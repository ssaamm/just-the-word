import requests

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

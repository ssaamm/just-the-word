import sys
from HTMLParser import HTMLParser

class PlanHTMLParser(HTMLParser):
    plan = [""]
    current_day = 0

    def handle_data(self, data):
        if "Day" in data:
            self.current_day += 1
        else:
            if len(self.plan) > self.current_day:
                self.plan.append("")
            self.plan[self.current_day] += data

    def get_plan(self):
        return self.plan

parser = PlanHTMLParser()
parser.feed("".join([line for line in sys.stdin]))

plan = parser.get_plan()
for i in plan:
    print i

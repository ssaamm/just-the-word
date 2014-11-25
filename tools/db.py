import sqlite3
import sys

def init_db():
    conn = sqlite3.connect('plan.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE plan (
        day_id INT PRIMARY KEY NOT NULL,
        passages TEXT NOT NULL
    );''')
    conn.commit()
    conn.close()

def dump_plan():
    conn = sqlite3.connect('plan.db')
    c = conn.cursor()
    c.execute('SELECT * FROM plan')
    for r in c:
        print r
    conn.commit()
    conn.close()

def init_plan():
    conn = sqlite3.connect('plan.db')
    c = conn.cursor()
    passages = [(idx,val) for idx, val in enumerate(sys.stdin)]
    print passages
    c.executemany('INSERT INTO plan (day_id,passages) VALUES (?,?)', passages)
    for r in c:
        print r
    conn.commit()
    conn.close()

if __name__ == "__main__":
    dump_plan()

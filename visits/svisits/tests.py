from django.test import TestCase

import sqlite3

conn = sqlite3.connect(r'C:\Users\kerg6\PycharmProjects\Kursovaya\visits\db.sqlite3')
cur = conn.cursor()


cur.execute("""SELECT * FROM students""")
#cur.execute("""SELECT * FROM visits""")
print(cur.fetchall())
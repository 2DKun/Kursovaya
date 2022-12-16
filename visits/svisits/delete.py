import sqlite3

conn = sqlite3.connect(r'C:\Users\kerg6\PycharmProjects\Kursov\Rursovaya\visits\db.sqlite3')
cur = conn.cursor()

cur.execute('DELETE FROM students WHERE student_id ==  ?', ('921',))

conn.commit()
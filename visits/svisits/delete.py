import sqlite3

conn = sqlite3.connect(r'E:\Kursov\Rursovaya\visits\db.sqlite3')
cur = conn.cursor()

cur.execute('DELETE FROM students WHERE student_id ==  ?', ('921',))

conn.commit()
import sqlite3

conn = sqlite3.connect(r'E:\Kursov\Rursovaya\visits\db.sqlite3')
cur = conn.cursor()

cur.execute('UPDATE students SET sgroup == ? WHERE student_id ==  ?', ('INBO-08-20', '921'))

conn.commit()
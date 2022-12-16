import sqlite3

conn = sqlite3.connect(r'C:\Users\kerg6\PycharmProjects\Kursovaya\visits\db.sqlite3')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS students 
    (student_id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    patronymic TEXT,
    sgroup TEXT NOT NULL,
    gender TEXT NOT NULL);""")

conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS visits
    (atten_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    visitdate TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    way CHAR(3) NOT NULL,
    student_id INTEGER NOT NULL, 
    FOREIGN KEY (student_id) REFERENCES students(student_id));""")
conn.commit()






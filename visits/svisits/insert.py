import sqlite3


import cursor as cursor

conn = sqlite3.connect(r'C:\Users\kerg6\PycharmProjects\Kursovaya\visits\db.sqlite3')
cur = conn.cursor()

cur.execute("INSERT INTO students(student_id, name, surname, patronymic, sgroup, gender) VALUES(00921, 'Van', 'Tyomniy', 'Holmovich', 'INBO-01-20', 'male')")
cur.execute("INSERT INTO students(student_id,name,surname, patronymic, sgroup, gender) VALUES(00201, 'Dany', 'Li', 'Каzyevich', 'INBO-08-20', 'female')")
cur.execute("INSERT INTO students(student_id, name, surname, patronymic, sgroup, gender) VALUES(00127, 'Mark', 'Volkov', 'Gymovich', 'IKBO-33-20', 'male')")
cur.execute("INSERT INTO students(student_id,name,surname, patronymic, sgroup, gender) VALUES(00333, 'Billy', 'Herrington', 'NULL', 'IKBO-01-20', 'male')")

cur.execute("INSERT INTO visits(student_id, way) VALUES('00921', 'in')")
cur.execute("INSERT INTO visits(student_id, way) VALUES('00921', 'out')")
cur.execute("INSERT INTO visits(student_id, way) VALUES('00921', 'in')")
cur.execute("INSERT INTO visits(student_id, way) VALUES('00921', 'out')")
cur.execute("INSERT INTO visits(student_id, way) VALUES('00201', 'in')")
cur.execute("INSERT INTO visits(student_id, way) VALUES('00201', 'out')")
cur.execute("INSERT INTO visits(student_id, way) VALUES('00201', 'in')")
cur.execute("INSERT INTO visits(student_id, way) VALUES('00201', 'out')")
cur.execute("INSERT INTO visits(student_id, way) VALUES('00201', 'in')")

cur.execute("INSERT INTO visits(student_id, way) VALUES('00333', 'in')")
cur.execute("INSERT INTO visits(student_id, way) VALUES('00333', 'out')")
cur.execute("INSERT INTO visits(student_id, way) VALUES('00333', 'in')")
cur.execute("INSERT INTO visits(student_id, way) VALUES('00333', 'out')")
cur.execute("INSERT INTO visits(student_id, way) VALUES('00127', 'in')")
cur.execute("INSERT INTO visits(student_id, way) VALUES('00127', 'out')")
cur.execute("INSERT INTO visits(student_id, way) VALUES('00127', 'in')")
cur.execute("INSERT INTO visits(student_id, way) VALUES('00127', 'out')")
cur.execute("INSERT INTO visits(student_id, way) VALUES('00127', 'in')")

conn.commit()




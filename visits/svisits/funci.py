import sqlite3


def out(req):
    conn = sqlite3.connect(r'E:\Kursov\Rursovaya\visits\db.sqlite3')
    cur = conn.cursor()
    cur.execute(f"{req}")
    resp = cur.fetchall()
    return resp

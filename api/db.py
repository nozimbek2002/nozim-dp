import sqlite3 as sql

con = sql.connect('words.sqlite')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS words')
sql = '''CREATE TABLE "words" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "uzbek" TEXT,
    "english" TEXT,
    "russian" TEXT,
    "description" TEXT)'''
cur.execute(sql)

con.commit()
con.close()
import sqlite3 as sql

def k(w,g,l,d):
    con = sql.connect('words.sqlite')
    cur = con.cursor()
    cur.execute('insert into words(word,grammar,lexical,description) values (?,?,?,?)', (w,g,l,d))
    con.commit()
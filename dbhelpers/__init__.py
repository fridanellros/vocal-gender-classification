import sqlite3

def select(sql, db):
    db.execute(sql)
    return db.fetchall()

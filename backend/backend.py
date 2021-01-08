# backend file 
import sqlite3


def db_connect():

    # database will be tailored to profile in future
    conn = sqlite3.connect("budget.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS budget (id INTEGER PRIMARY KEY, name text, date text, projected integer, actual integer, inout integer)")
    conn.commit()
    conn.close()


db_connect()

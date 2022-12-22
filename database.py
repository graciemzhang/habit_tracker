import sqlite3
from datetime import datetime, date


conn = sqlite3.connect('database.db')
cur = conn.cursor()

def create_habits():
    cur.execute("CREATE TABLE IF NOT EXISTS habits(habit TEXT)")

def create_notifs():
    cur.execute("CREATE TABLE IF NOT EXISTS notif(id INTEGER)")

def create_date():
    cur.execute("CREATE TABLE IF NOT EXISTS date(id INTEGER, date_started)")

def create_restart():
    cur.execute("CREATE TABLE IF NOT EXISTS restart(id INTEGER, total INTEGER)")
    cur.execute("INSERT INTO restart VALUES(:id, :total)", {'id': 1, 'total': 0})

def create_table():
    create_habits()
    create_notifs()
    create_date()
    create_restart()

def insert_habits(habits):
    cur.executemany("INSERT INTO habits VALUES(?)", habits)
    conn.commit()

def insert_notif(notify):
    cur.execute("INSERT INTO notif VALUES(:id)", {'id': notify})
    conn.commit()

def insert_date(date):
    cur.execute("INSERT INTO date VALUES(:id, :date_started)", {'id': 1, 'date_started': date})
    conn.commit()

def get_habits():
    res = cur.execute("SELECT habit FROM habits")
    habits = [x[0] for x in res]
    return habits

def get_date():
    res = cur.execute("SELECT date_started FROM date")
    date = res.fetchone()[0]
    return datetime.strptime(date, '%Y-%m-%d').date()

def get_restart():
    res = cur.execute("SELECT total FROM restart")
    return res.fetchone()[0]

def get_notif():
    res = cur.execute("SELECT id FROM notif")
    notif = res.fetchone()[0]
    return res

def update_date(date):
    #delete current date
    cur.execute("UPDATE date SET date_started = :date WHERE id = 1", {"date": date})
    conn.commit()

def update_restart():
    next_restart = get_restart() + 1
    cur.execute("UPDATE restart SET total = :next_start WHERE id = 1", {"next_start": next_restart})
    conn.commit()

    return get_restart()

def verify_table():
    res = cur.execute("SELECT name FROM sqlite_schema WHERE type='table'")
    return res.fetchall()



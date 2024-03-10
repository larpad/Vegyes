import sqlite3 as lite
def version():
    conn = lite.connect(r'F:\Database\Orarend\Orarend.db')
    cur = conn.cursor()
    cur.execute("SELECT SQLITE_VERSION()")
    version = cur.fetchall()[0]
    print(f"SQL Lite verzió : {version}")

def select(p_text_sql):
    conn = lite.connect(r'F:\Database\Orarend\Orarend.db')
    cur = conn.cursor()

    cur.execute(p_text_sql)
    return cur.fetchall()

def iskola_osztaly_select():
    return select("SELECT * from ISKOLA_OSZTALY")

def iskola_osztaly_select_id(PID):
    return select("select * from ISKOLA_OSZTALY t where t.ID = {0}".format(PID))[0]
    # return select("select * from ISKOLA_OSZTALY t where t.ID = {0}".format(PID))[0][1]

import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("web_data.db")

    def start(self):
        print('DB')

    def insert_fajl(self,file_name, blob):
        sql = "insert into FILES (FILENAME,BLOB) values (?,?)"
        cur = self.conn.cursor()
        cur.execute(sql, [file_name, sqlite3.Binary(blob)])
        self.conn.commit()

    def delete_file(self, PID,):
        sql = "delete from files where ID = ?"
        cur = self.conn.cursor()
        cur.execute(sql, PID)
        self.conn.commit()

    def select_fajl(self, PID):
        sql = "select ID,FILENAME,BLOB from files where ID = ?"

        cur = self.conn.cursor()

        for sor in cur.execute(sql, PID):
            tetel = sor

#        print(tetel)
        return tetel[0], tetel[1], tetel[2]

    def select_fajl_list(self):
        cur = self.conn.cursor()
        list_files = []
        for sor in cur.execute("select ID,FILENAME from files"):
            list_files.append(sor)
        cur.close()
        return list_files

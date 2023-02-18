import sqlite3

class DatabaseFiles():
    def __init__(self):
        self.dbnames = sqlite3.connect("Db1")
        self.curser = self.dbnames.cursor()
        self.curser.execute('''CREATE TABLE IF NOT EXISTS Database_Namesdb(Database_Files Text)''')

    def InsertDatabaseName(self,data):
        data1 = (data,)
        self.curser.execute("INSERT INTO Database_Namesdb(Database_Files) VALUES(?)",data1)
        self.dbnames.commit()


    def ReaddatabaseNames(self):
        retrieveddata = []
        self.curser.execute('''SELECT * FROM Database_Namesdb''')
        for record in self.curser:
            retrieveddata.append(record)
        return retrieveddata
    def __del__(self):
        self.dbnames.close()
if __name__=="__main__":
    obj = DatabaseFiles()

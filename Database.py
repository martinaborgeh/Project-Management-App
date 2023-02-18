import sqlite3
import pickle

class Sqldatabase:
    def __init__(self,dbname1):
        self.db = sqlite3.connect(dbname1)
        self.curser = self.db.cursor()
        self.curser.execute('''CREATE TABLE IF NOT EXISTS addAllproject(id integer primary key autoincrement,ProjectName Text,DateGiven Text, DateCompleted Text, Status Text)''')
        self.curser.execute('''CREATE TABLE IF NOT EXISTS addWeeklyProject(id integer primary key autoincrement,Day Text,Project1 Text, Project2 Text, Project3 Text,ProjTask1 Text,ProjTask2 Text,ProjTask3 Text)''')
        self.curser.execute('''CREATE TABLE IF NOT EXISTS addweeklycompleted(id integer primary key autoincrement,Day Text,ProjectName Text, TaskCompleted Text, DateCompleted Text)''')

    def AllPojectExist(self, data):
        for name in (data):
            self.curser.execute("SELECT count(*) FROM addAllproject WHERE ProjectName =?", (name,))
            data = self.curser.fetchone()[0]
            if data == 0:
                return True
            else:
                return False

    def weeklyPojectExist(self, data):
        for name in (data):
            self.curser.execute("SELECT rowid FROM addWeeklyProject WHERE Day =?", (name,))
            data = self.curser.fetchone()
            if data is None:
                return True
            else:
                return False

    def weeklycompletedPojectExist(self, data):
        for name in (data):
            self.curser.execute("SELECT rowid FROM addweeklycompleted WHERE Day =?", (name,))
            data = self.curser.fetchone()
            if data is None:
                return True
            else:
                return False

    def InsertWeeklyProjectData(self,data):
        checkweeklyexist = self.weeklyPojectExist(data)
        if checkweeklyexist:
            data1,data2,data3,data4,data5,data6,data7 = data
            self.curser.execute("INSERT INTO addWeeklyProject(Day,Project1,Project2,Project3,ProjTask1,ProjTask2,ProjTask3) VALUES(?,?,?,?,?,?,?)", (data1,data2,data3,data4,data5,data6,data7))#i will add data for weekly
            self.db.commit()

    def InsertWeeklyCompletedData(self,data):
        weeklycomplete = self.weeklycompletedPojectExist(data)
        if weeklycomplete:
            data1,data2,data3,data4 = data
            self.curser.execute("INSERT INTO addweeklycompleted(Day,ProjectName,TaskCompleted,DateCompleted) VALUES(?,?,?,?)", (data1,data2,data3,data4))
            self.db.commit()

    def InsertAllProjectData(self,data):
        checkExistance = self.AllPojectExist(data)
        if checkExistance:
            data1,data2,data3,data4 = data
            self.curser.execute("INSERT INTO addAllproject(ProjectName,DateGiven,DateCompleted,Status) VALUES(?,?,?,?)" , (data1,data2,data3,data4))
            self.db.commit()

    def DeleteWeeklyProjectData(self,data):
        self.curser.execute('DELETE FROM addWeeklyProject WHERE id=?', (data,))
        self.db.commit()

    def DeleteWeeklyCompletedData(self,data):
        self.curser.execute('DELETE FROM addweeklycompleted WHERE id=?', (data,))
        self.db.commit()

    def DeleteAllProjectData(self,data):
        self.curser.execute('DELETE FROM addAllproject WHERE id=?', (data,))
        self.db.commit()

    def UpdateWeeklyProjectData(self,id,column,data):
        if column ==1:
            self.curser.execute("Update addWeeklyProject set Day = ? Where id =?",(data,id))
            self.db.commit()
        elif column ==2:
            self.curser.execute("Update addWeeklyProject set Project1 = ? Where id =?",(data,id))
            self.db.commit()
        elif column ==3:
            self.curser.execute("Update addWeeklyProject set Project2 = ? Where id =?",(data,id))
            self.db.commit()
        elif column ==4:
            self.curser.execute("Update addWeeklyProject set Project3 = ? Where id =?",(data,id))
            self.db.commit()
        elif column ==5:
            self.curser.execute("Update addWeeklyProject set ProjTask1 = ? Where id =?",(data,id))
            self.db.commit()
        elif column ==6:
            self.curser.execute("Update addWeeklyProject set ProjTask2 = ? Where id =?",(data,id))
            self.db.commit()
        elif column ==7:
            self.curser.execute("Update addWeeklyProject set ProjTask3 = ? Where id =?",(data,id))
            self.db.commit()

    def UpdateWeeklyCompletedData(self,id,column,data):
        if column ==1:
            self.curser.execute("Update addweeklycompleted set Day = ? Where id =?",(data,id))
            self.db.commit()
        elif column ==2:
            self.curser.execute("Update addweeklycompleted set ProjectName = ? Where id =?",(data,id))
            self.db.commit()
        elif column ==3:
            self.curser.execute("Update addweeklycompleted set TaskCompleted = ? Where id =?",(data,id))
            self.db.commit()
        elif column ==4:
            self.curser.execute("Update addweeklycompleted set DateCompleted = ? Where id =?",(data,id))
            self.db.commit()

    def UpdateAllProjectData(self,id,column,data):
        if column ==1:
            self.curser.execute("Update addAllproject set ProjectName = ? Where id =?",(data,id))
            self.db.commit()

        elif column ==2:
            self.curser.execute("Update addAllproject set DateGiven = ? Where id =?", (data, id))
            self.db.commit()

        elif column ==3:
            self.curser.execute("Update addAllproject set DateCompleted = ? Where id =?", (data, id))
            self.db.commit()

        elif column ==4:
            self.curser.execute("Update addAllproject set Status = ? Where id =?", (data, id))
            self.db.commit()

    def ReadWeeklyProjectData(self):
        retrieveddata = []
        self.curser.execute('''SELECT * FROM addWeeklyProject''')
        for record in self.curser:
            retrieveddata.append(record)
        return retrieveddata

    def ReadWeeklyweeklyCompletedData(self):
        retrieveddata = []
        self.curser.execute('''SELECT * FROM addweeklycompleted''')
        for record in self.curser:
            retrieveddata.append(record)
        return retrieveddata

    def ReadAllProjectData(self):
        retrieveddata = []
        self.curser.execute('''SELECT * FROM addAllproject''')
        for record in self.curser:
            retrieveddata.append(record)
        return retrieveddata

    def __del__(self):
        self.db.close()

#
#
if __name__=='__main__':
    with open('trial.pickle', 'rb') as output:
        dataitem = pickle.load(output)
    sql_object=Sqldatabase(dataitem)



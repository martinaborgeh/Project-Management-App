from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QWidget
import sys
import pickle
from Database import Sqldatabase
class AddProject(QWidget):
    def __init__(self):
        super(AddProject,self).__init__()
        uic.loadUi(r"C:\Users\Martin Aborgeh\Desktop\Final_Year_Project_Manage_App\Add_Project.ui",self)
        self.weeklyprojectuis=uic.loadUi(r"C:\Users\Martin Aborgeh\Desktop\Final_Year_Project_Manage_App\Weekly_Project.ui")
        self.weeklycompleteduis=uic.loadUi(r"C:\Users\Martin Aborgeh\Desktop\Final_Year_Project_Manage_App\weeklyCompleted.ui")
        self.Addtotable.clicked.connect(self.AddtoAllProjectDatabase)
        self.weeklyprojectuis.Addtoweeklytable.clicked.connect(self.AddtoWeeklyProjectDatabase)
        self.weeklycompleteduis.AddtoWeeklyCompleted.clicked.connect(self.addtoweeklycompletedDatabase)
        self.cancel.clicked.connect(self.CancelAllProject)
        self.weeklyprojectuis.cancelweekly.clicked.connect(self.CancelweeklyProject)
        self.weeklycompleteduis.CancelweeklyCompleted.clicked.connect(self.Cancelweeklycompleted)

    def AddtoAllProjectDatabase(self):
        with open('trial.pickle','rb') as output:
            dataitem =pickle.load(output)

        project_name = self.ProjectName.text()
        date_given = self.dateGiven.text()
        date_to_completed = self.DateCompleted.text()
        status = self.Status.text()
        storedata = Sqldatabase(dataitem)
        storedata.InsertAllProjectData([project_name,date_given,date_to_completed,status])
        self.ProjectName.clear()
        self.dateGiven.clear()
        self.DateCompleted.clear()
        self.Status.clear()

    def AddtoWeeklyProjectDatabase(self):
        with open('trial2.pickle','rb') as output:
            dataitem =pickle.load(output)

        Date = self.weeklyprojectuis.Day.text()
        Project1= self.weeklyprojectuis.Project1.text()
        Project2 = self.weeklyprojectuis.Project2.text()
        Project3 = self.weeklyprojectuis.Project3.text()
        Projtask1 = self.weeklyprojectuis.ProjectTask1.text()
        projtask2 = self.weeklyprojectuis.Projecttask2.text()
        projtask3 = self.weeklyprojectuis.ProjectTask3.text()
        storedata = Sqldatabase(dataitem)
        storedata.InsertWeeklyProjectData([Date,Project1,Project2,Project3,Projtask1,projtask2,projtask3])
        self.weeklyprojectuis.Day.clear()
        self.weeklyprojectuis.Project1.clear()
        self.weeklyprojectuis.Project2.clear()
        self.weeklyprojectuis.Project3.clear()
        self.weeklyprojectuis.ProjectTask1.clear()
        self.weeklyprojectuis.Projecttask2.clear()
        self.weeklyprojectuis.ProjectTask3.clear()

    def addtoweeklycompletedDatabase(self):
        with open('trial3.pickle','rb') as output:
            dataitem =pickle.load(output)
        Day = self.weeklycompleteduis.Day.text()
        ProjectName = self.weeklycompleteduis.ProjectName.text()
        TaskCompleted = self.weeklycompleteduis.TaskCompleted.text()
        DateCompleted = self.weeklycompleteduis.DateCompleted.text()
        storedata = Sqldatabase(dataitem)
        storedata.InsertWeeklyCompletedData([Day, ProjectName, TaskCompleted, DateCompleted])
        self.weeklycompleteduis.Day.clear()
        self.weeklycompleteduis.TaskCompleted.clear()
        self.weeklycompleteduis.ProjectName.clear()
        self.weeklycompleteduis.DateCompleted.clear()
    def CancelAllProject(self):
        self.close()

    def CancelweeklyProject(self):
        self.weeklyprojectuis.close()

    def Cancelweeklycompleted(self):
        self.weeklycompleteduis.close()

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = AddProject()
    app.exec_()

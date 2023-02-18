from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QHeaderView,QMainWindow,QApplication
import pickle
import sys
from DatabaseNamesDatabase import DatabaseFiles
from AddDatabasename import addDatabasename
from Add_Project import AddProject
from Database import Sqldatabase

class ManageUI(QMainWindow):
    def __init__(self):
        super(ManageUI,self).__init__()
        uic.loadUi(r"C:\Users\Martin Aborgeh\Desktop\Final_Year_Project_Manage_App\Project_Management_UI.ui",self)
        stylesheet = "::section{Background-color:rgb(73, 79, 85);color:rgb(0,0,0);font-size:14px;font-weight:bold;border-radius:14px;}"
        self.AllProjectstable.horizontalHeader().setStyleSheet(stylesheet)
        self.WeeklyProjectstable.horizontalHeader().setStyleSheet(stylesheet)
        self.WeeklyProjectCompletedtable.horizontalHeader().setStyleSheet(stylesheet)
        self.verticalGroupBox.setStyleSheet("QGroupBox {border:3px solid rgb(73,80,85);}")
        self.databasescombobobox.addItems([data[0] for data in DatabaseFiles().ReaddatabaseNames()])
        choosedb = f'{self.databasescombobobox.currentText()}.db'
        with open('trial.pickle','wb') as input:
            pickle.dump(choosedb,input)
        with open('trial2.pickle','wb') as input1:
            pickle.dump(choosedb,input1)
        with open('trial3.pickle','wb') as input2:
            pickle.dump(choosedb,input2)
        self.AllProjectstable.horizontalHeader().setStretchLastSection(True)
        self.AllProjectstable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.WeeklyProjectstable.horizontalHeader().setStretchLastSection(True)
        self.WeeklyProjectstable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.WeeklyProjectCompletedtable.horizontalHeader().setStretchLastSection(True)
        self.WeeklyProjectCompletedtable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.AddTOAllProjects.clicked.connect(self.AddtoAllProject)
        self.AddtoWeeklyProject.clicked.connect(self.addtoWeeklyProject)
        self.AddtoWeeklycompleted.clicked.connect(self.addweeklycompleted)
        self.refreshprojecttable.clicked.connect(self.refreshProjectTable)
        self.RefreshWeekly.clicked.connect(self.WeeklyReffresh)
        self.RefreshWeeklyCompleted.clicked.connect(self.WeeklyRefreshCompleted)
        self.Refreshdbcombo.clicked.connect(self.RefreshDatabaseCombo)
        self.Openaddnewdbui.clicked.connect(self.openaddnewdb)
        self.Delete.clicked.connect(self.AllprojectItemDelete)
        self.Update.clicked.connect(self.UpdateTable)
        self.show()

    def openaddnewdb(self):
        self.newdb = addDatabasename()
        self.newdb.show()

    def RefreshDatabaseCombo(self):
        self.databasescombobobox.clear()
        self.databasescombobobox.addItems([data[0] for data in DatabaseFiles().ReaddatabaseNames()])

    def AllprojectItemDelete(self):
        fromsql = Sqldatabase(f'{self.databasescombobobox.currentText()}.db')
        checkallble = self.AllProjectstable.selectedItems()
        checkweekly = self.WeeklyProjectstable.selectedItems()
        checkweeklycomp = self.WeeklyProjectCompletedtable.selectedItems()
        if checkallble:
            for ix in self.AllProjectstable.selectedItems():
                rowid=ix.row()
                tablevalue = self.AllProjectstable.item(rowid,0).text()
                fromsql.DeleteAllProjectData(int(tablevalue))
                self.refreshProjectTable()
        elif checkweekly:
                for check2 in self.WeeklyProjectstable.selectedItems():
                    rowitem = check2.row()
                    tableitem = self.WeeklyProjectstable.item(rowitem,0).text()
                    fromsql.DeleteWeeklyProjectData(int(tableitem))
                    self.WeeklyReffresh()
        elif checkweeklycomp:
            for check3 in self.WeeklyProjectCompletedtable.selectedItems():
                rowitem1 = check3.row()
                tableitem1 = self.WeeklyProjectCompletedtable.item(rowitem1,0).text()
                fromsql.DeleteWeeklyCompletedData(int(tableitem1))
                self.WeeklyRefreshCompleted()

    def UpdateTable(self):
        fromsql = Sqldatabase(f'{self.databasescombobobox.currentText()}.db')
        checkallble = self.AllProjectstable.selectedItems()
        checkweekly = self.WeeklyProjectstable.selectedItems()
        checkweeklycomp = self.WeeklyProjectCompletedtable.selectedItems()
        if checkallble:
            for ix in self.AllProjectstable.selectedItems():
                rowid = ix.row()
                column = ix.column()
                tablevalue = self.AllProjectstable.item(rowid, 0).text()
                tablevalueitem = self.AllProjectstable.item(rowid, column).text()
                fromsql.UpdateAllProjectData(int(tablevalue),column,tablevalueitem)
                self.refreshProjectTable()
        elif checkweekly:
            for check2 in self.WeeklyProjectstable.selectedItems():
                rowitem = check2.row()
                column2 = check2.column()
                tableitem = self.WeeklyProjectstable.item(rowitem, 0).text()
                tableitemvalueitem1 = self.WeeklyProjectstable.item(rowitem, column2).text()
                fromsql.UpdateWeeklyProjectData(int(tableitem),column2,tableitemvalueitem1)
                self.WeeklyReffresh()
        elif checkweeklycomp:
            for check3 in self.WeeklyProjectCompletedtable.selectedItems():
                rowitem1 = check3.row()
                column3 =check3.column()
                tableitem1 = self.WeeklyProjectCompletedtable.item(rowitem1, 0).text()
                tableitemvalueitem3 = self.WeeklyProjectCompletedtable.item(rowitem1, column3).text()
                fromsql.UpdateWeeklyCompletedData(int(tableitem1),column3,tableitemvalueitem3)
                self.WeeklyRefreshCompleted()

    def refreshProjectTable(self):
        self.AllProjectstable.clearContents()
        with open('trial.pickle','wb') as input:
            pickle.dump(f'{self.databasescombobobox.currentText()}.db',input)
        data = Sqldatabase(f'{self.databasescombobobox.currentText()}.db').ReadAllProjectData()

        for i,row in enumerate(data):
            self.AllProjectstable.setItem(i+1, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.AllProjectstable.setItem(i+1, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.AllProjectstable.setItem(i+1, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.AllProjectstable.setItem(i+1, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.AllProjectstable.setItem(i+1, 4, QtWidgets.QTableWidgetItem(row[4]))

    def WeeklyReffresh(self):
        self.WeeklyProjectstable.clearContents()
        with open('trial2.pickle','wb') as input:
            pickle.dump(f'{self.databasescombobobox.currentText()}.db',input)
        data1 = Sqldatabase(f'{self.databasescombobobox.currentText()}.db').ReadWeeklyProjectData()
        for i, row in enumerate(data1):
            self.WeeklyProjectstable.setItem(i + 1, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.WeeklyProjectstable.setItem(i + 1, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.WeeklyProjectstable.setItem(i + 1, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.WeeklyProjectstable.setItem(i + 1, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.WeeklyProjectstable.setItem(i + 1, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.WeeklyProjectstable.setItem(i + 1, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.WeeklyProjectstable.setItem(i + 1, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.WeeklyProjectstable.setItem(i + 1, 7, QtWidgets.QTableWidgetItem(row[7]))

    def WeeklyRefreshCompleted(self):
        self.WeeklyProjectCompletedtable.clearContents()
        with open('trial3.pickle','wb') as input:
            pickle.dump(f'{self.databasescombobobox.currentText()}.db',input)
        data2 = Sqldatabase(f'{self.databasescombobobox.currentText()}.db').ReadWeeklyweeklyCompletedData()
        for i, row in enumerate(data2):
            self.WeeklyProjectCompletedtable.setItem(i + 1, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.WeeklyProjectCompletedtable.setItem(i + 1, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.WeeklyProjectCompletedtable.setItem(i + 1, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.WeeklyProjectCompletedtable.setItem(i + 1, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.WeeklyProjectCompletedtable.setItem(i + 1, 4, QtWidgets.QTableWidgetItem(row[4]))

    def AddtoAllProject(self):
        self.project = AddProject()
        self.project.show()

    def addtoWeeklyProject(self):
        self.weeklyproject = AddProject()
        self.weeklyproject.weeklyprojectuis.show()

    def addweeklycompleted(self):
        self.weeklycompleted = AddProject()
        self.weeklycompleted.weeklycompleteduis.show()


if __name__=="__main__":
    # def my_exception(type, value, tback):
    #     print(tback, value, tback)
    #     sys.__excepthook__(type, value, tback)
    # sys.excepthook = my_exception
    app = QApplication(sys.argv)
    window = ManageUI()
    app.exec_()


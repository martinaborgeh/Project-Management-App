from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5 import uic
from DatabaseNamesDatabase import DatabaseFiles
import sys

class addDatabasename(QWidget):
    def __init__(self):
        super(addDatabasename, self).__init__()
        uic.loadUi(r"C:\Users\Martin Aborgeh\Desktop\Final_Year_Project_Manage_App\DatabaseConfigu.ui",self)
        self.adddb.clicked.connect(self.addtodbnamedb)
        self.cancelnewdb.clicked.connect(self.closewindow)
        self.show()

    def addtodbnamedb(self):
        dbfilename = self.adddbfile.text()
        dbnamedatabe = DatabaseFiles()
        dbnamedatabe.InsertDatabaseName(f'{dbfilename}')

    def closewindow(self):
        self.close()


if __name__=="__main__":
    def my_exception(type, value, tback):
        print(tback, value, tback)
        sys.__excepthook__(type, value, tback)
    sys.excepthook = my_exception
    app = QApplication(sys.argv)
    window = addDatabasename()
    app.exec_()

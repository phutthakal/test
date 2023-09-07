import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream 
import mysql.connector as mc
from PyQt5.QtCore import QTimer


from Bigmonitor import *

class MainBigWindow(QMainWindow):
    def __init__(self):
        super(MainBigWindow, self).__init__()

        self.ui = Ui_BigMonitor()
        self.ui.setupUi(self)
        self.connectdb()
        self.timer = QTimer()
        self.timer.start(6000)
        self.timer.timeout.connect(self.connectdb)
        # self.showFullScreen()
        
        #flamelesswindow
        # self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        

    def connectdb(self):
        mydb = mc.connect(
            host="localhost",
                user="root",
                password="",
                database="carlot"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT bay,noplate,zone FROM data WHERE status='N'")
        status = ("SELECT status FROM data WHERE status='F'")
        result = mycursor.fetchone()

        if status:
            self.ui.num_plate1_left_label.setText("")
            self.ui.zone1_left_label.setText("")
            self.ui.bay1_left_label.setText("")
            self.ui.num_plate2_left_label.setText("")
            self.ui.zone2_left_label.setText("")
            self.ui.bay2_left_label.setText("")
            self.ui.num_plate3_left_label.setText("")
            self.ui.zone3_left_label.setText("")
            self.ui.bay3_left_label.setText("")
            # self.ui.num_plate4_left_label.setText("")
            # self.ui.zone4_left_label.setText("")
            # self.ui.bay4_left_label.setText("")
            #right frrame
            self.ui.num_plate1_right_label.setText("")
            self.ui.zone1_right_label.setText("")
            self.ui.bay1_right_label.setText("")
            self.ui.num_plate2_right_label.setText("")
            self.ui.zone2_right_label.setText("")
            self.ui.bay2_right_label.setText("")
            

        if result:
            self.ui.num_plate1_left_label.setText(str(result[1]))
            self.ui.bay1_left_label.setText(str(result[0]))
            self.ui.zone1_left_label.setText(str(result[2]))
        result = mycursor.fetchone()
        if result:
            self.ui.num_plate2_left_label.setText(str(result[1]))
            self.ui.bay2_left_label.setText(str(result[0]))
            self.ui.zone2_left_label.setText(str(result[2]))
        result = mycursor.fetchone()
        if result:
            self.ui.num_plate3_left_label.setText(str(result[1]))
            self.ui.bay3_left_label.setText(str(result[0]))
            self.ui.zone3_left_label.setText(str(result[2]))
        result = mycursor.fetchone()
        # if result:
        #     self.ui.num_plate4_left_label.setText(str(result[1]))
        #     self.ui.bay4_left_label.setText(str(result[0]))
        #     self.ui.zone4_left_label.setText(str(result[2]))
        # result = mycursor.fetchone()
        if result:
            self.ui.num_plate1_right_label.setText(str(result[1]))
            self.ui.bay1_right_label.setText(str(result[0]))
            self.ui.zone1_right_label.setText(str(result[2]))
        result = mycursor.fetchone()
        if result:
            self.ui.num_plate2_right_label.setText(str(result[1]))
            self.ui.bay2_right_label.setText(str(result[0]))
            self.ui.zone2_right_label.setText(str(result[2]))
        result = mycursor.fetchone()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    bigwindow = MainBigWindow()
    bigwindow.show()
    
        
    sys.exit(app.exec())

    
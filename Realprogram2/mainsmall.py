import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream 
import mysql.connector as mc


from Smallmonitor import *

class MainSmallWindow(QMainWindow):
    def __init__(self):
        super(MainSmallWindow, self).__init__()

        self.ui = Ui_Smallmonitor()
        self.ui.setupUi(self)
        # self.showFullScreen()
        
        #flamelesswindow
        # self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
    
        
        mydb = mc.connect(
            host="localhost",
                user="root",
                password="",
                database="carlot"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT bay,noplate,zone FROM data WHERE status='N'")
        
        result = mycursor.fetchone()
        if result:
            self.ui.np_right_label.setText(str(result[1]))
            self.ui.zone_right_label.setText(str(result[2]))
            self.ui.bay_right_label.setText(str(result[0]))
          

if __name__ =="__main__":
    app = QApplication(sys.argv)

    # style_file = QFile("smallscreenstyle.qss")
    # style_file.open(QFile.ReadOnly | QFile.Text)
    # style_stream = QTextStream(style_file)
    # app.setStyleSheet(style_stream.readAll())

    window = MainSmallWindow()
    window.show()

    sys.exit(app.exec())
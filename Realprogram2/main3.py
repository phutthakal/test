import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream
import mysql.connector as mc
import requests

from test import *
from Mainwindow3 import Ui_MainWindow
from mainbig import *
from mainsmall import *

bay_order=["A","F","C","B","G","D","H","E"]
zone_order=["1","2"]
parked_lot=[]

a=["A201","A202","A203","A204",
"A301","A302","A303","A304",
"A401","A402","A403","A404",
"A501","A502","A503","A504",
"A601","A602","A603","A604",
"A701","A702","A703","A704","A705"]
b=["B201","B202","B203","B204",
"B301","B302","B303","B304",
"B401","B402","B403","B404",
"B501","B502","B503","B504",
"B601","B602","B603","B604",
"B701","B702","B703","B704","B705"]
c=["C201","C202","C203","C204",
"C301","C302","C303","C304",
"C401","C402","C403","C404",
"C501","C502","C503","C504",
"C601","C602","C603","C604",
"C701","C702","C703","C704","C705"]
d=["D201","D202","D203","D204",
"D301","D302","D303","D304",
"D401","D402","D403","D404",
"D501","D502","D503","D504",
"D601","D602","D603","D604",
"D701","D702","D703","D704","D705"]
e=["E201","E202","E203","E204",
"E301","E302","E303","E304",
"E401","E402","E403","E404",
"E501","E502","E503","E504",
"E601","E602","E603","E604",
"E701","E702","E703","E704","E705"]
f=["F201","F202","F203","F204",
"F301","F302","F303","F304",
"F401","F402","F403","F404",
"F501","F502","F503","F504",
"F601","F602","F603","F604",
"F701","F702","F703","F704","F705"]
g=["G201","G202","G203","G204",
"G301","G302","G303","G304",
"G401","G402","G403","G404",
"G501","G502","G503","G504",
"G601","G602","G603","G604",
"G701","G702","G703","G704","G705"]
h=["H201","H202","H203","H204",
"H301","H302","H303","H304",
"H401","H402","H403","H404",
"H501","H502","H503","H504",
"H601","H602","H603","H604",
"H701","H702","H703","H704","H705"]

oha=["A101","A102","A103","A104"]
ohb=["B101","B102","B103","B104"]
ohc=["C101","C102","C103","C104"]
ohd=["D101","D102","D103","D104"]
ohe=["E101","E102","E103","E104"]
ohf=["F101","F102","F103","F104"]
ohg=["G101","G102","G103","G104"]
ohh=["H101","H102","H103","H104"]

# nz = normal zone
nz={"A":a,"F":f,"C":c,"B":b,"G":g,"D":d,"H":h,"E":e}

# oz = over heigh zone
oz={"A":oha,"F":ohf,"C":ohc,"B":ohb,"G":ohg,"D":ohd,"H":ohh,"E":ohe}

#Parking Zone
z={"A":zone_order[0],"B":zone_order[0],"C":zone_order[1],"D":zone_order[1],"E":zone_order[1],"F":zone_order[1],"G":zone_order[1],"H":zone_order[1]}

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.full_home_btn.setChecked(True)
        self.ui.stacked_bay.setCurrentIndex(0)
        self.ui.locasort_a_btn.setChecked(True)
        self.ui.tableWidget.clicked.connect(self.getitem)
        self.ui.loaddb_btn.clicked.connect(self.loaddb)
        self.ui.update_btn.clicked.connect(self.updatedb)
        self.ui.monitor1_btn.clicked.connect(self.smallscreen)
        self.ui.monitor2_btn.clicked.connect(self.bigscreen)
        self.ui.reload_btn.clicked.connect(self.load_data_api)
        self.ui.accept_btn.clicked.connect(self.get_lot)
        self.ui.return_btn.clicked.connect(self.return_lot)
    
    # def on_search_btn_clicked(self):
    #     self.ui.stackedWidget.setCurrentIndex(5)
    #     search_text = self.ui.search_input.text().strip()
    #     if search_text:

    def on_listsort_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        
    def on_locationsort_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)
    
    def on_icon_home_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_full_home_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_icon_dashboard_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_full_dashboard_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_icon_accept_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_full_accept_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_icon_edit_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_full_edit_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_icon_monitor_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_full_monitor_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    #locationsort_page_btn
    def on_locasort_a_btn_toggled(self):
        self.ui.stacked_bay.setCurrentIndex(0)
    def on_locasort_b_btn_toggled(self):
        self.ui.stacked_bay.setCurrentIndex(1)
    def on_locasort_c_btn_toggled(self):
        self.ui.stacked_bay.setCurrentIndex(2)
    def on_locasort_d_btn_toggled(self):
        self.ui.stacked_bay.setCurrentIndex(3)
    def on_locasort_e_btn_toggled(self):
        self.ui.stacked_bay.setCurrentIndex(4)
    def on_locasort_f_btn_toggled(self):
        self.ui.stacked_bay.setCurrentIndex(5)
    def on_locasort_g_btn_toggled(self):
        self.ui.stacked_bay.setCurrentIndex(6)
    def on_locasort_h_btn_toggled(self):
        self.ui.stacked_bay.setCurrentIndex(7)


    def loaddb(self):
        while True:
            mydb = mc.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="carlot"
                )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM data")
            result = mycursor.fetchall()

            self.ui.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.ui.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.ui.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

            self.ui.status_update_check_label.setText("Load Complete")
            break

    def getitem(self):
        row = self.ui.tableWidget.currentRow()

        rowItemID = self.ui.tableWidget.item(row, 0).text()
        rowItemZone = self.ui.tableWidget.item(row, 1).text()
        rowItemBay = self.ui.tableWidget.item(row, 2).text()
        rowItemLot = self.ui.tableWidget.item(row, 3).text()
        rowItemLicenseplate = self.ui.tableWidget.item(row, 4).text()
        rowItemStatus = self.ui.tableWidget.item(row, 5).text()
        rowItemTime = self.ui.tableWidget.item(row, 6).text()

        self.ui.id_edit.setText(rowItemID)
        self.ui.zone_edit.setText(rowItemZone)
        self.ui.bay_edit.setText(rowItemBay)
        self.ui.lot_edit.setText(rowItemLot)
        self.ui.license_edit.setText(rowItemLicenseplate)
        self.ui.status_combobox.setCurrentText(rowItemStatus)
        self.ui.time_edit.setText(rowItemTime)

    def updatedb(self):
        updateId = self.ui.id_edit.text()
        updateZone = self.ui.zone_edit.text()
        updateBay = self.ui.bay_edit.text()
        updateLot = self.ui.lot_edit.text()
        updateLicenseplate = self.ui.license_edit.text()
        updateStatus = self.ui.status_combobox.currentText()

        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="carlot"
        )

        mycursor = mydb.cursor()
        value = (updateBay,updateLicenseplate,updateZone, updateLot, updateStatus, updateId)
        updatedb = "UPDATE data SET bay = %s, noplate = %s, zone = %s, nolot = %s, status = %s WHERE id = %s"

        try:
            mycursor.execute(updatedb, value)
            mydb.commit()
            self.ui.status_update_check_label.setText("Update Complete")
        except:
            self.ui.status_update_check_label.setText("Update Incomplete")

    def smallscreen(self):
        self.window = MainSmallWindow()    
        self.window.show()
    
    def bigscreen(self):
        self.mainbig = MainBigWindow()
        self.mainbig.show()
    
    def load_data_api(self):
        response = requests.get('http://127.0.0.1:8000/api/test/users')
        api_noplate = response.json()[0]['license_plate']
        api_height = str(response.json()[0]['height'])
        
        self.ui.api_lcp_label.setText(api_noplate)
        self.ui.api_height_label.setText(api_height)
    def refresh_data():
            while True:
                response = requests.get('http://127.0.0.1:8000/api/test/users')
                api_height = response.json()[0]['height']
                return api_height
            
    def get_lot(self):
        car_height = refresh_data()
        parking_lot = None
        while True:
            for _ in range(8):
                if car_height>=190:
                    removed_element = bay_order.pop(0)
                    bay_order.append(removed_element)
                    if len(oz[removed_element])==0:
                        continue
                    parking_lot = oz[removed_element].pop(0)
                    
                    parked_lot.append(parking_lot)
                    print("Your Parking zone is : ",z[removed_element[0]])
                    print("Your bay is :",removed_element)
                    print("your parking lot is : ",parking_lot)
                    self.ui.accept_show_zone_label.setText(z[removed_element[0]])
                    self.ui.accept_show_bay_label.setText(removed_element)
                    self.ui.accept_show_lot_label.setText(parking_lot)
                    print("parked lot check:",parked_lot)
            
                    return parked_lot
                
                    
                else:
                    removed_element = bay_order.pop(0)            
                    bay_order.append(removed_element)                              
                    if len(nz[removed_element])==0:
                        continue
                    parking_lot = nz[removed_element].pop(0)
                    parked_lot.append(parking_lot)
                    print("Your Parking zone is : ",z[removed_element[0]])         
                    print("Your bay is :",removed_element)
                    print("your parking lot is : ",parking_lot)
                    self.ui.accept_show_zone_label.setText(z[removed_element[0]])
                    self.ui.accept_show_bay_label.setText(removed_element)
                    self.ui.accept_show_lot_label.setText(parking_lot)
                    print("parked lot check:",parked_lot)
                    return parked_lot
            return parking_lot
        
    def return_lot(lot_no):
        if lot_no in parked_lot:
            if lot_no[1]=="1":
                oz[lot_no[0]].append(lot_no)
            else:
                nz[lot_no[0]]
            parked_lot.remove(lot_no)
            return True
        return False


if __name__ == "__main__":
    app = QApplication(sys.argv)

    style_file = QFile("style2.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
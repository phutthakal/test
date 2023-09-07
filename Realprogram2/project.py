import requests
import mysql.connector as mc
import time

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
   
def refresh_data():
   while True:
      response = requests.get('http://127.0.0.1:8000/api/test/users')
      api_noplate = response.json()[0]['license_plate']
      api_height = response.json()[0]['height']
      # time.sleep(0.5)
      return api_height
      

def get_lot(car_height):
   parking_lot = None
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
   
# def savedata_db(removed_element, api_noplate):
#    try:
#       mydb = mc.connect(
#                host="localhost",
#                   user="root",
#                   password="",
#                   database="carlot"
#             )
#       mycursor = mydb.cursor()
#       bay = get_lot(removed_element)
#       noplate = refresh_data(api_noplate)
#       zone = get_lot(removed_element)

#       query = "INSERT INTO data(bay, noplate, zone, nolot,status) VALUES (%s, %s, %s, %s, %s)"
#       value = ()
#       mycursor.execute(query)
#       print("Save data complete")
#    except:
#       print("Save data incomplete")

def program():
    try:
        while True:
         print("=============== Test2 ===============")
         print("1. Enter your car Height")
         print("2. Return Parking Bay")
         print("3. Print parking available in bay")
         print("4. Close Program")
         ch=int(input("Select option : "))
         if ch==1:
            height = refresh_data()
            parked_lot=get_lot(height)
            if parked_lot==None:
               print("Can not get parking lot")
            
         elif ch==2:
            lot_no=input("Enter lot to return: ")
            if return_lot(lot_no):
               print("parked lot check: ",parked_lot)
            else:
               print("parked lot check: ",parked_lot)
         elif ch==3:
            bay=input("Enter bay to print: ")
            print(nz[bay])
            print(oz[bay])
         elif ch==4:
            print("=============== Thank you ===============")
            break 

    except:
        program()
program()
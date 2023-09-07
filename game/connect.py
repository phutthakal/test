# import mysql.connector

# #ทำการเชื่อมต่อกับฐานข้อมูลง่าย ๆ แค่ใส่ Host / User / Password ให้ถูกต้อง
# connection = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="puzzle"
# )

# db_cursor = connection.cursor()

# #สร้าง String ไว้รอใส่คำสั่งสำหรับการ SELECT
# db_cursor.execute("SELECT time FROM user Where time<30 LIMIT 1")

# #ดึงข้อมูลมาเก็บไว้ใน result
# result = db_cursor.fetchall()

# #แสดงผลข้อมูลมาทีละตัวจากที่ SELECT ได้ทั้งหมด
# for data in result:
#   print(data)


# from flask import Flask, render_template
# import psycopg2 as p
# app = Flask(__name__)

# @app.route('/list')
# def list():

#     con = p.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="puzzle"
#     )
#     cur = con.cursor()
#     cur.execute('SELECT version()')
#     sql = "SELECT time FROM user time<20 LIMIT 1"
#     sql = sql.encode('utf-8')
#     cur.execute(sql)
#     rows = cur.fetchall()
#     return render_template("index.html", rows=rows)


from flask import Flask, render_template, jsonify
import psycopg2 as p

app = Flask(__name__)

@app.route('/list')
def list():
    con = p.connect(
        host="localhost",
        user="root",
        password="",
        database="puzzle"
    )
    cur = con.cursor()
    cur.execute('SELECT version()')
    sql = "SELECT time FROM user WHERE time < 20 LIMIT 1"
    sql = sql.encode('utf-8')
    cur.execute(sql)
    rows = cur.fetchall()

    # ดึงค่า time จาก rows (ถ้ามีข้อมูล)
    usetime = rows[0][0] if rows else "N/A"  # ถ้าไม่มีข้อมูลให้เป็น "N/A"

    return jsonify(usetime=usetime)


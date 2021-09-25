#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dbConfig import *


@app.route('/homework', methods=['POST'])
def homework():
    try:
        data = request.json
        account_id = data["account_id"]
        course_name = data["course_name"]
        room = data["room"]
        date = data["date"]
        detail = data["detail"]
        filePdf = data["filePdf"]

        # connect db
        conn = connectToDB()
        cursor = conn.cursor()

        sql = """ INSERT INTO homework (account_id, course_name, room, date, detail, file) VALUES (%s,%s,%s,%s,%s,%s)""" 
        cursor.execute(sql,(account_id,course_name,room,date,detail,filePdf))
        conn.commit()

        # data_sql = cursor.fetchall()
        # columns = [column[0] for column in cursor.description]
        # result = toJson(data_sql,columns)
        result = {"status":"OK","result":"เพิ่มข้อมูลสำเร็จ"}
    except Exception as e:
        print(e)
        result = {"status":"ER","errorCode":"ER999","errorMessage":str(e)}
    finally:
        conn.close()
        return result

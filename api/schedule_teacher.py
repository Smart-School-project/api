#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ast import literal_eval
from dbConfig import *
import json


@app.route('/schedule_teacher', methods=['POST'])
def schedule_teacher():
    try:
        data = request.json
        account_id = data["account_id"]

        # # connect db
        conn = connectToDB()
        cursor = conn.cursor()

        sql = """ SELECT * FROM schedule_teacher WHERE account_id = """ + str(account_id)
        cursor.execute(sql)
        data_sql = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = toJson(data_sql,columns)
        if len(result) > 0:
            result[0]['schedule'] =  literal_eval(result[0]['schedule'])
            result = {"status":"OK","result":result}
        else:
            result = {"status":"ER","errorMessage":"ไม่พบ ข้อมูล"}
    except Exception as e:
        print(e)
        result = {"status":"ER","errorCode":"ER999","errorMessage":str(e)}
    finally:
        # conn.close()
        return result
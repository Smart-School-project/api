#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dbConfig import *


@app.route('/leave', methods=['POST'])
def leave():
    try:
        data = request.json
        subject = data["subject"]
        room = data["room"]
        result = []

        # connect db
        conn = connectToDB()
        cursor = conn.cursor()

        sql = " SELECT * FROM `leave` WHERE subject = '" + str(subject) +"' AND LEFT(room,3) = '" + str(room) +"'"
        print(sql)
        cursor.execute(sql)
        data_sql = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = toJson(data_sql,columns)
        if len(result) >= 0:
            result = {"status":"OK","result":result}
        else:
            result = {"status":"ER","errorMessage":"Not found"}
    except Exception as e:
        print(e)
        result = {"status":"ER","errorCode":"ER999","errorMessage":str(e)}
    finally:
        conn.close()
        return result


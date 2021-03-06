#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dbConfig import *


@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data["username"]
        password = data["password"]

        # connect db
        conn = connectToDB()
        cursor = conn.cursor()

        sql = """ SELECT account.id,account.role_id,profile.id AS std_id FROM account INNER JOIN profile ON account.id = profile.account_id WHERE username = %s AND password = %s """
        print(sql)
        cursor.execute(sql,(username,password))
        data_sql = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = toJson(data_sql,columns)
        if len(result) > 0:
            result = {"status":"OK","result":result}
        else:
            result = {"status":"ER","errorMessage":"Username or Password in correct"}
    except Exception as e:
        print(e)
        result = {"status":"ER","errorCode":"ER999","errorMessage":str(e)}
    finally:
        conn.close()
        return result


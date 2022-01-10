#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dbConfig import *
from ast import literal_eval


@app.route('/update_score', methods=['POST'])
def update_score():
    try:
        data = request.json
        # connect db
        conn = connectToDB()
        cursor = conn.cursor()
        for i in data['items']:
            sql = """ UPDATE score SET full= %s, have=%s,miss=%s,sick=%s,affiar=%s,indicators=%s,itemScore=%s,have_score=%s WHERE id = %s """ 
            # sql = """ UPDATE score SET full=[%s],have=[%s],miss=[%s],sick=[%s],affiar=[%s],indicators=[%s],itemScore=[%s] WHERE id = """ + str(i['id'])
            # cursor.execute(sql,(i['full'],i['have'],i['miss'],i['sick'],i['affiar'],str(i['indicators']),str(data['item_score'])))
            cursor.execute(sql,(i['full'],i['have'],i['miss'],i['sick'],i['affiar'],str(i['indicators']),str(data['item_score']),i['have_score'],str(i['id'])))
            print(sql)
            conn.commit()

        result = {"status":"OK","result":"อัพเดทข้อมูลสำเร็จ"}
        
    except Exception as e:
        print(e)
        result = {"status":"ER","errorCode":"ER999","errorMessage":str(e)}
    finally:
        conn.close()
        return result


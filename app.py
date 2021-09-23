#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dbConfig import *
from api import *
# ------------------------------------------------------------------------------

import mysql.connector
mydb = mysql.connector.connect(
host='localhost',
database='Project',
user='root',
password='root',
port=8899
)

#print(mydb)

query = "SELECT * FROM account"
cursor = mydb.cursor()
cursor.execute(query)
row = cursor.fetchone()
#print(row)





if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',threaded=True,port=3000)

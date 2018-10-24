from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

DB_NAME='letsgo'

DB_TABLES={}

DB_TABLES['USER'] = (
    " CREATE TABLE USER( ID INT(11) NOT NULL AUTO_INCREMENT, "
    " NAME VARCHAR(50) NOT NULL, "
    " PHONE VARCHAR(17), "
    " PRIMARY KEY(ID) "
    ") ENGINE=InnoDB "
)

cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='letsgo')
cursor = cnx.cursor()

for table_name in DB_TABLES:
    table_description = DB_TABLES[table_name]
    try:
        print('Create table {} '.format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('Already exists')
        else:
            print(err.msg)
    else:
        print('OK!')

cursor.close
cnx.close


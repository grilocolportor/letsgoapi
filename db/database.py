from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

DB_TABLES = {}

DB_TABLES['USER'] = (
    " CREATE TABLE USER( ID INT(11) NOT NULL AUTO_INCREMENT, "
    " NAME VARCHAR(50) NOT NULL, "
    " PASSWORD VARCHAR(8) NOT NULL, "
    " PHONE VARCHAR(17), "
    " PROFILE_IMAGE_PATH VARCHAR(100), "
    " PRIMARY KEY(ID) "
    ") ENGINE=InnoDB "
)

def connect():
    """ Connect to Mysql Database """
    DB_NAME = 'letsgo'
    try:
        conn = mysql.connector.connect(host='localhost', 
                                       database='letsgo', 
                                       user='root', 
                                       password='root')
        
        if conn.is_connected():
            print("Connected to MySql Databae: {} \n".format(DB_NAME), end='')
            cursor = conn.cursor()

            for table_name in DB_TABLES:
                table_description = DB_TABLES[table_name]
                try:
                    cursor.execute(table_description)
                    print('Creating table {} \n'.format(table_name), end='')
                except mysql.connector.Error as err:
                    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                        print('Table {} Already exists\n'.format(table_name), end='')
                    else:
                        print(err.msg)
                else:
                    print('Table {} created success!\n'.format(table_name), end='')
        
            cursor.close()

    except Error as err:
        print(err)
    
    finally:
        conn.close()
        print('database desconnected\n')

if __name__ == '__main__':
    connect()

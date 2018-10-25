from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'letsgo'
TB_NAME = 'USER'

def insert():
    """ Insert new user """
    try:
        conn = mysql.connector.connect(host='localhost', 
                                       database='letsgo', 
                                       user='root', 
                                       password='root')
        
        if conn.is_connected():
            print("Connected to MySql Databae: {} \n".format(DB_NAME), end='')
            cursor = conn.cursor()

            sql = (" INSERT INTO USER "
                " (NAME, PASSWORD, PHONE, PROFILE_IMAGE_PATH ) "
                " VALUES "
                " (%(nome)s, %(senha)s, %(phone)s, %(image)s) ")

            user = {
                'nome': 'teste1',
                'senha': 'ttt',
                'phone': '(81)123456789',
                'image': '/the/path/of/image'
            }

            cursor.execute(sql, user)

            conn.commit()

            cursor.close()

    except Error as err:
        print(err)
    
    finally:
        conn.close()

if __name__=='__main__':
    insert()
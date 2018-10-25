from __future__ import print_function

import mysql.connector
import json
from mysql.connector import errorcode

DB_NAME = 'letsgo'
TB_NAME = 'USER'

def update(user):
    """update item by param"""
    try:
        conn = mysql.connector.connect(host='localhost', 
                                       database='letsgo', 
                                       user='root', 
                                       password='root')
        
        if conn.is_connected():
            print("Connected to MySql Databae: {} \n".format(DB_NAME), end='')
            cursor = conn.cursor()

            param = mountSql(user)

            if not param:
                sql = (" UPDATE USER(NAME = %(nome)s, PASSWORD=%(senha)s, PHONE=%(phone)s) where 1=1 " + param + ";")
                print(sql)
                cursor.execute(sql)
                conn.commit()

            cursor.close()

    except ValueError as err:
        print(err)
    
    finally:
        conn.close()
        print('\n Database desconnected \n')

def delete(user):
    """delete item by param"""
    try:
        conn = mysql.connector.connect(host='localhost', 
                                       database='letsgo', 
                                       user='root', 
                                       password='root')
        
        if conn.is_connected():
            print("Connected to MySql Databae: {} \n".format(DB_NAME), end='')
            cursor = conn.cursor()

            param = mountSql(user)

            if not param:
                sql = (" DELETE  FROM USER where 1=1 " + param + ";")
                print(sql)
                cursor.execute(sql)
                conn.commit()

            cursor.close()

    except ValueError as err:
        print(err)
    
    finally:
        conn.close()
        print('\n Database desconnected \n')


def queryByParam(user):
    """ get all row by param """
    try:
        conn = mysql.connector.connect(host='localhost', 
                                       database='letsgo', 
                                       user='root', 
                                       password='root')
        
        if conn.is_connected():
            print("Connected to MySql Databae: {} \n".format(DB_NAME), end='')
            cursor = conn.cursor()

            param = mountSql(user)

            sql = (" SELECT * FROM USER where 1=1 " + param + ";")

            print(sql)

            cursor.execute(sql)

            row = cursor.fetchone()

            while row is not None:
                print('\n{}'.format(row), end='')
                row = cursor.fetchone()

            cursor.close()

    except ValueError as err:
        print(err)
    
    finally:
        conn.close()
        print('\n Database desconnected \n')

def queryAll():
    """ get all row from table """
    try:
        conn = mysql.connector.connect(host='localhost', 
                                       database='letsgo', 
                                       user='root', 
                                       password='root')
        
        if conn.is_connected():
            print("Connected to MySql Databae: {} \n".format(DB_NAME), end='')
            cursor = conn.cursor()

            sql = (" SELECT * FROM USER;")

            cursor.execute(sql)

            row = cursor.fetchone()

            while row is not None:
                print('\n{}'.format(row), end='')
                row = cursor.fetchone()

            cursor.close()

    except ValueError as err:
        print(err)
    
    finally:
        conn.close()
        print('\n Database desconnected \n')

def insert(user):
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

            cursor.execute(sql, user)

            conn.commit()

            cursor.close()

    except ValueError as err:
        print(err)
    
    finally:
        conn.close()
        print('Database desconnected \n')

def mountSql(user):
    param = ""

    if  user['id']:
        param = param + " and ID = " + user['id'] + " "
    if  user['nome']:
        param = param + " and NAME = '" +user['nome'] + "' "
    if  user['senha']:
        param = param + " and PASSWORD = '" + user['senha'] + "' "
    if  user['phone']:
        param = param + " and PHONE = '" + user['phone'] + "' "
    
    return param

if __name__=='__main__':
    user = json.loads('{"id": "2", "nome": "", "senha": "", "phone": "",  "image": ""}')
    queryAll()
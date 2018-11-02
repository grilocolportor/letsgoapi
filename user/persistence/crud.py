import falcon
from __future__ import print_function

import mysql.connector
import json
from mysql.connector import errorcode

DB_NAME = 'letsgo'
TB_NAME = 'USER'

class Crud():

    def on_get(self, req, resp):
        resp.body = 'Deu tudo certo'
        resp.status = falcon.HTTP_200

    def update(self, user):
        """update item by param"""
        try:
            conn = mysql.connector.connect(host='localhosst', 
                                        database='letsgo', 
                                        user='root', 
                                        password='root')
            
            if conn.is_connected():
                print("Connected to MySql Databae: {} \n".format(DB_NAME), end='')
                cursor = conn.cursor()

                param = self.mountSql(user)

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

    def delete(self, user):
        """delete item by param"""
        try:
            conn = mysql.connector.connect(host='localhost', 
                                        database='letsgo', 
                                        user='root', 
                                        password='root')
            
            if conn.is_connected():
                print("Connected to MySql Databae: {} \n".format(DB_NAME), end='')
                cursor = conn.cursor()

                param = self.mountSql(user)

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


    def queryByParam(self, user):
        """ get all row by param """
        try:
            conn = mysql.connector.connect(host='localhost', 
                                        database='letsgo', 
                                        user='root', 
                                        password='root')
            
            if conn.is_connected():
                print("Connected to MySql Databae: {} \n".format(DB_NAME), end='')
                cursor = conn.cursor()

                param = self.mountSql(user)

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

    def queryAll(self):
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

    def insert(self, user):
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

    def mountSql(self, user):
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
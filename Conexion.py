import mysql.connector
from mysql.connector.connection import MySQLConnection

class Conexion:
    _MySQLConnection: MySQLConnection

    def __init__(self):
        self._MySQLConnection = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="", 
            database="estacionamiento"
            )
    
    def __del__(self):
        self._MySQLConnection.close()

    def hacerSelectUno(self,sqlquery:str):
        cursor=self._MySQLConnection.cursor()
        cursor.execute(sqlquery)
        listaSQL = cursor.fetchone()
        return listaSQL
    
    def hacerSelectTodos(self, sqlquery:str):
        cursor=self._MySQLConnection.cursor()
        cursor.execute(sqlquery)
        listaSQL = cursor.fetchall()
        return listaSQL

    def hacerInsert(self, sqlquery:str):
        cursor=self._MySQLConnection.cursor()
        cursor.execute(sqlquery)
        self._MySQLConnection.commit()
        return cursor._last_insert_id
    
    def hacerUpdate(self, sqlquery:str):
        cursor=self._MySQLConnection.cursor()
        cursor.execute(sqlquery)
        self._MySQLConnection.commit()
        return cursor.rowcount
         

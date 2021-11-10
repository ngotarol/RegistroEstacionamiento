from dataclasses import dataclass

from mysql import connector
from Conexion import Conexion
@dataclass

class Vehiculo:
    patente: str
    color: str
    tipo_vehiculo: str 

    def registrarVehiculo(self):
        if Vehiculo.buscarPatente(self.patente) == None:
            conector = Conexion()
            sql = f"insert into vehiculo values('{self.patente}','{self.color}','{self.tipo_vehiculo}')"
            conector.hacerInsert(sql)
            del conector        
        else:
            print("Vehiculo previamente existente")
        
    def buscarPatente(patente:str):
        conector = Conexion()
        vehiculo = None
        sql = f"select patente,color,tipo_vehiculo from vehiculo where patente = '{patente}'"    
        listaSQL = conector.hacerSelectUno(sql)
        if listaSQL!=None:           
            vehiculo = Vehiculo(listaSQL[0],listaSQL[1],listaSQL[2])            
        del conector
        return vehiculo
        
    def mostrarDatos(self):
        imprimir = "Datos del vehículo\n"
        imprimir = imprimir + f"Patente: {self.patente}\n"
        imprimir = imprimir + f"Color: {self.color}\n"
        imprimir = imprimir + f"Tipo de vehiculo: {self.tipo_vehiculo}\n"
        return imprimir
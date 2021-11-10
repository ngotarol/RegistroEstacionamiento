import os
from dataclasses import dataclass
from Ticket import Ticket
from Vehiculo import Vehiculo 
import mysql.connector
os.system("cls")

def ingresarPatente():
    patente = input("Ingrese patente\n")
    if len(patente)==6: a=2
    else: 
        print("Ingrese una patente de 6 caracteres")
        ingresarPatente()
    return patente

def ingresarTicket():
    nro_ticket = -1
    try:
        nro_ticket = int(input("Ingrese número de ticket\n"))
    except:
        print("Ingrese un número")
        ingresarTicket()   
    return nro_ticket


menu = True
print("Bienvenido al sistema de registro")
while menu:
    opcion = int(input("Seleccione una opción:\n1.Registro de ingreso\n2.Registro de salida\n3.Modificar un vehículo\n4.Eliminar un vehículo\n5.Buscar un ticket\n6.Buscar vehículo\n7.Historial de ingresos\n8. Salir\n"))
    while opcion>=1 and opcion<=8:
        if opcion==1:
            patente = ingresarPatente()
            vehiculo = Vehiculo.buscarPatente(patente) #reviso si está creado en la BD   
            if vehiculo == None:
                print("Vehiculo sin registro en el sistema")
                tipo_vehiculo = input("Ingrese tipo de vehículo: auto/moto/camioneta\n")
                color = input("Ingrese color del vehículo\n")
                vehiculo = Vehiculo(patente,color,tipo_vehiculo)
                vehiculo.registrarVehiculo()
            print(vehiculo.mostrarDatos())
            ticket = Ticket.generarTicket(patente)
            print(ticket.mostrarDatos())
            opcion = 0
        if opcion ==2:
            ticket = Ticket.buscarTicketxPatente(ingresarPatente())
            ticket.registrarSalida()
            print(ticket.mostrarDatos())
            opcion = 0
        #if opcion==3:

        if opcion==5:
            ticket = Ticket.buscarTicketxNro(ingresarTicket())
            print(ticket.mostrarDatos())
            opcion = 0       

        if opcion==6:          
            vehiculo = Vehiculo.buscarPatente(ingresarPatente())
            if vehiculo == None:
                print("Vehiculo sin registro en el sistema")
            else:
                print(vehiculo.mostrarDatos())
            opcion = 0
        
        if opcion==8:
            print("Desea salir del programa?")
            while opcion==8:
                salir = int(input("1. Si\n2. No\n"))
                if salir == 1: 
                    menu = False
                    opcion = 10
                else:
                    if salir == 2: opcion = 0
                    else: print("ingrese una opción válida")
else:
    print("Fin del programa")
from dataclasses import dataclass
from Conexion import Conexion
import datetime
@dataclass

class Ticket:
    nro_ticket:int
    patente: str
    fecha_entrada: datetime
    fecha_salida: datetime

    def generarTicket(patente:str):       
        sql=f"INSERT INTO ticket(patente,fecha_entrada) VALUES('{patente}', now())"
        conector = Conexion()        
        nro_ticket = conector.hacerInsert(sql)        
        del conector        
        ticket = Ticket.buscarTicketxNro(nro_ticket)
        return ticket

    def buscarTicketxPatente(patente):
        ticket = None
        sql = f"SELECT nro_ticket,patente,fecha_entrada,fecha_salida FROM ticket WHERE patente = '{patente}' ORDER BY nro_ticket DESC LIMIT 1"
        conector = Conexion()
        dtoTicket = conector.hacerSelectUno(sql)
        if dtoTicket != None:
            ticket = Ticket(dtoTicket[0],dtoTicket[1],dtoTicket[2],dtoTicket[3])        
        del conector
        return ticket

    def buscarTicketxNro(nro_ticket):
        ticket = None
        sql = f"SELECT nro_ticket,patente,fecha_entrada,fecha_salida FROM ticket WHERE nro_ticket = '{nro_ticket}'"
        conector = Conexion()
        dtoTicket = conector.hacerSelectUno(sql)
        if dtoTicket != None:
            ticket = Ticket(dtoTicket[0],dtoTicket[1],dtoTicket[2],dtoTicket[3])        
        del conector
        return ticket

    def registrarSalida(self):
        sql = f"UPDATE ticket SET fecha_salida = now() WHERE nro_ticket = '{self.nro_ticket}'"
        conector = Conexion()
        conector.hacerUpdate(sql)
        sql = f"SELECT fecha_salida FROM ticket WHERE nro_ticket = '{self.nro_ticket}'" #tomo la fecha que el servidor de BD asignó
        dtoFechaSalida = conector.hacerSelectUno(sql)
        self.fecha_salida = dtoFechaSalida[0]
        del conector
        return self.fecha_salida

    def mostrarDatos(self):
        imprimir = "Datos del ticket\n"
        imprimir = imprimir + f"Nro ticket: {self.nro_ticket}\n"
        imprimir = imprimir + f"Patente: {self.patente}\n"
        imprimir = imprimir + f"Fecha entrada: {self.fecha_entrada}\n"
        imprimir = imprimir + f"Fecha salida: {self.fecha_salida}\n"
        return imprimir
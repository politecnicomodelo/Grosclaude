from .Pasajeros import Pasajero
from .ServicioBordo import ServicioABordo
from .Servicio import Servicios
from .Aviones import Avion
from datetime import datetime
class Vuelo(object):

    def __init__(self,a,f,h,o,d,t,p):
        self.Avion = a
        self.Fecha = f
        self.Hora = h
        self.Origen = o
        self.Destino = d
        self.Tripulantes = t
        self.Pasajeros = p

    def CantPersonas(self):
        return len(self.Tripulantes) + len(self.Pasajeros)

    def PasajeroJoven(self):
        a=[]
        for item in self.Pasajeros:
            a.append(item.FechaNacimiento)
        return max(a)

    def TripulacionMin(self):
        if len(self.Tripulantes) >= self.Avion.CantTrip:
            return True
        return False

    def Colados(self):
        Lis = []
        existe=0
        for item in self.Tripulantes:
            existe = 0
            for item2 in item.ModAvion:
                if item2 != None:
                    if item2.Codigo == self.Avion.Codigo:
                        existe = 1
            if existe == 0 and item not in Lis:
                Lis.append(item.Nombre)
        return Lis

    def PersonasVip(self):
        lista = []
        for item in self.Pasajeros:
            if item !=None:
                if item.Vip == 1 or item.Necesidades != '\n' and item not in lista:
                    lista.append(item)
        return lista






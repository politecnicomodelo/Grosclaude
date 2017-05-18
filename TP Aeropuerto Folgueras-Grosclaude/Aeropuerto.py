from Clases.Personas import Persona
from Clases.Pasajeros import Pasajero
from Clases.ServicioBordo import ServicioABordo
from Clases.Aviones import Avion
from Clases.Vuelos import Vuelo
from Clases.Servicio import Servicios
Pasajeros = []
Servi = []
Pilotos = []
Aviones = []
Vuelos = []

def Cargar():
    with open("aviones.dat","r") as file:
        for item in file:
            a = item.split("|")
            b = Avion(a[0],a[1],a[2])
            Aviones.append(b)
    a = []
    with open("personas.dat","r") as file:
        for item in file:
            a = item.split("|")
            if a[0]== "Servicio":
                c = Servicios(a[1],a[2],a[3],a[4],a[5],a[6])
                Servi.append(c)
            elif a[0] == "Pasajero":
                e.Pasajero(a[1],a[2],a[3],a[4],a[5],a[6])
                Pasajeros.append(e)
            elif a[0] == "Piloto":
                f = ServicioABordo(a[1],a[2],a[3],a[4],a[5])
                Pilotos.append(f)
    a = []
    with open("vuelos.dat","r") as file:
        for item in file:
            a = item.split("|")

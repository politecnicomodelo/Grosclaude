from Clases.Personas import Persona
from Clases.Pasajeros import Pasajero
from Clases.ServicioBordo import ServicioABordo
from Clases.Aviones import Avion
from Clases.Vuelos import Vuelo
from Clases.Servicio import Servicios
from datetime import datetime
from datetime import date
Pasajeros = []
Servi = []
Pilotos = []
Aviones = []
Vuelos = []


def Cargar():
    trip = []
    pas = []
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
                c = Servicios(a[1],a[2],TransformarFecha(a[3]),a[4],EncontrarAviones(a[5]),a[6])
                Servi.append(c)
            elif a[0] == "Pasajero":
                e = Pasajero(a[1],a[2],TransformarFecha(a[3]),a[4],a[5],a[6])
                Pasajeros.append(e)
            elif a[0] == "Piloto":
                f = ServicioABordo(a[1],a[2],TransformarFecha(a[3]),a[4],EncontrarAviones(a[5]))
                Pilotos.append(f)
    a = []
    with open("vuelos.dat","r") as file:
        for item in file:
            a = item.split("|")
            b = a[5].split(",")
            for item in b:
                trip.append(EncontrarTripulacion(item))
            b = a[6].split(",")
            for item in b:
                pas.append(EncontrarPasajeros(item))
            v = Vuelo(EncontrarAvion(a[0]),TransformarFecha(a[1]),a[2],a[3],a[4],trip,pas)
            Vuelos.append(v)

def TransformarFecha(f):
    a = f.split("-")
    return date(int(a[2]),int(a[1]),int(a[0]))

def EncontrarAviones(modelos):
    a = modelos.split(",")
    b = []
    for item in a:
        b.append(EncontrarAvion(item))
    return b

def EncontrarAvion(mod):
    for item in Aviones:
        if item.Codigo == mod:
            return item

def EncontrarTripulacion(dni):
    for item in Servi:
        if item.Dni == dni:
            return item
    for item in Pilotos:
        if item.Dni == dni:
            return item
def EncontrarPasajeros(dni):
    for item in Pasajeros:
        if item.Dni == dni:
            return item
    for item in Servi:
        if item.Dni == dni:
            return item
    for item in Pilotos:
        if item.Dni == dni:
            return item

def VuelosPorDia():
    lista = []
    for item in Vuelos:
        for item2 in Vuelos:
            if item != item2 and item.Fecha == item2.Fecha:
                for item3 in item.Tripulantes:
                    if item3 in item2.Tripulantes:
                        lista.append(item3)
    return lista
Cargar()
print(Vuelos[0].Tripulantes[0].Nombre)
print(Vuelos[0].CantPersonas())
a=0
for item in Vuelos:
    if Vuelos[0].TripulacionMin():
        a += 1
print("Hay " + str(a) + " vuelos que cumplen con la tripulacion minima")
b=1
for item in Vuelos:
    print("En el vuelo " + str(b) + " los Colados son: " )
    for item2 in item.Colados():
        print(item2)
    b+=1
for item in VuelosPorDia():
    print(item.Nombre)
    print(item.Dni)
print(Vuelos[0].PasajeroJoven().Nombre)
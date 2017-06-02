from Clases.Pasajeros import Pasajero
from Clases.ServicioBordo import ServicioABordo
from Clases.Aviones import Avion
from Clases.Vuelos import Vuelo
from Clases.Servicio import Servicios
from datetime import datetime
from datetime import date
import os
Pasajeros = []
Servi = []
Pilotos = []
Aviones = []
Vuelos = []

def MostrarPasajeros(Vuelo):
    a=1
    print(105 * '=')
    X = ['Vuelo','Pasajeros','Fecha de Nacimiento','DNI']
    print('{: <20} | {: <43} | {: <20} | {: <20}'.format(*X))
    print(105*'=')
    for item in Vuelos:
        for item2 in item.Pasajeros:
            texto = [a,item2.Nombre, item2.Apellido, str(item2.FechaNacimiento), item2.Dni]
            print('{: <20} | {: <20} | {: <20} | {: <20} | {: <20}'.format(*texto))
        print(" ")
        a+=1

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
            trip=[]
            pas=[]

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
                    if item3 in item2.Tripulantes and item3 not in lista:
                        lista.append(item3)
    return lista

Cargar()

def Ejercicio_6():
    a = 1
    for item in Vuelos:
        print("Vuelo numero " + str(a) + ":")
        print("Las personas vip o con necesidades especiales son : ")
        for item2 in item.PersonasVip():
            if item2.Necesidades != '\n' and item2.Vip=="1":
                X = [item2.Nombre, item2.Dni,"Es VIP",item2.Necesidades]
                print('{: <20} | {: <20} | {: <20} | {: <20} '.format(*X))
            elif item2.Vip == "1":
                X = [item2.Nombre, item2.Dni, "Es VIP"]
                print('{: <20} | {: <20} | {: <20} '.format(*X))
            else:

                X = [item2.Nombre, item2.Dni, item2.Necesidades]
                print('{: <20} | {: <20} | {: <20} '.format(*X))
        a += 1
        print(" ")

def EncontrarPasFecha(f):
    for item in Pasajeros:
        if item.FechaNacimiento==f:
            return item

def Menu():
    while True:
        os.system('clear')
        print("1: Nomina de Personas por Vuelo")
        print("2: Pasajero mas joven por Vuelo")
        print("3: Tripulacion minima no alcanzada")
        print("4: Vuelos con personas no autorizadas")
        print("5: Tripulantes que viajen mas de una vez por dia")
        print("6: Personas VIP o Necesitadas")
        print("Salir")
        Elegir = input()
        os.system('clear')
        if Elegir == "1":
            MostrarPasajeros(Vuelos[0])
            print("Escriba salir para continuar")
            Salir = input()
            while Salir != "salir":
                print("INGRESE SALIR")
                Salir = input()
        elif Elegir == "2":
            a = 1
            for item in Vuelos:
                print("El pasajero mas joven del vuelo " + str(a) + " es: ")
                print(EncontrarPasFecha(item.PasajeroJoven()).Nombre + " " +
                      EncontrarPasFecha(item.PasajeroJoven()).Apellido + " " + EncontrarPasFecha(item.PasajeroJoven()).Dni)
                print(" ")
                a+=1
            print("Escriba salir para continuar")
            Salir = input()
            while Salir != "salir":
                print("INGRESE SALIR")
                Salir = input()
        elif Elegir == "3":
            for item in Vuelos:
                if not item.TripulacionMin():
                    print("El vuelo con destino a " + item.Destino + " no cumple con la tripulacion necesaria para volar")
            print("Escriba salir para continuar")
            Salir = input()
            while Salir != "salir":
                print("INGRESE SALIR")
                Salir = input()
        elif Elegir == "4":
            b = 1
            for item in Vuelos:
                print("En el vuelo " + str(b) + " las personas no autorizadas son: ")
                for item2 in item.Colados():
                    print(item2)
                b += 1
            print("Escriba salir para continuar")
            Salir = input()
            while Salir != "salir":
                print("INGRESE SALIR")
                Salir = input()
        elif Elegir == "5":
            if len(VuelosPorDia()) == 0:
                print("No hay tripulantes que viajen mas de una vez por dia")
            for item in VuelosPorDia():
                print(item.Nombre)
                print(item.Dni)
            print("Escriba salir para continuar")
            Salir = input()
            os.system('clear')
        elif Elegir == "6":
            Ejercicio_6()
            print("Escriba salir para continuar")
            Salir = input()
            while Salir != "salir":
                print("INGRESE SALIR")
                Salir = input()
        elif Elegir == "salir":
            break
        else:
            while int(Elegir) > 6 and int(Elegir) < 1 or Elegir != "salir":
                print("Elija una opcion correcta")
                Elegir = input()
Menu()
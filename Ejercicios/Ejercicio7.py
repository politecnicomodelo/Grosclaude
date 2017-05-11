from Ejercicio7classes.Profesor import Profesor
from Ejercicio7classes.Alumno import Alumno
from datetime import datetime
Alumnos=[]
Profesores=[]
Platos=[]
Pedidos=[]
def InsertarNombre():
    print("Inserte nombre")
    return input()

def InsertarApellido():
    print("Inserte apellido")
    return input()

def InsertarDni():
    print("Inserte dni")
    return input()

def InsertarDivision():
    print("Inserte division")
    return input()

def InsertarDescuento():
    print("Inserte descuento")
    return input()

def AgregarAlumno():
    a=Alumno(InsertarNombre(),InsertarApellido(),InsertarDivision(),InsertarDni())
    Alumnos.append(a)

def ModificarAlumno():
    Alumnos[EncontrarAlumno(InsertarDni())].ModifPersona(InsertarNombre(), InsertarApellido(), InsertarDni(),InsertarDivision())
    a = Alumno(InsertarNombre(), InsertarApellido(), InsertarDivision(), InsertarDni())

def EncontrarPlatos(n):
    for item in Platos:
        if item.nombre == n:
            return item

def EncontrarAlumno(dni):
    a=0
    for item in Alumnos:
        if item.dni == dni:
            return a
        a+=1

def EncontrarProfesor(dni):
    a=0
    for item in Profesores:
        if item.dni == dni:
            return a
        a += 1

def PlatosDeldia(h):
    for item in Pedidos:
        if item.HoraEnt == h and item.Entregado is False:
            print(item.Plato.Nombre,item.CalcularPrecio())

def Menu():
    print("1) Agregar alumno")
    print("2) Modificar alumno")
    print("3) Eliminar alumno")
    print("4) Agregar profesor")
    print("5) Modificar profesor")
    print("6) Eliminar profesor")
    print("7) Agregar plato")
    print("8) Modificar plato")
    print("9) Eliminar plato")
    print("10) Agregar pedido")
    print("11) Modificar pedido")
    print("12) Eliminar pedido")
    print("13) Platos del dia")
    opcion=input()
    if opcion == 1:
        AgregarPersona()

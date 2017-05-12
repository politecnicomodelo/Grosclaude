from Ejercicio7classes.Profesor import Profesor
from Ejercicio7classes.Alumno import Alumno
from Ejercicio7classes.Plato import Plato
from Ejercicio7classes.Pedido import Pedido
from datetime import datetime
from datetime import date

Alumnos = []
Profesores = []
Platos = []
Pedidos = []



def Cargar():
    CargarAlumnos()
    CargarProfesores()
    CargarPlatos()
    CargarPedidos()

def CargarAlumnos():
    a = Alumno
    with open("Alumnos.txt","w+") as line:
        for item in line:
            if line == " ":
                continue
            else:
                l = item.split("|")
            a.Nombre = l[0]
            a.Apellido = l[1]
            a.dni = l[2]
            a.Division = l[3]
            Alumnos.append(a)

def CargarProfesores():
    a = Profesor
    with open("Profesores.txt","w+") as line:
        for item in line:
            if line == " ":
                continue
            else:
                l = item.split("|")
            a.Nombre = l[0]
            a.Apellido = l[1]
            a.dni = l[2]
            a.Descuento = l[3]
            Profesores.append(a)

def CargarPlatos():
    a = Plato
    with open("Platos.txt","w+") as line:
        for item in line:
            if line == " ":
                continue
            else:
                l = item.split("|")
            a.Nombre = l[0]
            a.Precio = int(l[1])
            Platos.append(a)

def CargarPedidos():
    a = Pedido
    with open("Pedidos.txt","w+") as line:
        for item in line:
            if line == " ":
                continue
            else:
                l = item.split("|")
            a.FechaCreacion = date(l[0])
            if EncontrarAlumno():
                if EncontrarProfesor() != None:
                    a.Persona = Profesores[EncontrarProfesor(l[1])]
            a.Persona = Alumnos[EncontrarAlumno(l[1])]

            a.FechaEntrega = date(l[2])
            a.Plato = l[3]
            a.Entregado = l[4]
            Pedidos.append(a)


Cargar()


def EncontrarPedido():
    d = input("Inserte dni de la persona")
    p = input("Inserte nombre del plato")
    f = datetime.datetime.strptime(input("Ingrese fecha de creacion"),"%d-%m-%Y").date()
    a = 0
    for item in Pedidos:
        if item.Persona.dni == d and item.FechaCreacion == f and item.Plato.Nombre == p:
            return a
        a += 1


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
    return None


def EncontrarProfesor(dni):
    a=0
    for item in Profesores:
        if item.dni == dni:
            return a
        a += 1


def AgregarAlumno():
    a=Alumno(input("Inserte nombre")
             ,input("Inserte apellido")
             ,input("Inserte division")
             ,input("Inserte Dni"))
    Alumnos.append(a)


def ModificarAlumno():
    Alumnos[EncontrarAlumno(input("Inserte dni del alumno"))].ModifPersona(
                            input("Inserte nuevo nombre")
                            ,input("Inserte nuevo apellido")
                            ,input("Inserte nueva division"))


def AgregarProfesor():
    a = Profesor(input("Inserte nombre")
                 ,input("Inserte apellido")
                 ,input("Inserte Dni"))
    Profesores.append(a)


def ModificarProfesor():
    Profesores[EncontrarProfesor(input("Inserte Dni actual"))].ModifPersona(
                                input("Insertar nuevo nombre")
                                ,input("Insertar nuevo apellido")
                                ,input("Insertar nuevo decuento"))


def AgregarPlato():
    input("Inserte precio")
    Platos.append(Plato(input("Inserte nombre"),input("Inserte precio")))


def ModificarPlato():
    print("Inserte precio")
    b = input()
    Platos[EncontrarPlatos(input("Inserte nombre"))].ModifPlato(
                            input("Insertar nuevo nombre")
                            ,input("Insertar nuevo precio"))


def AgregarPedido():
    f = datetime.datetime.strptime(input("Ingrese fecha de creacion"),"%d-%m-%Y").date()
    h = datetime.datetime.strptime(input("Ingrese fecha de entrega"),"%d-%m-%Y").date()
    p = input("Ingrese Dni")
    if EncontrarAlumno(p):
        if EncontrarProfesor(p):
            print("No se encontro esa persona")
        else:
            p = Profesores(EncontrarProfesor(p))
    else:
        p=Alumnos(EncontrarAlumno(p))
    Pedidos.append(Pedido(f,p, h,Platos[EncontrarPlatos(input("Insertar nombre del plato"))]))


def ModificarPedido():
    f = datetime.datetime.strptime(input("Ingrese fecha de creacion"), "%d-%m-%Y").date()
    h = datetime.datetime.strptime(input("Ingrese fecha de entrega"), "%d-%m-%Y").date()
    p = input("Ingrese Dni")
    n = input("Insertar nombre del plato")
    e = input("Ya se entrego?")
    if EncontrarAlumno(p):
        if EncontrarProfesor(p):
            print("No se encontro esa persona")
        else:
            p = Profesores(EncontrarProfesor(p))
    else:
        p=Alumnos(EncontrarAlumno(p))
    Pedidos[EncontrarPedido()].ModifPedido(f,p,h,Platos[EncontrarPlatos(n)],e)


def PlatosDeldia(h):
    for item in Pedidos:
        if item.HoraEnt == h and item.Entregado is False:
            print(item.Plato.Nombre,item.CalcularPrecio())


def Menu():
    while(True):
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
        print("14) Salir")
        opcion = int(input())
        if opcion == 1:
            AgregarAlumno()
        elif opcion == 2:
            ModificarAlumno()
        elif opcion == 3:
            del (Alumnos[EncontrarAlumno(input("Ingresar Dni"))])
        elif opcion == 4:
            AgregarProfesor()
        elif opcion == 5:
            ModificarProfesor()
        elif opcion == 6:
            del (Profesores[EncontrarProfesor(input("Ingresar Dni"))])
        elif opcion == 7:
            AgregarPlato()
        elif opcion == 8:
            ModificarPlato()
        elif opcion == 9:
            del (Platos[EncontrarPlatos(input("Ingresar nombre del plato"))])
        elif opcion == 10:
            AgregarPedido()
        elif opcion == 11:
            ModificarPedido()
        elif opcion == 12:
            del (Pedidos[EncontrarPedido()])
        elif opcion == 13:
            PlatosDeldia(datetime.datetime.strptime(input("Ingrese fecha"), "%d-%m-%Y").date())
        elif opcion == 14:
            break


def GuardarAlumnos():
    with open("Alumnos.txt", "w") as f:
        for item in Alumnos:
            f.write(item.Nombre
                    +"|"+item.Apellido
                    +"|"+item.dni
                    +"|"+item.Division
                    +" \n")


def GuardarProfesores():
    with open("Profesores.txt", "w") as f:
        for item in Profesores:
            f.write(item.Nombre
                    +"|"+item.Apellido
                    +"|"+item.dni
                    +"|"+item.Descuento
                    +"\n")


def GuardarPlatos():
    with open("Platos.txt", "w") as f:
        for item in Platos:
            f.write(item.Nombre
                    +"|"+item.Precio
                    +"\n")


def GuardarPedidos():
    with open("Pedidos.txt", "w") as f:
        for item in Pedidos:
            f.write(item.FechaCreacion
                    +"|"+item.Persona.dni
                    +"|"+item.HoraEnt
                    +"|"+item.Plato.Nombre
                    +"|"+item.Entregado+"\n")
def Guardar():
    GuardarAlumnos()
    GuardarProfesores()
    GuardarPlatos()
    GuardarPedidos()

Menu()
Guardar()
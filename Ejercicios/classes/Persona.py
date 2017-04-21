class Persona(object):
    Nombre = ""
    Apellido = ""
    FechaNac = None

    def __init__(self):
        self.ListaControl = []

    def SetPersona(self,n,a,f):
        self.Nombre = n
        self.Apellido = a
        self.FechaNac = f

    def AniadirControl(self,c):
        self.ListaControl.append(c)

    def BuscarControl(self,f):
        for item in self.ListaControl:
            if item.Fecha==f:
                return item.MostrarControl()

    def Promedio(self,y):
        peso=0
        altura=0
        c=0
        for item in self.ListaControl:
            if item.Fecha.year==y:
                peso += item.Peso
                altura += item.Altura
                c +=1
        return peso/c, altura/c

    def Crecimiento(self,a):
        for item in self.ListaControl:
            if item.Fecha.year==a:
                for item2 in self.ListaControl:
                    if item2.Fecha.year==(a+1)and item2.Fecha.month==item.Fecha.month and item2.Fecha.day==item.Fecha.day:
                        return (item2.Altura*100/item.Altura)-100,1

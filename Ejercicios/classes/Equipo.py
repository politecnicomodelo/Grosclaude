
class Equipo(object):
    nombre=""
    capitan=None
    listaJugadores=[]
    barrio=""

    def __init__(self):
        self.listaJugadores=[]
        self.disponibilidad = [[False, False, False],[False, False, False],[False, False, False],[False, False, False],[False, False, False],[False, False, False]]

    def setNombre(self,n):
        self.nombre=n

    def setCapitan(self,cap):
        if cap in self.listaJugadores:
            self.capitan=cap

    def setBarrio(self,n):
        self.barrio=n

    def agregarJugador(self,j):
        for item in self.listaJugadores:
            if item.nroCamiseta == j.nroCamiseta:
                return False
        self.listaJugadores.append(j)
        return True

    def modifDisponibilidad(self,dia,turno,activo):
        self.disponibilidad[dia][turno]=activo

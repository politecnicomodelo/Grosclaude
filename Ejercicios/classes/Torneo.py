from .Partido import Partido

class Torneo(object):
    listaEquipos=[]
    listaPartidos=[]

    def __init__(self):
        self.listaEquipos=[]
        self.listaPartidos=[]

    def agregarEquipo(self,e):
        self.listaEquipos.append(e)

    def organizarFixture(self):
        self.encontrarHorario()

    def Disponible(self, equipo, dia, turno):
        for item in self.listaPartidos:
            if equipo == item.Equipo1.nombre or equipo == item.Equipo2.nombre:
                if item.Dia == dia and item.Turno == turno:
                    return False
                else:
                    return True
        return True

    def encontrarCoincidencia(self, item1,dia, turno):
        for item in self.listaEquipos:
            if item.disponibilidad[dia][turno] == True and not item.nombre == item1:
                if self.Disponible(item,dia,turno)==True and self.yajugaron(item1.nombre,item.nombre) == False:
                    return item, True
                else:
                    return item,False

    def encontrarHorario(self):
        for item in self.listaEquipos:
            for item2 in range(6):
                for item3 in range(3):
                    if item.disponibilidad[item2][item3] == True:
                        if self.Disponible(item,item2,item3)==True:
                            equipo, coincide=self.encontrarCoincidencia(item,item2,item3)
                            if coincide == True:
                                self.crearPartido(item,equipo,item2,item3)

    def crearPartido(self,equipo1,equipo2,dia,turno):
        partido = Partido()
        partido.Dia=dia
        partido.Turno=turno
        partido.Equipo1=equipo1
        partido.Equipo2=equipo2
        self.listaPartidos.append(partido)

    def yajugaron(self,equipo1,equipo2):
        for item in self.listaPartidos:
            if (item.Equipo1.nombre == equipo1 and item.Equipo2.nombre == equipo2) or (item.Equipo1.nombre == equipo2 and item.Equipo2.nombre == equipo1):
                return True
            else:
                return False








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

    def encontrarCoincidencia(self, item1,dia, turno):
        for item in self.listaEquipos:
            if item.disponibilidad[dia][turno] == True and item.nombre!=item1.nombre:
                return item, True

    def encontrarHorario(self):
        for item in self.listaEquipos:
            for item2 in range(6):
                for item3 in range(3):
                    if item.disponibilidad[item2][item3] == True:
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






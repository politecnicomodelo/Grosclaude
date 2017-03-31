class Torneo(object):
    listaEquipos=[]
    listaPartidos=[]

    def __init__(self):
        self.listaEquipos=[]
        self.listaPartidos=[]

    def agregarEquipo(self,e):
        self.listaEquipos.append(e)

    def organizarFixture(self):

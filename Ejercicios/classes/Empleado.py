class Empleado(object):
    Nombre = ""
    Apellido = ""
    Telefono = ""
    FechaNac = None

    def __init__(self):
        DiasDisp = []
        Asistencia = []

    def SetEmpleado(self,nom,apel,tel,nac):
        self.Nombre = nom
        self.Apellido = apel
        self.Telefono = tel
        self.FechaNac = nac

    def SetDisponibilidad(self,dis):
        self.Disponibilidad = dis

    def SetAsistencia(self,date):
        self.Asistencia.append(date)

    def PorcentajeAsistencia(self,mes,a):
        b=0
        c=0
        for item in self.Asistencia:
            if item.month == mes and item.year == a:
                b+=1
        for item2 in self.Disponibilidad:
            if item2:
                c+=1
        return b*100/c*4






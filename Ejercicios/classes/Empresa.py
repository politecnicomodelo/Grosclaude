class Empresa(object):

    def __init__(self):
        self.ListaEmpleados = []

    def AgregarEmpleado(self,em):
        self.ListaEmpleado.append(em)

    def PorcentajeAsis(self,month,year):
        a=0
        for item in self.ListaEmpleados:
            a += item.PorcentajeAsistencia(month,year)
        return a/len(self.ListaEmpleados)
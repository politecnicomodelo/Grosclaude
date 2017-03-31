from .Materia import Materia
class Alumno(object):
    nombre=""
    apellido=""
    fecha_nac=None
    lista_de_notas=[]
    Materias=[]
    def __init__(self):
        self.lista_de_notas=[]


    def setNombre(self,n):
        self.nombre=n

    def setApellido(self,t):
        self.apellido=t

    def setFecha_nac(self,fecha):
        self.fecha_nac=fecha

    def agregarMateria(self,g):
        nuevaMateria = Materia()
        nuevaMateria.nombreMateria(g)
        self.Materias.append(nuevaMateria)

    def encontrarMateria(self, mat):
        for item in self.Materias:
            if item.nombre == mat:
                return item

    def agregarNotasMateria(self,mat,i):
        self.encontrarMateria(mat).lista_de_notas.append(i)

    def promMateria(self,n):
        if len(self.encontrarMateria(n).lista_de_notas)==0:
            return 0
        return float(sum(self.encontrarMateria(n).lista_de_notas)/len(self.encontrarMateria(n).lista_de_notas))

    def promAlumno(self):
        a=0
        x=len(self.Materias)
        for item in self.Materias:
            if self.promMateria(item.nombre)==0:
                x=x-1

            a += self.promMateria(item.nombre)
            print(x)

        return float(a/x)

    def menorYmayorProm(self):
        a=[]
        for item in self.Materias:
            a.append(item.promMateria(item.nombre))
        return min(a),max(a)


    def agregarNota(self,h):
        self.lista_de_notas.append(h)

    def menor_nota(self):
        return min(self.lista_de_notas)

    def mayor_nota(self):
        return max(self.lista_de_notas)

    def prom(self):
        return sum(self.lista_de_notas)/len(self.lista_de_notas)


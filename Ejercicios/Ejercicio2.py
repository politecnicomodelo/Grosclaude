from classes.Alumno import Alumno
from classes.Materia import Materia

miAlumno=Alumno()
miAlumno.agregarMateria("Matematica")
miAlumno.agregarMateria("Castellano")
miAlumno.agregarMateria("Bio")


miAlumno.agregarNotasMateria("Matematica",3)
miAlumno.agregarNotasMateria("Matematica",5)

miAlumno.agregarNotasMateria("Castellano",8)

print(miAlumno.Materias[0].lista_de_notas[0])
print(miAlumno.Materias[1].lista_de_notas[0])
print(miAlumno.promAlumno())


from classes.Alumno import Alumno
from datetime import date

miAlumno=Alumno()
miAlumno.setNombre("vitti")
miAlumno.setApellido("chuaman")
miAlumno.setFecha_nac(date(2000,3,13))
miAlumno.agregarNota(8)
miAlumno.agregarNota(4)
print(miAlumno.menor_nota())
print(miAlumno.mayor_nota())
print(miAlumno.prom())

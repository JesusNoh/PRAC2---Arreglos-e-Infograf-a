import numpy as np

def generar_datos(num_alumnos, num_materias):
    return np.random.randint(0, 101, size=(num_alumnos, num_materias))

def buscar_calificacion(matriz, alumno, materia):
    if 1 <= alumno <= matriz.shape[0] and 1 <= materia <= matriz.shape[1]:
        return matriz[alumno-1, materia-1]
    else:
        return "Número de alumno o materia fuera de rango."

num_alumnos = int(input("Ingrese el número de alumnos: "))
num_materias = int(input("Ingrese el número de materias: "))

matriz = generar_datos(num_alumnos, num_materias)
print(matriz)

alumno = int(input("Ingrese el número del alumno (1-{}): ".format(num_alumnos)))
materia = int(input("Ingrese el número de la materia (1-{}): ".format(num_materias)))

calificacion = buscar_calificacion(matriz, alumno, materia)
print(f"La calificación del alumno {alumno} en la materia {materia} es: {calificacion}")

for alumnos, materias in [(10000, 100), (100000, 500), (1000000, 1000)]:
    matriz_prueba = generar_datos(alumnos, materias)
    print(f"Prueba con {alumnos} alumnos y {materias} materias completada.")

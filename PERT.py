import math

class Actividad:
    def __init__(self, nombre, predecesores, tiempo_optimista, tiempo_mas_probable, tiempo_pesimista):
        self.nombre = nombre
        self.predecesores = predecesores
        self.tiempo_optimista = tiempo_optimista
        self.tiempo_mas_probable = tiempo_mas_probable
        self.tiempo_pesimista = tiempo_pesimista
        self.tiempo_esperado = (tiempo_optimista + 4 * tiempo_mas_probable + tiempo_pesimista) / 6
        self.varianza = ((tiempo_pesimista - tiempo_optimista) / 6) ** 2
        self.desviacion_estandar = math.sqrt(self.varianza)

# Crear actividades
actividades = [
    Actividad("A", [], 2, 4, 6),
    Actividad("B", ["A"], 1, 3, 5),
    Actividad("C", ["A"], 3, 5, 7),
    Actividad("D", ["B", "C"], 2, 4, 6),
    Actividad("E", ["D"], 1, 3, 5),
    Actividad("F", ["D"], 2, 4, 6),
    Actividad("G", ["E", "F"], 3, 5, 7)
]

# Calcular tiempos y estadísticas
for actividad in actividades:
    print(f"Actividad: {actividad.nombre}")
    print(f"Predecesores: {actividad.predecesores}")
    print(f"Tiempo optimista: {actividad.tiempo_optimista}")
    print(f"Tiempo más probable: {actividad.tiempo_mas_probable}")
    print(f"Tiempo pesimista: {actividad.tiempo_pesimista}")
    print(f"Tiempo esperado: {actividad.tiempo_esperado}")
    print(f"Varianza: {actividad.varianza}")
    print(f"Desviación estándar: {actividad.desviacion_estandar}")
    print()


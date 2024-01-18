import tkinter as tk
from tkinter import simpledialog, messagebox
import numpy as np


def obtener_utilidades():
    num_suceso = simpledialog.askinteger("Input", "Ingrese el número de sucesos:")
    num_alternativas = simpledialog.askinteger("Input", "Ingrese el número de alternativas:")

    matriz_utilidades = []

    for i in range(num_suceso):
        fila_utilidades = []

        for j in range(num_alternativas):
            utilidad = simpledialog.askfloat(f"Input", f"Ingrese la utilidad para la alternativa {i + 1} en el suceso {j + 1}:")
            fila_utilidades.append(utilidad)

        matriz_utilidades.append(fila_utilidades)

    return matriz_utilidades, num_suceso, num_alternativas

def mostrar_matriz(matriz_utilidades):
    messagebox.showinfo("Matriz de Utilidades", "\n".join(["\t".join(map(str, fila)) for fila in matriz_utilidades]))

def criterio_wald(matriz_utilidades, num_suceso):
    maximos_minimos = [min(fila) for fila in matriz_utilidades]
    decision_optima_wald = maximos_minimos.index(max(maximos_minimos)) + 1
    utilidades_peor_escenario = [maximos_minimos[i] for i in range(num_suceso)]
    return decision_optima_wald, utilidades_peor_escenario

def criterio_optimista(matriz_utilidades, num_suceso):
    maximos_maximos = [max(fila) for fila in matriz_utilidades]
    decision_optima_optimista = maximos_maximos.index(max(maximos_maximos)) + 1
    utilidades_mejor_escenario = [maximos_maximos[i] for i in range(num_suceso)]
    return decision_optima_optimista, utilidades_mejor_escenario

def criterio_laplace(matriz_utilidades, num_suceso, num_alternativas):
    probabilidad_uniforme = 1 / num_alternativas
    utilidades_promedio = [sum(fila) * probabilidad_uniforme for fila in matriz_utilidades]
    decision_optima_laplace = utilidades_promedio.index(max(utilidades_promedio)) + 1
    return decision_optima_laplace, utilidades_promedio

def criterio_hurwicz(matriz_utilidades, num_suceso, alfa):
    utilidades_hurwicz = [alfa * max(fila) + (1 - alfa) * min(fila) for fila in matriz_utilidades]
    decision_optima_hurwicz = utilidades_hurwicz.index(max(utilidades_hurwicz)) + 1
    return decision_optima_hurwicz, utilidades_hurwicz

def criterio_savage(matriz_utilidades, num_suceso):
    maximos_por_columna = np.amax(matriz_utilidades, axis=0)
    matriz_resultante = maximos_por_columna - matriz_utilidades
    # Obtener el máximo de cada fila en la matriz resultante
    maximos_por_fila = np.amax(matriz_resultante, axis=1)   
    # Obtener la posición de la fila que contiene el máximo
    decision_savage = np.argmax(maximos_por_fila)
    return decision_savage, maximos_por_fila
    
def main():
    matriz_utilidades, num_suceso, num_alternativas = obtener_utilidades()

    mostrar_matriz(matriz_utilidades)

    decision_wald, utilidades_wald = criterio_wald(matriz_utilidades, num_suceso)
    messagebox.showinfo("Criterio de Wald", f"Decision Pesimista según Wald: alternativa {decision_wald}\nUtilidad Esperada en el Peor Escenario para cada Decisión: {utilidades_wald}")

    decision_optimista, utilidades_optimista = criterio_optimista(matriz_utilidades, num_suceso)
    messagebox.showinfo("Criterio Optimista", f"Decision Óptima : alternativa {decision_optimista}\nUtilidad Esperada en el Mejor Escenario para cada Decisión: {utilidades_optimista}")

    decision_laplace, utilidades_laplace = criterio_laplace(matriz_utilidades, num_suceso, num_alternativas)
    messagebox.showinfo("Criterio de Laplace", f"Decision según Laplace: alternativa {decision_laplace}\nUtilidad Esperada Promedio para cada Decisión: {utilidades_laplace}")

    alfa = simpledialog.askfloat("Input", "Ingrese el valor de alfa para el criterio de Hurwicz (entre 0 y 1):")
    if 0 <= alfa <= 1:
        decision_hurwicz, utilidades_hurwicz = criterio_hurwicz(matriz_utilidades, num_suceso, alfa)
        messagebox.showinfo("Criterio de Hurwicz", f"Decision según Hurwicz: alternativa {decision_hurwicz}\nUtilidad Esperada para cada Decisión (alfa = {alfa}): {utilidades_hurwicz}")
    else:
        messagebox.showerror("Error", "El valor de alfa debe estar entre 0 y 1.")

    decision_savage, maximos_lamentos = criterio_savage(matriz_utilidades, num_suceso)
    messagebox.showinfo("Criterio de Savage", f"Decision según Savage: alternativa {decision_savage}\nLamento Máximo para cada Decisión: {maximos_lamentos}")

if __name__ == "__main__":
    main()

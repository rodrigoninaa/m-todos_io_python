import tkinter as tk
from tkinter import simpledialog, messagebox

resultados_esperados = []

def calcular_valor_esperado(probabilidades, ganancias):
    if len(probabilidades) != len(ganancias):
        raise ValueError("La longitud de las listas de probabilidades y ganancias debe ser la misma.")
    
    valor_esperado = sum(p * g for p, g in zip(probabilidades, ganancias))
    return valor_esperado

def ingresar_datos_decision():
    num_decisiones = simpledialog.askinteger("Número de decisiones", "Ingrese el número de probabilidades:")
    decisiones = []

    for i in range(num_decisiones):
        prob = simpledialog.askfloat(f"Probabilidad para la decisión {i + 1}", f"Ingrese la probabilidad para la decisión {i + 1}:")
        ganancia = simpledialog.askfloat(f"Ganancia para la decisión {i + 1}", f"Ingrese la ganancia para la decisión {i + 1}:")
        decisiones.append((prob, ganancia))

    probabilidades, ganancias = zip(*decisiones)
    valor_esperado = calcular_valor_esperado(probabilidades, ganancias)
    resultados_esperados.append(valor_esperado)
    messagebox.showinfo("Resultado", f"El valor esperado es: {valor_esperado}")

def mostrar_resultado(opcion):
    if opcion == "max":
        valor_maximo = max(resultados_esperados)
        posicion_maximo = resultados_esperados.index(valor_maximo)
        messagebox.showinfo("Resultado", f"El valor máximo del array es: {valor_maximo}\nTomar la decisión # {posicion_maximo + 1}")
    elif opcion == "min":
        valor_min = min(resultados_esperados)
        posicion_minimo = resultados_esperados.index(valor_min)
        messagebox.showinfo("Resultado", f"El valor mínimo del array es: {valor_min}\nTomar la decisión # {posicion_minimo + 1}")

def main():
    # Solicitar al usuario el número de decisiones
    num_deci = simpledialog.askinteger("Número de decisiones totales", "Ingrese el número de decisiones totales:")

    for _ in range(num_deci):
        ingresar_datos_decision()

    opcion = simpledialog.askstring("Max o Min", "Elige entre 'max' o 'min':")
    mostrar_resultado(opcion)

if __name__ == "__main__":
    main()

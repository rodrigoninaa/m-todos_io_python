import numpy as np

resultados_esperados = []
id_decision = []
def calcular_valor_esperado(probabilidades, ganancias):
    if len(probabilidades) != len(ganancias):
        raise ValueError("La longitud de las listas de probabilidades y ganancias debe ser la misma.")
    
    valor_esperado = sum(p * g for p, g in zip(probabilidades, ganancias))
    return valor_esperado

def main():
    # Solicitar al usuario el número de decisiones
    num_deci = int(input("Ingrese # decisiones: "))
    for i in range (num_deci):

        num_decisiones = int(input("Ingrese el número de probabilidades: "))

        decisiones = []

        # Solicitar probabilidades y ganancias para cada decisión
        for i in range(num_decisiones):
            prob = float(input(f"Ingrese la probabilidad para la decisión {i + 1}: "))
            ganancia = float(input(f"Ingrese la ganancia para la decisión {i + 1}: "))

            decisiones.append((prob, ganancia))

        # Calcular y mostrar el valor esperado
        probabilidades, ganancias = zip(*decisiones)
        valor_esperado = calcular_valor_esperado(probabilidades, ganancias)
        resultados_esperados.append(valor_esperado)
        print(f"El valor esperado es: {valor_esperado}")

    opcion = input("Elige entre max o min: ")
    if(opcion == "max" ):
        valor_maximo = max(resultados_esperados)
        posicion_maximo = resultados_esperados.index(valor_maximo)
        # Mostrar el resultado
        print(f"El valor máximo del array es: {valor_maximo}")
        print(f"Tomar la decision # {posicion_maximo+1}")
    elif(opcion == "min"):
        valor_min = min(resultados_esperados)
        posicion_minimo = resultados_esperados.index(valor_min)
        # Mostrar el resultado
        print(f"El valor máximo del array es: {valor_min}")
        print(f"Tomar la decision # {posicion_minimo+1}")

if __name__ == "__main__":
    main()

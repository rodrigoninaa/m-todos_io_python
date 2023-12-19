opcion = int(input("arbol de decision[1] o bajo incertidumbre[2]??:  "))
if(opcion == 1):
    num_decisiones = int(input("Ingrese el número de decisiones: "))
    num_estados = int(input("Ingrese el número de estados: "))

    arreglo_decisiones=[]
    arreglo_estados=[]

    for i in range(num_decisiones):
        decision = float(input(f"Ingrese decisión {i + 1}: "))
        arreglo_decisiones.append(decision)
    for i in range(num_estados):
        estado = float(input(f"Ingrese estado {i + 1}: "))
        arreglo_estados.append(estado)

    # Multiplicar cada elemento del arreglo de decisiones por cada estado y sumar los resultados
    resultados = []

    for decision in arreglo_decisiones:
        suma_resultados = sum(decision * estado for estado in arreglo_estados)
        resultados.append(suma_resultados)

    print("Resultados:", resultados)

    # Elegir el mayor o menor según se pida
    opcion = input("¿Desea encontrar el resultado máximo o mínimo? (max/min): ").lower()

    if opcion == "max":
        indice_max = resultados.index(max(resultados))
        print(f"La decisión óptima es la número {indice_max + 1} con un resultado máximo de {max(resultados)}.")

    elif opcion == "min":
        indice_min = resultados.index(min(resultados))
        print(f"La decisión óptima es la número {indice_min + 1} con un resultado mínimo de {min(resultados)}.")

    else:
        print("Opción no válida. Por favor, ingrese 'max' o 'min'.")
    

elif(opcion == 2):
    # Solicitar al usuario el número de decisiones y eventos inciertos
    num_suceso = int(input("Ingrese el número de sucesos: "))
    num_alternativas = int(input("Ingrese el número de alternativa: "))

    # Inicializar una matriz para almacenar las utilidades de cada decisión y evento
    matriz_utilidades = []

    # Construir la matriz con un bucle for
    for i in range(num_suceso):
        fila_utilidades = []  # Inicializar una fila para cada decisión

        for j in range(num_alternativas):
            # Solicitar al usuario la utilidad para cada combinación de decisión y evento
            utilidad = float(input(f"Ingrese la utilidad para la alternativa {i + 1} en el suceso {j + 1}: "))
            fila_utilidades.append(utilidad)

        matriz_utilidades.append(fila_utilidades)

    # Mostrar la matriz resultante
    print("\nMatriz de Utilidades:")
    for fila in matriz_utilidades:
        print(fila)

    # Aplicar el criterio de Wald
    maximos_minimos = [min(fila) for fila in matriz_utilidades]
    decision_optima_wald = maximos_minimos.index(max(maximos_minimos)) + 1

    # Calcular la utilidad esperada en el peor escenario para cada decisión
    utilidades_peor_escenario = [maximos_minimos[i] for i in range(num_suceso)]

    # Mostrar resultados
    print(f"\nCriterio de Wald:")
    print(f"Decision Óptima según Wald: alternativa {decision_optima_wald}")
    print(f"Utilidad Esperada en el Peor Escenario para cada Decisión: {utilidades_peor_escenario}")

    # Aplicar el criterio optimista
    maximos_maximos = [max(fila) for fila in matriz_utilidades]
    decision_optima_optimista = maximos_maximos.index(max(maximos_maximos)) + 1

    # Calcular la utilidad esperada en el mejor escenario para cada decisión
    utilidades_mejor_escenario = [maximos_maximos[i] for i in range(num_suceso)]

    # Mostrar resultados
    print(f"\nCriterio Optimista:")
    print(f"Decision Óptima según Optimista: alternativa {decision_optima_optimista}")
    print(f"Utilidad Esperada en el Mejor Escenario para cada Decisión: {utilidades_mejor_escenario}")

    # Aplicar el criterio de Laplace
    probabilidad_uniforme = 1 / num_alternativas
    utilidades_promedio = [sum(fila) * probabilidad_uniforme for fila in matriz_utilidades]
    decision_optima_laplace = utilidades_promedio.index(max(utilidades_promedio)) + 1

    # Mostrar resultados
    print(f"\nCriterio de Laplace:")
    print(f"Decision Óptima según Laplace: alternativa {decision_optima_laplace}")
    print(f"Utilidad Esperada Promedio para cada Decisión: {utilidades_promedio}")

    # Solicitar al usuario el valor de peso (alfa) para el criterio de Hurwicz
    alfa = float(input("Ingrese el valor de alfa para el criterio de Hurwicz (entre 0 y 1): "))

    # Validar que alfa esté en el rango correcto
    if 0 <= alfa <= 1:
        # Aplicar el criterio de Hurwicz
        utilidades_hurwicz = [alfa * max(fila) + (1 - alfa) * min(fila) for fila in matriz_utilidades]
        decision_optima_hurwicz = utilidades_hurwicz.index(max(utilidades_hurwicz)) + 1

        # Mostrar resultados
        print(f"\nCriterio de Hurwicz:")
        print(f"Decision Óptima según Hurwicz: alternativa {decision_optima_hurwicz}")
        print(f"Utilidad Esperada para cada Decisión (alfa = {alfa}): {utilidades_hurwicz}")
    else:
        print("Error: El valor de alfa debe estar entre 0 y 1.")

    # Calcular el máximo lamento para cada decisión
    maximos_lamentos = [max(fila) - min(fila) for fila in matriz_utilidades]

    # Encontrar la decisión que minimiza el máximo lamento
    decision_optima_savage = maximos_lamentos.index(min(maximos_lamentos)) + 1

    # Mostrar resultados
    print(f"\nCriterio de Savage:")
    print(f"Decision Óptima según Savage: alternativa {decision_optima_savage}")
    print(f"Lamento Máximo para cada Decisión: {maximos_lamentos}")



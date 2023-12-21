import tkinter as tk
from tkinter import simpledialog, Scrollbar, Canvas

def obtener_tamano_matriz():
    tamano = simpledialog.askinteger("Tamaño de la Matriz", "Ingrese el numero de criterios (n):", minvalue=1)
    return tamano

def obtener_numero_alternativas():
    nalt = simpledialog.askinteger("Número de Alternativas", "Ingrese el número de alternativas (nalt):", minvalue=1)
    return nalt

def crear_matriz(tamano, nalt):
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Matrices")

    # Crear un lienzo y una barra de desplazamiento vertical
    canvas = Canvas(ventana)
    scrollbar = Scrollbar(ventana, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Marco que contendrá las matrices
    frame_matrices = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame_matrices, anchor="nw")

    resultados = []

    # Crear la matriz "Criterios"
    titulo_criterios = "Criterios"
    resultados_criterios = crear_matriz_individual(frame_matrices, tamano, 0, titulo_criterios)
    resultados.append((titulo_criterios, resultados_criterios))

    for alt in range(1, nalt + 1):
        # Crear las demás matrices
        titulo = f"Alternativa {alt}"
        resultados_matriz = crear_matriz_individual(frame_matrices, tamano, alt, titulo)
        resultados.append((titulo, resultados_matriz))

    # Boton calcular
    boton_sumar = tk.Button(frame_matrices, text="Calcular", command=lambda: mostrar_resultados(resultados, tamano))
    boton_sumar.grid(row=(nalt + 1) * (tamano + 2) + 1, column=1, columnspan=tamano, padx=5, pady=5)

    # Ajustar el desplazamiento vertical
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Iniciar el bucle principal
    ventana.mainloop()

def crear_matriz_individual(frame_matrices, tamano, offset, titulo):
    # Etiqueta para el título de la matriz
    etiqueta_titulo = tk.Label(frame_matrices, text=titulo, font=('bold', 12))
    etiqueta_titulo.grid(row=offset * (tamano + 2) + 1, column=0, columnspan=tamano, padx=5, pady=5)

    # Etiquetas para las columnas
    columnas_etiquetas = [f"Criterio {i+1}" for i in range(tamano)]
    for j, columna in enumerate(columnas_etiquetas):
        etiqueta = tk.Label(frame_matrices, text=columna, width=12)
        etiqueta.grid(row=offset * (tamano + 2) + 2, column=j + 1, padx=2, pady=2)

    # Etiquetas para las filas
    filas_etiquetas = [f"Criterio {i+1}" for i in range(tamano)]
    for i, fila in enumerate(filas_etiquetas):
        etiqueta = tk.Label(frame_matrices, text=fila, width=12)
        etiqueta.grid(row=i + offset * (tamano + 2) + 3, column=0, padx=2, pady=2)

    # Crear la matriz de entradas
    matriz_entries = []
    for i in range(tamano):
        fila_entries = []
        for j in range(tamano):
            entry = tk.Entry(frame_matrices, width=8)
            entry.grid(row=i + offset * (tamano + 2) + 3, column=j + 1, padx=2, pady=2)
            fila_entries.append(entry)
        matriz_entries.append(fila_entries)

    return matriz_entries

def mostrar_resultados(resultados, tamano):
    # Crear la ventana para mostrar los resultados
    ventana_resultados = tk.Toplevel()
    ventana_resultados.title("Resultados")

    # Crear un lienzo y una barra de desplazamiento vertical
    canvas_resultados = Canvas(ventana_resultados)
    scrollbar_resultados = Scrollbar(ventana_resultados, orient="vertical", command=canvas_resultados.yview)
    canvas_resultados.configure(yscrollcommand=scrollbar_resultados.set)

    canvas_resultados.pack(side="left", fill="both", expand=True)
    scrollbar_resultados.pack(side="right", fill="y")

    # Marco que contendrá los resultados
    frame_resultados = tk.Frame(canvas_resultados)
    canvas_resultados.create_window((0, 0), window=frame_resultados, anchor="nw")

    resultados_finales = []

    for titulo, matriz_entries in resultados:
        # Obtener los valores de la matriz
        valores = [[float(entry.get()) for entry in fila_entries] for fila_entries in matriz_entries]

        # Calcular la suma de cada columna
        sumas_columnas = [sum(col) for col in zip(*valores)]

        # Calcular la matriz resultante
        matriz_resultante = [[valor / suma_columna for valor, suma_columna in zip(fila, sumas_columnas)] for fila in valores]

        # Calcular el promedio de cada fila en la matriz resultante
        promedio_fila = [sum(fila) / len(fila) for fila in matriz_resultante]

        # Mostrar el título de la matriz
        etiqueta_titulo = tk.Label(frame_resultados, text=f"Matriz Resultante de {titulo}:", font=('bold', 12))
        etiqueta_titulo.pack()

        # Mostrar la matriz resultante sin la primera columna
        for fila in matriz_resultante:
            etiqueta_fila = tk.Label(frame_resultados, text=[f"{valor:.3f}" for valor in fila[1:]])
            etiqueta_fila.pack()

        # Mostrar el promedio de cada fila en la matriz resultante (organizado en columnas)
        for i, valor in enumerate(promedio_fila):
            etiqueta_promedio = tk.Label(frame_resultados, text=f"Promedio Fila {i + 1}: {valor:.3f}")
            etiqueta_promedio.pack()

        # Separador
        separador = tk.Label(frame_resultados, text="\n" + "-" * 50 + "\n")
        separador.pack()

        resultados_finales.append((titulo, matriz_resultante, promedio_fila))

    # Añadir sección "Selección de la mejor alternativa"
    etiqueta_seleccion = tk.Label(frame_resultados, text="Selección de la mejor alternativa:", font=('bold', 12))
    etiqueta_seleccion.pack()

    # Crear la matriz de selección (sin la primera columna)
    matriz_seleccion = [[promedio_fila[i] for _, _, promedio_fila in resultados_finales] for i in range(tamano)]

    # Mostrar la matriz de selección (sin la primera columna)
    for fila in matriz_seleccion:
        etiqueta_fila = tk.Label(frame_resultados, text=[f"{valor:.3f}" for valor in fila[1:]])
        etiqueta_fila.pack()

    # Añadir la columna "Vector"
    etiqueta_vector = tk.Label(frame_resultados, text="Vector", font=('bold', 12))
    etiqueta_vector.pack()

    # Mostrar la primera columna de la matriz de selección
    for valor in matriz_seleccion:
        etiqueta_valor = tk.Label(frame_resultados, text=f"{valor[0]:.3f}")
        etiqueta_valor.pack()

    # Calcular el producto de la matriz de selección por el vector
    producto_vector = [sum(fila[i] * valor[0] for i, valor in enumerate(matriz_seleccion)) for fila in matriz_seleccion]

    # Añadir sección "Producto de la matriz por el vector"
    etiqueta_producto = tk.Label(frame_resultados, text="Producto de la matriz por el vector:", font=('bold', 12))
    etiqueta_producto.pack()

    # Mostrar la columna de resultados del producto
    for i, valor in enumerate(producto_vector):
        etiqueta_producto = tk.Label(frame_resultados, text=f"Resultado Fila {i + 1}: {valor:.3f}")
        etiqueta_producto.pack()

    # Encontrar el índice del máximo valor en el producto
    indice_maximo = max(range(len(producto_vector)), key=producto_vector.__getitem__)

    # Mostrar el resultado final
    etiqueta_resultado_final = tk.Label(frame_resultados, text=f"\nEl mayor resultado tiene un valor de {producto_vector[indice_maximo]:.3f}", font=('bold', 12))
    etiqueta_resultado_final.pack()

    # Ajustar el desplazamiento vertical
    canvas_resultados.update_idletasks()
    canvas_resultados.config(scrollregion=canvas_resultados.bbox("all"))

# Obtener el tamaño de la matriz y el número de alternativas
tamano_matriz = obtener_tamano_matriz()
numero_alternativas = obtener_numero_alternativas()

# Crear y mostrar las matrices
crear_matriz(tamano_matriz, numero_alternativas)

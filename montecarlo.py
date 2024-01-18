import random
import tkinter as tk
from tkinter import ttk, messagebox

pares = []
ocurrencias_dict = {}
def obtener_datos():
    cantidad_pares = int(entry_cantidad.get())

    # Crear una nueva ventana para ingresar los pares (valor, frecuencia)
    ventana_pares = tk.Toplevel(ventana)
    ventana_pares.title("Ingreso de Pares (Valor, Frecuencia)")

    # Crear etiquetas y campos de entrada dinámicamente
    etiquetas_valor = []
    entradas_valor = []
    etiquetas_frecuencia = []
    entradas_frecuencia = []

    for i in range(cantidad_pares):
        etiqueta_valor = tk.Label(ventana_pares, text=f"Valor {i + 1}:")
        etiqueta_valor.grid(row=i, column=0, padx=10, pady=10, sticky=tk.W)
        etiquetas_valor.append(etiqueta_valor)

        entrada_valor = tk.Entry(ventana_pares)
        entrada_valor.grid(row=i, column=1, padx=10, pady=10)
        entradas_valor.append(entrada_valor)

        etiqueta_frecuencia = tk.Label(ventana_pares, text=f"Frecuencia {i + 1}:")
        etiqueta_frecuencia.grid(row=i, column=2, padx=10, pady=10, sticky=tk.W)
        etiquetas_frecuencia.append(etiqueta_frecuencia)

        entrada_frecuencia = tk.Entry(ventana_pares)
        entrada_frecuencia.grid(row=i, column=3, padx=10, pady=10)
        entradas_frecuencia.append(entrada_frecuencia)

    # Función para obtener los pares (valor, frecuencia) ingresados
    def obtener_pares():
        
        for valor, frecuencia in zip(entradas_valor, entradas_frecuencia):
            valor = valor.get()
            frecuencia = frecuencia.get()
            if valor and frecuencia:
                par = (float(valor), int(frecuencia))
                pares.append(par)
            else:
                messagebox.showerror("Error", "Por favor, ingrese tanto el valor como la frecuencia para todos los pares.")
                return

        limites_superiores = mostrar_tabla(pares)
        ventana_pares.destroy()

        # Mostrar tabla de simulación
        boton_simulacion["state"] = tk.NORMAL  # Habilitar el botón de simulación
        
        def iniciar_simulacion():
            cantidad_simulaciones = int(entry_cant_simulaciones.get())
            ocurrencias_dict = mostrar_tabla_simulacion(cantidad_simulaciones, limites_superiores)
            
            mostrar_resultados_finales(pares, ocurrencias_dict)

        boton_simulacion["command"] = iniciar_simulacion


    # Botón para obtener los pares (valor, frecuencia)
    boton_obtener_pares = tk.Button(ventana_pares, text="Obtener Pares", command=obtener_pares)
    boton_obtener_pares.grid(row=cantidad_pares, column=0, columnspan=4, pady=10)

    


def mostrar_tabla(pares):
    # Crear una nueva ventana para mostrar la tabla
    ventana_tabla = tk.Toplevel(ventana)
    ventana_tabla.title("Tabla de Resultados")

    # Crear encabezados de la tabla
    encabezados = ["Valor", "Frecuencia", "Probabilidad", "Limite Inferior", "Limite Superior"]
    
    # Crear Treeview
    tree = ttk.Treeview(ventana_tabla, columns=encabezados, show="headings", height=10)

    for encabezado in encabezados:
        tree.heading(encabezado, text=encabezado)
        tree.column(encabezado, anchor=tk.CENTER)
        tree.column(encabezado, width=100)  # Ajustar el ancho de las columnas

    tree.grid(row=0, column=0, padx=10, pady=10, columnspan=5, sticky=tk.W+tk.E)

    # Calcular probabilidades y acumuladas
    total_frecuencia = sum(frecuencia for _, frecuencia in pares)
    prob_acumulada_inf = 0
    limites_superiores = []

    for i, (valor, frecuencia) in enumerate(pares):
        probabilidad = frecuencia / total_frecuencia
        prob_acumulada_sup = prob_acumulada_inf + probabilidad
        limites_superiores.append(prob_acumulada_sup)

        tree.insert("", "end", values=[valor, frecuencia, f"{probabilidad:.2f}", f"{prob_acumulada_inf:.2f}", f"{prob_acumulada_sup:.2f}"])

        prob_acumulada_inf = prob_acumulada_sup

    return limites_superiores


def mostrar_tabla_simulacion(cantidad_simulaciones, limites_superiores):
    ocurrencias_dict = {}  # Inicializar el diccionario de ocurrencias
    # Función para cerrar la ventana de simulación y retornar el diccionario de ocurrencias
    def cerrar_ventana():
        ventana_simulacion.destroy()
    # Crear una nueva ventana para mostrar la tabla de simulación
    ventana_simulacion = tk.Toplevel(ventana)
    ventana_simulacion.title("Tabla de Simulación")

    # Crear encabezados de la tabla
    encabezados_simulacion = ["N°", "Num. Aleatorio", "Valor"]
    
    # Crear Treeview
    tree_simulacion = ttk.Treeview(ventana_simulacion, columns=encabezados_simulacion, show="headings", height=10)

    for encabezado in encabezados_simulacion:
        tree_simulacion.heading(encabezado, text=encabezado)
        tree_simulacion.column(encabezado, anchor=tk.CENTER)
        tree_simulacion.column(encabezado, width=100)  # Ajustar el ancho de las columnas

    tree_simulacion.grid(row=0, column=0, padx=10, pady=10, columnspan=3, sticky=tk.W+tk.E)

    # Generar la tabla de simulación
    for i in range(cantidad_simulaciones):
        num_aleatorio = random.uniform(0, 1)

        # Comparar el número aleatorio con los valores de limites_superiores
        valor = None
        for idx, lim_sup in enumerate(limites_superiores):
            if num_aleatorio <= lim_sup:
                valor = pares[idx][0]  # Obtener el valor correspondiente
                break

        # Actualizar el diccionario de ocurrencias
        ocurrencias_dict[valor] = ocurrencias_dict.get(valor, 0) + 1

        tree_simulacion.insert("", "end", values=[i+1, f"{num_aleatorio:.2f}", valor])
    
    # Configurar el botón para cerrar la ventana
    boton_cerrar = tk.Button(ventana_simulacion, text="Cerrar", command=cerrar_ventana)
    boton_cerrar.grid(row=1, column=0, columnspan=3, pady=10)
    
    # Mostrar el diccionario de ocurrencias

    # Retornar el diccionario de ocurrencias antes de iniciar el bucle principal de la ventana
        

    # Iniciar el bucle principal de la ventana_simulacion
    ventana_simulacion.mainloop()


def mostrar_resultados_finales(pares, ocurrencias_dict):
    # Crear una nueva ventana para mostrar los resultados finales
    ventana_resultados = tk.Toplevel(ventana)
    ventana_resultados.title("Resultados Finales")

    # Crear encabezados de la tabla
    encabezados_finales = ["Valor", "Frecuencia", "Probabilidad", "Limite Inferior", "Limite Superior", "Valor * Frecuencia", "Ocurrencias", "Porcentajes", "Ocurrencias * Valor"]
    
    # Crear Treeview
    tree_finales = ttk.Treeview(ventana_resultados, columns=encabezados_finales, show="headings", height=10)

    for encabezado in encabezados_finales:
        tree_finales.heading(encabezado, text=encabezado)
        tree_finales.column(encabezado, anchor=tk.CENTER)
        tree_finales.column(encabezado, width=110)  # Ajustar el ancho de las columnas

    tree_finales.grid(row=0, column=0, padx=10, pady=10, columnspan=9, sticky=tk.W+tk.E)

    # Calcular probabilidades y acumuladas
    total_frecuencia = sum(frecuencia for _, frecuencia in pares)
    prob_acumulada_inf = 0
    for i, (valor, frecuencia) in enumerate(pares):
        probabilidad = frecuencia / total_frecuencia
        prob_acumulada_sup = prob_acumulada_inf + probabilidad

        # Calcular columnas adicionales
        valor_por_frecuencia = valor * frecuencia
        ocurrencias = ocurrencias_dict.get(valor, 0)
        porcentaje = ocurrencias / len(pares) if len(pares) > 0 else 0
        ocurrencias_por_valor = ocurrencias * valor
        
        # Insertar datos en la tabla
        tree_finales.insert("", "end", values=[
            valor, frecuencia, f"{probabilidad:.2f}", f"{prob_acumulada_inf:.2f}", f"{prob_acumulada_sup:.2f}",
            valor_por_frecuencia, ocurrencias, f"{porcentaje:.2%}", ocurrencias_por_valor
        ])

        prob_acumulada_inf = prob_acumulada_sup


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ingreso de Cantidad de Pares (Valor, Frecuencia)")

# Etiqueta y campo de entrada para la cantidad de pares
etiqueta_cantidad = tk.Label(ventana, text="Cantidad de Pares:")
etiqueta_cantidad.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

entry_cantidad = tk.Entry(ventana)
entry_cantidad.grid(row=0, column=1, padx=10, pady=10)

# Etiqueta y campo de entrada para la cantidad de simulaciones
etiqueta_cant_simulaciones = tk.Label(ventana, text="Cant. Simulaciones:")
etiqueta_cant_simulaciones.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

entry_cant_simulaciones = tk.Entry(ventana)
entry_cant_simulaciones.grid(row=1, column=1, padx=10, pady=10)

# Botón para ingresar la cantidad de pares y simulaciones
boton_ingresar_cantidad = tk.Button(ventana, text="Ingresar Cantidad", command=obtener_datos)
boton_ingresar_cantidad.grid(row=2, column=0, columnspan=2, pady=10)

# Crear el botón de simulación, pero inicialmente deshabilitado
boton_simulacion = tk.Button(ventana, text="Simulación", state=tk.DISABLED)
boton_simulacion.grid(row=3, column=0, columnspan=2, pady=10)

# Botón para mostrar los resultados finales
#boton_resultados_finales = tk.Button(ventana, text="Resultados Finales", command=lambda: mostrar_resultados_finales(pares, {}))
#boton_resultados_finales.grid(row=4, column=0, columnspan=2, pady=10)

# Ejecutar el bucle principal de la interfaz gráfica
ventana.mainloop()

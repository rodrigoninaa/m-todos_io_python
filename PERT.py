import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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

# Función para mostrar actividades
def mostrar_actividades():
    resultado_text.delete("1.0", tk.END)  # Limpiar el cuadro de texto
    for actividad in actividades:
        resultado_text.insert(tk.END, f"Actividad: {actividad.nombre}\n")
        resultado_text.insert(tk.END, f"Predecesores: {actividad.predecesores}\n")
        resultado_text.insert(tk.END, f"Tiempo optimista: {actividad.tiempo_optimista}\n")
        resultado_text.insert(tk.END, f"Tiempo más probable: {actividad.tiempo_mas_probable}\n")
        resultado_text.insert(tk.END, f"Tiempo pesimista: {actividad.tiempo_pesimista}\n")
        resultado_text.insert(tk.END, f"Tiempo esperado: {actividad.tiempo_esperado}\n")
        resultado_text.insert(tk.END, f"Varianza: {actividad.varianza}\n")
        resultado_text.insert(tk.END, f"Desviación estándar: {actividad.desviacion_estandar}\n\n")

# Función para calcular y mostrar la ruta crítica
def mostrar_ruta_critica():
    G = construir_grafo()
    fechas_tempranas, fechas_tardias, holguras, ruta_critica = cpm(G)
    
    resultado_text.delete("1.0", tk.END)  # Limpiar el cuadro de texto
    resultado_text.insert(tk.END, "Ruta crítica: {}\n".format(ruta_critica))

    # Dibujar el gráfico con la ruta crítica resaltada
    plt.clf()
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=8, font_color="black", font_weight="bold")
    nx.draw_networkx_edges(G, pos, edgelist=[(ruta_critica[i], ruta_critica[i + 1]) for i in range(len(ruta_critica) - 1)], edge_color='red', width=2)
    canvas.draw()

# Función para construir el grafo a partir de las actividades
def construir_grafo():
    G = nx.DiGraph()
    for actividad in actividades:
        for predecesor in actividad.predecesores:
            G.add_edge(predecesor, actividad.nombre, weight=actividad.tiempo_esperado)
    return G

# Función para calcular el camino crítico
def cpm(graph):
    fechas_tempranas = {nodo: 0 for nodo in graph.nodes()}
    for nodo in nx.topological_sort(graph):
        for sucesor in graph.successors(nodo):
            fechas_tempranas[sucesor] = max(fechas_tempranas[sucesor], fechas_tempranas[nodo] + graph[nodo][sucesor]['weight'])

    ultimo_nodo = list(graph.nodes())[-1]
    fechas_tardias = {nodo: fechas_tempranas[ultimo_nodo] for nodo in graph.nodes()}
    for nodo in reversed(list(nx.topological_sort(graph))):
        for predecesor in graph.predecessors(nodo):
            fechas_tardias[predecesor] = min(fechas_tardias[predecesor], fechas_tardias[nodo] - graph[predecesor][nodo]['weight'])

    holguras = {nodo: fechas_tardias[nodo] - fechas_tempranas[nodo] for nodo in graph.nodes()}
    ruta_critica = [nodo for nodo in graph.nodes() if holguras[nodo] == 0]

    return fechas_tempranas, fechas_tardias, holguras, ruta_critica

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Análisis de Proyecto")

# Botón para mostrar actividades
boton_mostrar = ttk.Button(ventana, text="Mostrar Actividades", command=mostrar_actividades)
boton_mostrar.pack(pady=10)

# Cuadro de texto para mostrar resultados
resultado_text = tk.Text(ventana, width=50, height=20)
resultado_text.pack()

# Botón para mostrar el gráfico con la ruta crítica
boton_ruta_critica = ttk.Button(ventana, text="Mostrar Ruta Crítica", command=mostrar_ruta_critica)
boton_ruta_critica.pack(pady=10)

# Configurar el gráfico en la ventana
figura, ax = plt.subplots()
canvas = FigureCanvasTkAgg(figura, master=ventana)
widget_canvas = canvas.get_tk_widget()
widget_canvas.pack()

ventana.mainloop()

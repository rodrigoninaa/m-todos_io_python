import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import scrolledtext

def cpm(graph):
    # Calcula las fechas tempranas
    fechas_tempranas = {nodo: 0 for nodo in graph.nodes()}
    for nodo in nx.topological_sort(graph):
        for sucesor in graph.successors(nodo):
            fechas_tempranas[sucesor] = max(fechas_tempranas[sucesor], fechas_tempranas[nodo] + graph[nodo][sucesor]['weight'])

    # Calcula las fechas tardías
    ultimo_nodo = list(graph.nodes())[-1]
    fechas_tardias = {nodo: fechas_tempranas[ultimo_nodo] for nodo in graph.nodes()}
    for nodo in reversed(list(nx.topological_sort(graph))):
        for predecesor in graph.predecessors(nodo):
            fechas_tardias[predecesor] = min(fechas_tardias[predecesor], fechas_tardias[nodo] - graph[predecesor][nodo]['weight'])

    # Calcula las holguras
    holguras = {nodo: fechas_tardias[nodo] - fechas_tempranas[nodo] for nodo in graph.nodes()}

    # Identificar la ruta crítica
    ruta_critica = [nodo for nodo in graph.nodes() if holguras[nodo] == 0]

    return fechas_tempranas, fechas_tardias, holguras, ruta_critica

# Crear ventana emergente
root = tk.Tk()
root.title("Resultados de CPM")

# Ejemplo de uso
G = nx.DiGraph()
G.add_edge(0, 1, weight=3)
G.add_edge(0, 2, weight=2)
G.add_edge(1, 3, weight=4)
G.add_edge(2, 3, weight=2)
G.add_edge(2, 4, weight=3)
G.add_edge(3, 5, weight=2)
G.add_edge(4, 5, weight=2)

fechas_tempranas, fechas_tardias, holguras, ruta_critica = cpm(G)

# Crear y configurar la ventana emergente
resultados_text = scrolledtext.ScrolledText(root, width=50, height=10, wrap=tk.WORD)
resultados_text.pack()

# Imprimir los resultados en la ventana emergente
resultados_text.insert(tk.END, "Fechas tempranas: {}\n".format(fechas_tempranas))
resultados_text.insert(tk.END, "Fechas tardías: {}\n".format(fechas_tardias))
resultados_text.insert(tk.END, "Holguras: {}\n".format(holguras))
resultados_text.insert(tk.END, "Ruta crítica: {}\n".format(ruta_critica))

# Dibuja el gráfico resaltando la ruta crítica
pos = nx.spring_layout(G)
node_colors = ["red" if nodo in ruta_critica else "skyblue" for nodo in G.nodes()]
edge_colors = ["red" if (nodo, sucesor) in G.edges() and nodo in ruta_critica and sucesor in ruta_critica else "black" for nodo, sucesor in G.edges()]

nx.draw_networkx(G, pos, with_labels=True, node_size=700, node_color=node_colors, font_size=8, font_color="black", font_weight="bold", edgelist=G.edges(), edge_color=edge_colors)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
plt.show()

# Ejecutar la ventana emergente
root.mainloop()

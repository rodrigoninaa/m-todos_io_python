import networkx as nx
import matplotlib.pyplot as plt

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

    return fechas_tempranas, fechas_tardias, holguras

# Ejemplo de uso
G = nx.DiGraph()
G.add_edge(0, 1, weight=3)
G.add_edge(0, 2, weight=2)
G.add_edge(1, 3, weight=4)
G.add_edge(2, 3, weight=2)
G.add_edge(2, 4, weight=3)
G.add_edge(3, 5, weight=2)
G.add_edge(4, 5, weight=2)

fechas_tempranas, fechas_tardias, holguras = cpm(G)

# Imprime los resultados
print("Fechas tempranas:", fechas_tempranas)
print("Fechas tardías:", fechas_tardias)
print("Holguras:", holguras)

# Dibuja el gráfico
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=8, font_color="black", font_weight="bold")
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
plt.show()

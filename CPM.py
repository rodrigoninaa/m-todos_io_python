import networkx as nx
import matplotlib.pyplot as plt

def cpm(graph):
    # Calcula las fechas tempranas
    early_dates = {node: 0 for node in graph.nodes()}
    for node in nx.topological_sort(graph):
        for successor in graph.successors(node):
            early_dates[successor] = max(early_dates[successor], early_dates[node] + graph[node][successor]['weight'])

    # Calcula las fechas tardías
    last_node = list(graph.nodes())[-1]
    late_dates = {node: early_dates[last_node] for node in graph.nodes()}
    for node in reversed(list(nx.topological_sort(graph))):
        for predecessor in graph.predecessors(node):
            late_dates[predecessor] = min(late_dates[predecessor], late_dates[node] - graph[predecessor][node]['weight'])

    # Calcula las holguras
    slack = {node: late_dates[node] - early_dates[node] for node in graph.nodes()}

    return early_dates, late_dates, slack

# Ejemplo de uso
G = nx.DiGraph()
G.add_edge(0, 1, weight=3)
G.add_edge(0, 2, weight=2)
G.add_edge(1, 3, weight=4)
G.add_edge(2, 3, weight=2)
G.add_edge(2, 4, weight=3)
G.add_edge(3, 5, weight=2)
G.add_edge(4, 5, weight=2)

early_dates, late_dates, slack = cpm(G)

# Imprime los resultados
print("Fechas tempranas:", early_dates)
print("Fechas tardías:", late_dates)
print("Holguras:", slack)

# Dibuja el gráfico
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=8, font_color="black", font_weight="bold")
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
plt.show()

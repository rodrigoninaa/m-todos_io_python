import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog

class GeneradorGrafo:
    def __init__(self):
        self.G = nx.Graph()
        self.contador_nodos = 1  # Comenzamos con el nodo 1

    def crear_ramas(self, nodo_padre, num_ramas):
        nodos_hijos = range(self.contador_nodos, self.contador_nodos + num_ramas)
        self.G.add_edges_from([(nodo_padre, hijo) for hijo in nodos_hijos])
        self.contador_nodos += num_ramas
        return nodos_hijos

    def visualizar_grafo(self):
        pos = nx.spring_layout(self.G)
        nx.draw(self.G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)
        plt.show()

def obtener_numero_ramas(nodo_text):
    return simpledialog.askinteger("Número de ramas", f"Ingrese el número de ramas para el nodo {nodo_text}:")

def main():
    try:
        generador = GeneradorGrafo()

        num_ramas = obtener_numero_ramas("principal (1)")
        if num_ramas is None or num_ramas < 0:
            print("Por favor, ingresa un número mayor o igual a 0.")
            return
        
        nodos_hijos = generador.crear_ramas(1, num_ramas)

        for i, nodo_hijo in enumerate(nodos_hijos, start=2):
            num_ramas_hijo = obtener_numero_ramas(nodo_hijo)
            if num_ramas_hijo is None or num_ramas_hijo < 0:
                print("Por favor, ingresa un número mayor o igual a 0.")
                return

            generador.crear_ramas(nodo_hijo, num_ramas_hijo)

        generador.visualizar_grafo()

    except ValueError:
        print("Por favor, ingresa un valor numérico válido.")

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox

class DiagramaGantt:
    def __init__(self, tareas):
        self.tareas = tareas

    def crear_diagrama(self):
        root = tk.Tk()
        root.title("Diagrama de Gantt")

        # Encabezados
        tk.Label(root, text="Tarea", font=("Helvetica", 12, "bold")).grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        tk.Label(root, text="Inicio", font=("Helvetica", 12, "bold")).grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        tk.Label(root, text="Fin", font=("Helvetica", 12, "bold")).grid(row=0, column=2, padx=10, pady=5, sticky="ew")

        # Datos de tareas
        for i, tarea in enumerate(self.tareas, start=1):
            tk.Label(root, text=tarea['name']).grid(row=i, column=0, padx=10, pady=5, sticky="w")
            tk.Label(root, text=tarea['start']).grid(row=i, column=1, padx=10, pady=5, sticky="w")
            tk.Label(root, text=tarea['end']).grid(row=i, column=2, padx=10, pady=5, sticky="w")

        # Ajustar el tamaño de las columnas
        for j in range(3):
            root.grid_columnconfigure(j, weight=1)

        tk.mainloop()

# Ejemplo de uso
tareas = [
    {'name': 'Tarea 1', 'start': '2022-01-01', 'end': '2022-01-05'},
    {'name': 'Tarea 2', 'start': '2022-01-06', 'end': '2022-01-10'},
    {'name': 'Tarea 3', 'start': '2022-01-11', 'end': '2022-01-15'}
]

diagrama = DiagramaGantt(tareas)
diagrama.crear_diagrama()

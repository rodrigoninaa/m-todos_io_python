import tkinter as tk
from tkinter import ttk
from scipy.optimize import minimize
import numpy as np

class QuadraticProgrammingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Programación Cuadrática")

        self.create_widgets()

    def create_widgets(self):
        # Variables de entrada
        self.coefficient_label = ttk.Label(self.root, text="Coeficientes:")
        self.coefficient_entry = ttk.Entry(self.root)
        self.coefficient_label.grid(row=0, column=0, sticky=tk.W)
        self.coefficient_entry.grid(row=0, column=1)

        self.constraint_label = ttk.Label(self.root, text="Restricciones:")
        self.constraint_entry = ttk.Entry(self.root)
        self.constraint_label.grid(row=1, column=0, sticky=tk.W)
        self.constraint_entry.grid(row=1, column=1)

        # Botón para resolver
        self.solve_button = ttk.Button(self.root, text="Resolver", command=self.solve_problem)
        self.solve_button.grid(row=2, column=0, columnspan=2)

        # Resultado
        self.result_label = ttk.Label(self.root, text="Resultado:")
        self.result_label.grid(row=3, column=0, sticky=tk.W)

    def solve_problem(self):
        # Obtener los coeficientes y restricciones de las entradas
        coefficients = np.fromstring(self.coefficient_entry.get(), sep=',')
        constraints = np.fromstring(self.constraint_entry.get(), sep=',')

        # Definir la función objetivo cuadrática
        def objective(x, Q, c):
            return 0.5 * np.dot(x, np.dot(Q, x)) + np.dot(c, x)

        # Definir las restricciones de igualdad y desigualdad (en este ejemplo no hay)
        constraints_eq = []
        constraints_ineq = []

        # Resolver el problema de programación cuadrática
        result = minimize(objective, np.zeros_like(coefficients), args=(np.diag(coefficients), constraints),
                          constraints={'type': 'eq', 'fun': lambda x: constraints_eq, 'jac': lambda x: []},
                          bounds=[(None, None)] * len(coefficients))

        # Mostrar el resultado en la interfaz gráfica
        self.result_label.config(text=f"Resultado: {result.x}\nValor óptimo: {result.fun}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuadraticProgrammingApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import Label, Entry, Button

from scipy.optimize import minimize

def objective_function(vars):
    x, y, z, lambda1, lambda2, r = vars
    return x * (1/y) * z**2 + lambda1 * (1/2 * x**3 * y * (1/z) - 1) + lambda2 * (1/4 * x**(-1/2) + 1/4 * y**(-1/2) + 1/4 * z - 1) + r * (-1/8 + 1/3 * z) + (-7/3 + 1/6 * z)

def run_optimization():
    # Obtener las condiciones iniciales desde la interfaz
    x_val = float(x_entry.get())
    y_val = float(y_entry.get())
    z_val = float(z_entry.get())
    r_val = float(r_entry.get())

    # Definir las condiciones iniciales
    initial_guess = [x_val, y_val, z_val, 0, 0, r_val]

    # Definir las restricciones de desigualdad
    constraints = [
        {'type': 'ineq', 'fun': lambda vars: 1/2 * vars[0]**3 * vars[1] * (1/vars[2]) - 1},
        {'type': 'ineq', 'fun': lambda vars: 1/4 * vars[0]**(-1/2) + 1/4 * vars[1]**(-1/2) + 1/4 * vars[2] - 1},
        {'type': 'ineq', 'fun': lambda vars: vars[5] - 14}  # Restricción adicional para r>=14
    ]

    # Resolver el problema de optimización
    result = minimize(objective_function, initial_guess, constraints=constraints)

    # Extraer los valores óptimos de x, y, y z
    optimal_values = result.x[:-1]  # Excluir el valor óptimo de r

    # Mostrar los puntos factibles
    result_label.config(text=f"Puntos factibles:\nx: {optimal_values[0]}\ny: {optimal_values[1]}\nz: {optimal_values[2]}")

# Crear la ventana principal
window = tk.Tk()
window.title("Optimización")

# Crear y posicionar los elementos en la ventana
Label(window, text="Condiciones iniciales:").grid(row=0, column=0, columnspan=2)

Label(window, text="x:").grid(row=1, column=0)
x_entry = Entry(window)
x_entry.grid(row=1, column=1)

Label(window, text="y:").grid(row=2, column=0)
y_entry = Entry(window)
y_entry.grid(row=2, column=1)

Label(window, text="z:").grid(row=3, column=0)
z_entry = Entry(window)
z_entry.grid(row=3, column=1)

Label(window, text="r:").grid(row=4, column=0)
r_entry = Entry(window)
r_entry.grid(row=4, column=1)

Button(window, text="Optimizar", command=run_optimization).grid(row=5, column=0, columnspan=2)

result_label = Label(window, text="")
result_label.grid(row=6, column=0, columnspan=2)

# Iniciar el bucle de la interfaz gráfica
window.mainloop()

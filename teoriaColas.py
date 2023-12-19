import tkinter as tk
from tkinter import ttk

def calcular_utilizacion(root):
    def on_calculate():
        input_lambda = float(lambda_entry.get())
        input_mu = float(mu_entry.get())
        utilizacion = input_lambda / input_mu
        result_label.config(text=f"Utilización: {utilizacion}")

    input_window = tk.Toplevel(root)
    input_window.title("Input")
    
    lambda_label = ttk.Label(input_window, text="Tasa media de llegadas (λ):")
    lambda_label.grid(column=0, row=0, padx=10, pady=5, sticky=tk.E)
    
    lambda_entry = ttk.Entry(input_window)
    lambda_entry.grid(column=1, row=0, padx=10, pady=5, sticky=tk.W)
    
    mu_label = ttk.Label(input_window, text="Tasa media de servicio en trabajos por minuto (μ):")
    mu_label.grid(column=0, row=1, padx=10, pady=5, sticky=tk.E)
    
    mu_entry = ttk.Entry(input_window)
    mu_entry.grid(column=1, row=1, padx=10, pady=5, sticky=tk.W)

    calculate_button = ttk.Button(input_window, text="Calcular", command=on_calculate)
    calculate_button.grid(column=0, row=2, columnspan=2, pady=10)

    result_label = ttk.Label(input_window, text="")
    result_label.grid(column=0, row=3, columnspan=2, pady=5)

def calcular_numero_esperado_sistema(root):
    def on_calculate():
        input_lambda = float(lambda_entry.get())
        input_mu = float(mu_entry.get())
        numero_esperado_sistema = input_lambda / (input_mu - input_lambda)
        result_label.config(text=f"Número esperado en el sistema: {numero_esperado_sistema}")

    input_window = tk.Toplevel(root)
    input_window.title("Input")
    
    lambda_label = ttk.Label(input_window, text="Tasa media de llegadas (λ):")
    lambda_label.grid(column=0, row=0, padx=10, pady=5, sticky=tk.E)
    
    lambda_entry = ttk.Entry(input_window)
    lambda_entry.grid(column=1, row=0, padx=10, pady=5, sticky=tk.W)
    
    mu_label = ttk.Label(input_window, text="Tasa media de servicio en trabajos por minuto (μ):")
    mu_label.grid(column=0, row=1, padx=10, pady=5, sticky=tk.E)
    
    mu_entry = ttk.Entry(input_window)
    mu_entry.grid(column=1, row=1, padx=10, pady=5, sticky=tk.W)

    calculate_button = ttk.Button(input_window, text="Calcular", command=on_calculate)
    calculate_button.grid(column=0, row=2, columnspan=2, pady=10)

    result_label = ttk.Label(input_window, text="")
    result_label.grid(column=0, row=3, columnspan=2, pady=5)

def calcular_numero_esperado_cola(root):
    def on_calculate():
        input_lambda = float(lambda_entry.get())
        input_mu = float(mu_entry.get())
        numero_esperado_cola = (input_lambda ** 2) / (input_mu * (input_mu - input_lambda))
        result_label.config(text=f"Número esperado en la cola de espera: {numero_esperado_cola}")

    input_window = tk.Toplevel(root)
    input_window.title("Input")
    
    lambda_label = ttk.Label(input_window, text="Tasa media de llegadas (λ):")
    lambda_label.grid(column=0, row=0, padx=10, pady=5, sticky=tk.E)
    
    lambda_entry = ttk.Entry(input_window)
    lambda_entry.grid(column=1, row=0, padx=10, pady=5, sticky=tk.W)
    
    mu_label = ttk.Label(input_window, text="Tasa media de servicio en trabajos por minuto (μ):")
    mu_label.grid(column=0, row=1, padx=10, pady=5, sticky=tk.E)
    
    mu_entry = ttk.Entry(input_window)
    mu_entry.grid(column=1, row=1, padx=10, pady=5, sticky=tk.W)

    calculate_button = ttk.Button(input_window, text="Calcular", command=on_calculate)
    calculate_button.grid(column=0, row=2, columnspan=2, pady=10)

    result_label = ttk.Label(input_window, text="")
    result_label.grid(column=0, row=3, columnspan=2, pady=5)

def calcular_tiempo_esperado_cola(root):
    def on_calculate():
        input_lambda = float(lambda_entry.get())
        input_mu = float(mu_entry.get())
        tiempo_esperado_cola = 1 / (input_mu - input_lambda)
        result_label.config(text=f"Tiempo esperado en la cola de espera: {tiempo_esperado_cola}")

    input_window = tk.Toplevel(root)
    input_window.title("Input")
    
    lambda_label = ttk.Label(input_window, text="Tasa media de llegadas (λ):")
    lambda_label.grid(column=0, row=0, padx=10, pady=5, sticky=tk.E)
    
    lambda_entry = ttk.Entry(input_window)
    lambda_entry.grid(column=1, row=0, padx=10, pady=5, sticky=tk.W)
    
    mu_label = ttk.Label(input_window, text="Tasa media de servicio en trabajos por minuto (μ):")
    mu_label.grid(column=0, row=1, padx=10, pady=5, sticky=tk.E)
    
    mu_entry = ttk.Entry(input_window)
    mu_entry.grid(column=1, row=1, padx=10, pady=5, sticky=tk.W)

    calculate_button = ttk.Button(input_window, text="Calcular", command=on_calculate)
    calculate_button.grid(column=0, row=2, columnspan=2, pady=10)

    result_label = ttk.Label(input_window, text="")
    result_label.grid(column=0, row=3, columnspan=2, pady=5)

def calcular_tiempo_esperado_promedio(root):
    def on_calculate():
        input_lambda = float(lambda_entry.get())
        input_mu = float(mu_entry.get())
        tiempo_esperado_promedio = 1 / (input_mu - input_lambda)
        result_label.config(text=f"Tiempo de espera promedio: {tiempo_esperado_promedio}")


    input_window = tk.Toplevel(root)
    input_window.title("Input")
    
    lambda_label = ttk.Label(input_window, text="Tasa media de llegadas (λ):")
    lambda_label.grid(column=0, row=0, padx=10, pady=5, sticky=tk.E)
    
    lambda_entry = ttk.Entry(input_window)
    lambda_entry.grid(column=1, row=0, padx=10, pady=5, sticky=tk.W)
    
    mu_label = ttk.Label(input_window, text="Tasa media de servicio en trabajos por minuto (μ):")
    mu_label.grid(column=0, row=1, padx=10, pady=5, sticky=tk.E)
    
    mu_entry = ttk.Entry(input_window)
    mu_entry.grid(column=1, row=1, padx=10, pady=5, sticky=tk.W)

    calculate_button = ttk.Button(input_window, text="Calcular", command=on_calculate)
    calculate_button.grid(column=0, row=2, columnspan=2, pady=10)

    result_label = ttk.Label(input_window, text="")
    result_label.grid(column=0, row=3, columnspan=2, pady=5)

def calcular_probabilidad_desocupado(root):
    def on_calculate():
        input_lambda = float(lambda_entry.get())
        input_mu = float(mu_entry.get())
        probabilidad_desocupado = 1 - (input_lambda / input_mu)
        result_label.config(text=f"Probabilidad de que el sistema esté desocupado: {probabilidad_desocupado:.2%}")

    input_window = tk.Toplevel(root)
    input_window.title("Input")
    
    lambda_label = ttk.Label(input_window, text="Tasa media de llegadas (λ):")
    lambda_label.grid(column=0, row=0, padx=10, pady=5, sticky=tk.E)
    
    lambda_entry = ttk.Entry(input_window)
    lambda_entry.grid(column=1, row=0, padx=10, pady=5, sticky=tk.W)
    
    mu_label = ttk.Label(input_window, text="Tasa media de servicio en trabajos por minuto (μ):")
    mu_label.grid(column=0, row=1, padx=10, pady=5, sticky=tk.E)
    
    mu_entry = ttk.Entry(input_window)
    mu_entry.grid(column=1, row=1, padx=10, pady=5, sticky=tk.W)

    calculate_button = ttk.Button(input_window, text="Calcular", command=on_calculate)
    calculate_button.grid(column=0, row=2, columnspan=2, pady=10)

    result_label = ttk.Label(input_window, text="")
    result_label.grid(column=0, row=3, columnspan=2, pady=5)

def ejecutar_calculo(opcion, root):
    if opcion == 1:
        calcular_utilizacion(root)
    elif opcion == 2:
        calcular_numero_esperado_sistema(root)
    elif opcion == 3:
        calcular_numero_esperado_cola(root)
    elif opcion == 4:
        calcular_tiempo_esperado_promedio(root)
    elif opcion == 5:
        calcular_tiempo_esperado_cola(root)
    elif opcion == 6:
        calcular_probabilidad_desocupado(root)
 

def crear_interfaz():
    def on_calculate(option):
        ejecutar_calculo(option, root)

    root = tk.Tk()
    root.title("Calculadora de Colas")

    frame = ttk.Frame(root, padding="10")
    frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    label = ttk.Label(frame, text="Selecciona una fórmula:")
    label.grid(column=0, row=0, columnspan=2, pady=10)

    options = [
        "Utilización",
        "Número esperado en el sistema",
        "Número esperado en la cola de espera",
        "Tiempo de espera promedio",
        "Tiempo esperado en la cola de espera",
        "Probabilidad de que el sistema esté desocupado"
    ]

    for i, option_text in enumerate(options, start=1):
        button = ttk.Button(frame, text=option_text, command=lambda i=i: on_calculate(i))
        button.grid(column=0, row=i, pady=5)

    root.mainloop()

if __name__ == "__main__":
    crear_interfaz()

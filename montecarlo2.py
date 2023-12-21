import random
import sympy as sp
import tkinter as tk

def montecarlo_integral(estimaciones, funcion, intervalo):
    # Desempaquetamos el intervalo
    a, b = intervalo
    
    # Inicializamos la suma de valores de la función evaluados en puntos aleatorios
    suma_funcion = 0
    
    # Realizamos 'estimaciones' iteraciones
    for _ in range(estimaciones):
        # Generamos un punto aleatorio en el intervalo [a, b)
        x = random.uniform(a, b)
        
        # Evaluamos la función en el punto x y sumamos el resultado
        suma_funcion += funcion(x)

    # Calculamos la estimación de la integral como el promedio de los valores de la función
    # multiplicado por la longitud del intervalo
    estimacion_integral = (suma_funcion / estimaciones) * (b - a)

    return estimacion_integral

def mostrar_resultados():
    expresion = expresion_entry.get()
    intervalo_a = float(a_entry.get())
    intervalo_b = float(b_entry.get())
    num_estimaciones = 100000  # Número fijo de estimaciones (puedes ajustarlo según sea necesario)

    try:
        x = sp.symbols('x')
        funcion_usuario = sp.lambdify(x, sp.sympify(expresion), 'numpy')
        intervalo_usuario = (intervalo_a, intervalo_b)

        # Utilizamos el método Montecarlo para estimar la integral definida
        integral_estimada = montecarlo_integral(num_estimaciones, funcion_usuario, intervalo_usuario)

        # Crear una nueva ventana para mostrar los resultados
        resultados_ventana = tk.Toplevel(ventana)
        resultados_ventana.title("Resultados")

        # Etiqueta para mostrar el resultado
        resultado_label = tk.Label(resultados_ventana, text=f"Estimación con metodo Montecarlo =====> {integral_estimada}")
        resultado_label.pack()

    except Exception as e:
        # Mostrar un mensaje de error en la ventana principal
        error_label.config(text=f"Error: {str(e)}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Estimador de Integral con Montecarlo")

# Etiqueta y entrada para la expresión de la función
expresion_label = tk.Label(ventana, text="Ingrese la función en términos de x:")
expresion_label.pack()
expresion_entry = tk.Entry(ventana)
expresion_entry.pack()

# Etiquetas y entradas para los límites del intervalo
a_label = tk.Label(ventana, text="Límite inferior del intervalo:")
a_label.pack()
a_entry = tk.Entry(ventana)
a_entry.pack()

b_label = tk.Label(ventana, text="Límite superior del intervalo:")
b_label.pack()
b_entry = tk.Entry(ventana)
b_entry.pack()

# Botón para ejecutar el método de Montecarlo
ejecutar_button = tk.Button(ventana, text="Ejecutar Montecarlo", command=mostrar_resultados)
ejecutar_button.pack()

# Etiqueta para mostrar mensajes de error
error_label = tk.Label(ventana, text="")
error_label.pack()

# Botón para cerrar la ventana
cerrar_button = tk.Button(ventana, text="Cerrar", command=ventana.destroy)
cerrar_button.pack()

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()

import random
import sympy as sp

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

# Solicitamos al usuario ingresar la función en términos de x
expresion = input("Ingrese la función en términos de x: ")
x = sp.symbols('x')
funcion_usuario = sp.lambdify(x, sp.sympify(expresion), 'numpy')

# Solicitamos al usuario ingresar el intervalo
a = float(input("Ingrese el límite inferior del intervalo: "))
b = float(input("Ingrese el límite superior del intervalo: "))
intervalo_usuario = (a, b)

# Número de estimaciones/simulaciones
num_estimaciones = 100000

# Utilizamos el método Montecarlo para estimar la integral definida
integral_estimada = montecarlo_integral(num_estimaciones, funcion_usuario, intervalo_usuario)

# Imprimimos el resultado
print(f"Estimación de la integral definida: {integral_estimada}")
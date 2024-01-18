import customtkinter as ctk
import tkinter as tk
import numpy as np

def calcular():
    # Recuperamos la información de la función mostrar
    n = int(entry1.get()) # Numero de criterios
    nalt =  int(entry2.get()) # Numero de alternativas

    global matrices, promedios
    root = tk.Toplevel()
    root.configure(bg="#242424")
    root.title("AHP")

    # Añadir la barra de desplazamiento al root
    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill='y')

    # Crear un canvas
    canvas = tk.Canvas(root, yscrollcommand=scrollbar.set, bg="#242424", highlightthickness=0)
    canvas.pack(side=tk.LEFT, fill='both', expand=True)

    # Configurar la barra de desplazamiento para usarla con el canvas
    scrollbar.config(command=canvas.yview)

    # Crear un frame dentro del canvas para añadir los widgets
    frame = tk.Frame(canvas, bg="#242424")
    canvas.create_window((0,0), window=frame, anchor='nw')

    # Ajustar el scrollregion después de que el frame se haya renderizado
    def adjust_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox('all'))

    frame.bind('<Configure>', adjust_scrollregion)

    # Crear un número específico de matrices 
    num_matrices = nalt+1  # Define el número de matrices aquí
    all_avg_values = []  # Almacenamos todos los vectores columna de promedios aquí
    for _ in range(num_matrices):
        if _ == 0:  # Solo para la primera matriz
            title_label = tk.Label(frame, text="Matriz de criterios", fg="white", bg="#242424", font=("Calibri", 16))
            title_label.pack(padx=50, pady=(30, 20))
        elif _ == 1:  # Solo para la segunda matriz
            title_label = tk.Label(frame, text="Matrices de comparacion de las alternativas", fg="white", bg="#242424", font=("Calibri", 16))
            title_label.pack(padx=50, pady=(30, 20))

        matrix_frame = tk.Frame(frame, bg="#242424")
        matrix_frame.pack(pady=20)  # Espaciado entre las matrices

        updated_values = []  # Almacenamos los valores actualizados aquí
        for i in range(n):
            row = []
            for j in range(n):
                # Crear los títulos de las columnas y filas
                title = tk.Label(matrix_frame, text=f"C{j+1}", fg="white", bg="#242424", font=("Calibri", 15))
                title.grid(row=0, column=j+1, padx=5, pady=5)  # Ajustar la posición

                title = tk.Label(matrix_frame, text=f"C{i+1}", fg="white", bg="#242424", font=("Calibri", 15))
                title.grid(row=i+1, column=0, padx=5, pady=5)  # Ajustar la posición

                # Aquí cambiamos el Entry por un Label para que sea de solo lectura
                # Si la casilla está vacía, se asume que es un cero
                value = matrices[_][i][j].get() if matrices[_][i][j].get() != "" else "0"
                label = tk.Label(matrix_frame, text=value, fg="white", bg="#242424", font=("Calibri", 15))
                label.grid(row=i+1, column=j+1, padx=5, pady=5)  # Usar grid en lugar de place y ajustar la posición
                row.append(float(value))
            updated_values.append(row)

        #.. Aquí calculamos y mostramos la suma de cada columna
        for j in range(n):
            sum_column = sum(updated_values[i][j] for i in range(n))
            sum_label = tk.Label(matrix_frame, text=str(round(sum_column,3)), fg="#242424", bg="#242424", font=("Calibri", 15))
            sum_label.grid(row=n+1, column=j+1, padx=5, pady=5)  # Ajustar la posición

            # Aquí actualizamos el valor de cada celda con el resultado de la división de la celda entre el valor de la suma de su respectiva columna
            for i in range(n):
                updated_value = updated_values[i][j] / sum_column if sum_column != 0 else 0
                label = tk.Label(matrix_frame, text=str(round(updated_value, 3)), fg="white", bg="#242424", font=("Calibri", 15))
                label.grid(row=i+1, column=j+1, padx=5, pady=5)  # Usar grid en lugar de place y ajustar la posición
                updated_values[i][j] = updated_value  # Actualizamos el valor en la matriz

        # Aquí calculamos y mostramos el promedio de cada fila
        avg_values = []
        for i in range(n):
            avg_row = sum(updated_values[i]) / n
            avg_label = tk.Label(matrix_frame, text=str(round(avg_row,3)), fg="white", bg="#242424", font=("Calibri", 15))
            avg_label.grid(row=i+1, column=n+2, padx=20, pady=5)  # Ajustar la posición
            avg_values.append(avg_row)

        # Agregamos un título al vector columna de promedios
        title = tk.Label(matrix_frame, text="Vector propio", fg="white", bg="#242424", font=("Calibri", 15))
        title.grid(row=0, column=n+2, padx=20, pady=5)  # Ajustar la posición

    # Solo para la primera matriz, calculamos y mostramos el vector columna "A"
        if _ == 0:
            for i in range(n):
                a_value = sum(updated_values[i][j] * avg_values[j] for j in range(n))
                a_label = tk.Label(matrix_frame, text=str(round(a_value,3)), fg="white", bg="#242424", font=("Calibri", 15))
                a_label.grid(row=i+1, column=n+3, padx=20, pady=5)  # Ajustar la posición

            # Agregamos un título al vector columna "A"
            title = tk.Label(matrix_frame, text="A", fg="white", bg="#242424", font=("Calibri", 15))
            title.grid(row=0, column=n+3, padx=20, pady=5)  # Ajustar la posición

        # Almacenamos el vector columna de promedios para usarlo más tarde
        all_avg_values.append(avg_values)



        # Crear una nueva matriz debajo de la última matriz, donde cada columna es el vector columna correspondiente de cada una de las matrices anteriores, sin considerar la primera matriz
    new_matrix_frame = tk.Frame(frame, bg="#242424")
    new_matrix_frame.pack(pady=20)  # Espaciado entre las matrices


    matrix_values = []  # Almacenamos los valores de la matriz aquí

    for i in range(n):  # Recorremos las filas
        row_values = []  # Almacenamos los valores de la fila aquí
        for j in range(1, num_matrices):  # Comenzamos desde 1 para ignorar la primera matriz
            value = all_avg_values[j][i]
            row_values.append(value)  # Añadimos el valor a la lista de valores de la fila
            label = tk.Label(new_matrix_frame, text=str(round(value, 3)), fg="white", bg="#242424", font=("Calibri", 15))
            label.grid(row=i+1, column=j, padx=5, pady=5)  # Usar grid en lugar de place y ajustar la posición
        matrix_values.append(row_values)  # Añadimos la fila a la matriz


    
        # Agregamos un título al vector columna "Vector propio"
    title = tk.Label(new_matrix_frame, text="Vector propio", fg="white", bg="#242424", font=("Calibri", 15))
    title.grid(row=0, column=num_matrices, padx=20, pady=5)  # Ajustar la posición

    
    
    # Mostrar el vector propio correspondiente a la primera matriz al lado de la última matriz
    for i in range(n):
        value = all_avg_values[0][i]
        label = tk.Label(new_matrix_frame, text=str(round(value, 3)), fg="white", bg="#242424", font=("Calibri", 15))
        label.grid(row=i+1, column=num_matrices, padx=5, pady=5)  # Usar grid en lugar de place y ajustar la posición


    # Solo para la última matriz, calculamos y mostramos el vector columna "A"
    if _ == num_matrices - 1:
        a_values = [sum(matrix_values[i][j] * all_avg_values[0][j] for j in range(n)) for i in range(n)]
        for i in range(n):
            a_label = tk.Label(new_matrix_frame, text=str(round(a_values[i], 3)), fg="#ECD43C", bg="#242424", font=("Calibri", 15))
            a_label.grid(row=i+1, column=num_matrices+1, padx=5, pady=5)  # Usar grid en lugar de place y ajustar la posición

            # Agregamos un título al vector columna "A"
            title = tk.Label(new_matrix_frame, text="A", fg="#ECD43C", bg="#242424", font=("Calibri", 15))
            title.grid(row=0, column=num_matrices+1, padx=20, pady=5)  # Ajustar la posición

        # Encontrar el mayor número en el vector "A" y su correspondiente número de fila
        max_value = max(a_values)
        max_index = a_values.index(max_value) + 1

        # Convertir el mayor número a su forma de porcentaje
        max_value_percentage = max_value * 100

        # Mostrar el mayor número, su forma de porcentaje y su correspondiente número de fila
        max_value_label = tk.Label  (new_matrix_frame, text=f"La alternativa {max_index} es la mejor opción según los criterios elegidos con {round(max_value_percentage,1)}% de importancia", fg="white", bg="#242424", font=("Calibri", 15))
        max_value_label.grid(row=n+2, column=1, columnspan=num_matrices+1, padx=30, pady=5)  # Usar grid en lugar de place y ajustar la posición

 
    root.update_idletasks()  # Actualizar la ventana gráfica
    root.geometry(f'{root.winfo_width()}x{root.winfo_height()}')  # Ajustar el tamaño de la ventana al tamaño del contenido

    root.mainloop()





def mostrar():
    n = int(entry1.get()) # Numero de criterios
    nalt =  int(entry2.get()) # Numero de alternativas

    global matrices, promedios
    root = tk.Toplevel()
    root.configure(bg="#242424")
    root.title("AHP")

    # Añadir la barra de desplazamiento al root
    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill='y')

    # Crear un canvas
    canvas = tk.Canvas(root, yscrollcommand=scrollbar.set, bg="#242424", highlightthickness=0)
    canvas.pack(side=tk.LEFT, fill='both', expand=True)

    # Configurar la barra de desplazamiento para usarla con el canvas
    scrollbar.config(command=canvas.yview)

    # Crear un frame dentro del canvas para añadir los widgets
    frame = tk.Frame(canvas, bg="#242424")
    canvas.create_window((0,0), window=frame, anchor='nw')

    # Ajustar el scrollregion después de que el frame se haya renderizado
    def adjust_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox('all'))

    frame.bind('<Configure>', adjust_scrollregion)

    title_label = tk.Label(frame, text="Matriz de criterios", fg="white", bg="#242424", font=("Calibri", 16))
    title_label.pack(padx=50, pady=(30, 20))

    # Crear un número específico de matrices 
    num_matrices = nalt+1  # Define el número de matrices aquí
    matrices = []
    promedios = []
    for _ in range(num_matrices):
        if _ == 1:  # Solo para la segunda matriz
            title_label = tk.Label(frame, text="Matrices de comparacion de las alternativas", fg="white", bg="#242424", font=("Calibri", 16))
            title_label.pack(padx=50, pady=(30, 20))

        matrix_frame = tk.Frame(frame, bg="#242424")
        matrix_frame.pack(pady=20)  # Espaciado entre las matrices

        matrix = []
        promedio = []
        for i in range(n):
            row = []
            for j in range(n):
                # Crear los títulos de las columnas y filas
                title = tk.Label(matrix_frame, text=f"C{j+1}", fg="white", bg="#242424", font=("Calibri", 15))
                title.grid(row=0, column=j+1, padx=5, pady=5)  # Ajustar la posición

                title = tk.Label(matrix_frame, text=f"C{i+1}", fg="white", bg="#242424", font=("Calibri", 15))
                title.grid(row=i+1, column=0, padx=5, pady=5)  # Ajustar la posición

                entry = ctk.CTkEntry(matrix_frame, width=50, font=ctk.CTkFont(size=15))  # Reducir el ancho
                entry.grid(row=i+1, column=j+1, padx=5, pady=5)  # Usar grid en lugar de place y ajustar la posición
                row.append(entry)

            promedio_label = tk.Label(matrix_frame, text="", fg="white", bg="#242424", font=("Calibri", 15))
            promedio_label.grid(row=i+1, column=6, padx=5, pady=5)  # Ajustar la posición
            promedio.append(promedio_label)

            matrix.append(row)
        matrices.append(matrix)
        promedios.append(promedio)

    boton = ctk.CTkButton(frame, text="Calcular",font=ctk.CTkFont(size=17),command=calcular)
    boton.pack(pady=20)

    result_label = tk.Label(frame, text="", fg="white", bg="#242424", font=("Calibri", 13))
    result_label.pack(pady=10)

    root.update_idletasks()  # Actualizar la ventana gráfica
    root.geometry(f'{root.winfo_width()}x{root.winfo_height()}')  # Ajustar el tamaño de la ventana al tamaño del contenido

    root.mainloop()

root = tk.Tk()
root.geometry("450x370")
root.configure(bg="#242424")
root.title("AHP")

title_label = tk.Label(root, text="Proceso Analítico Jerárquico (AHP)", fg="white", bg="#242424", font=("Calibri", 16))
title_label.pack(padx=10, pady=(30, 20))

text_label = tk.Label(root, text="Número de criterios (n):", fg="white", bg="#242424", font=("Calibri", 13))
text_label.pack(pady=10,padx=18,anchor='w')

entry1 = ctk.CTkEntry(root, width=300,font=ctk.CTkFont(size=15))
entry1.pack(pady=10,padx=18,anchor="w")

text_label = tk.Label(root, text="Número de alternativas (nalt):", fg="white", bg="#242424", font=("Calibri", 13))
text_label.pack(pady=10,padx=18,anchor='w')

entry2 = ctk.CTkEntry(root, width=300,font=ctk.CTkFont(size=15))
entry2.pack(pady=10,padx=18,anchor="w")

boton = ctk.CTkButton(root, text="Mostrar",font=ctk.CTkFont(size=17), command=mostrar)
boton.pack(pady=20)

result_label = tk.Label(root, text="", fg="white", bg="#242424", font=("Calibri", 13))
result_label.pack(pady=10)

root.mainloop()

import customtkinter as ctk
import tkinter as tk
import math

def create_window():
    new_window = tk.Toplevel(root)
    new_window.geometry("500x450")
    new_window.configure(bg="#313131")
    new_window.title("M/M/1")

    title_label = tk.Label(new_window, text="M/M/1", fg="white", bg="#313131", font=("Calibri", 20))
    title_label.pack(padx=10, pady=(30, 20))

    optionmenu_1 = ctk.CTkOptionMenu(new_window, values=["Utilización", "Número esperado en el sistema", "Número esperado en la cola de espera",
    "Tiempo de espera promedio", "Tiempo esperado en la cola de espera",
    "Probabilidad de que el sistema esté desocupado","Número promedio de unidades en el sistema","Tiempo promedio que la unidad pasa en la linea de espera","Tiempo promedio que una unidad pasa en el sistema"], width=470,font=ctk.CTkFont(size=17))
    optionmenu_1.pack(pady=10)

    text_label = tk.Label(new_window, text="Tasa media de llegadas (λ):", fg="white", bg="#313131", font=("Calibri", 13))
    text_label.pack(pady=10,padx=18,anchor='w')

    entry1 = ctk.CTkEntry(new_window, width=300,font=ctk.CTkFont(size=15))
    entry1.pack(pady=10,padx=18,anchor="w")

    text_label = tk.Label(new_window, text="Tasa media de servicio en trabajos por minuto (μ):", fg="white", bg="#313131", font=("Calibri", 13))
    text_label.pack(pady=10,padx=18,anchor='w')

    entry2 = ctk.CTkEntry(new_window, width=300,font=ctk.CTkFont(size=15))
    entry2.pack(pady=10,padx=18,anchor="w")

    def calcular():
        input_lambda = float(entry1.get())
        input_mu = float(entry2.get())
        
        operacion = optionmenu_1.get()
        
        if operacion == "Utilización":
            resultado = input_lambda / input_mu
        elif operacion == "Número esperado en el sistema":
            resultado = input_lambda / (input_mu - input_lambda)
        elif operacion == "Número esperado en la cola de espera":
            resultado = (input_lambda*input_lambda) / (input_mu*(input_mu - input_lambda))
        elif operacion == "Tiempo de espera promedio":
            resultado = 1 / (input_mu - input_lambda)
        elif operacion == "Tiempo esperado en la cola de espera":
            resultado = input_lambda / (input_mu*(input_mu - input_lambda))
        elif operacion == "Probabilidad de que el sistema esté desocupado":
            resultado = 1 - (input_lambda/input_mu)
        elif operacion == "Número promedio de unidades en el sistema":
            resultado = (pow(input_lambda,2)/ (input_mu*(input_mu - input_lambda))) + input_lambda/input_mu
        elif operacion == "Tiempo promedio que la unidad pasa en la linea de espera":
            resultado = (pow(input_lambda,2)/ (input_mu*(input_mu - input_lambda)))/input_lambda

        elif operacion == "Tiempo promedio que una unidad pasa en el sistema":
            resultado = ((pow(input_lambda,2)/ (input_mu*(input_mu - input_lambda)))/input_lambda) + 1/input_mu

        
        
        result_label.config(text="Resultado: " + str(resultado))

    boton = ctk.CTkButton(new_window, text="Calcular",font=ctk.CTkFont(size=17), command=calcular)
    boton.pack(pady=20)

    result_label = tk.Label(new_window, text="", fg="white", bg="#313131", font=("Calibri", 13))
    result_label.pack(pady=10)

#----------------------------------------------------------------

def create_window2():
    new_window2 = tk.Toplevel(root)
    new_window2.geometry("600x550")
    new_window2.configure(bg="#313131")
    new_window2.title("M/M/s")

    title_label = tk.Label(new_window2, text="M/M/s", fg="white", bg="#313131", font=("Calibri", 20))
    title_label.pack(padx=10, pady=(30, 20))

    optionmenu_1 = ctk.CTkOptionMenu(new_window2, values=["Utilización","Tiempo promedio que la unidad pasa en la linea de espera","Número promedio de unidades en la linea de espera","Tiempo promedio que una unidad pasa en el sistema","Número promedio de unidades en el sistema","Probabilidad de que el sistema esté vacio","Probabilidad que haya n unidades en el sistema"], width=570,font=ctk.CTkFont(size=17))
    optionmenu_1.pack(pady=10)

    text_label = tk.Label(new_window2, text="Tasa media de llegadas (λ):", fg="white", bg="#313131", font=("Calibri", 13))
    text_label.pack(pady=10,padx=18,anchor='w')

    entry1 = ctk.CTkEntry(new_window2, width=300,font=ctk.CTkFont(size=15))
    entry1.pack(pady=10,padx=18,anchor="w")

    text_label = tk.Label(new_window2, text="Tasa media de servicio en trabajos por minuto (μ):", fg="white", bg="#313131", font=("Calibri", 13))
    text_label.pack(pady=10,padx=18,anchor='w')

    entry2 = ctk.CTkEntry(new_window2, width=300,font=ctk.CTkFont(size=15))
    entry2.pack(pady=10,padx=18,anchor="w")

    text_label = tk.Label(new_window2, text="Número de servidores (s):", fg="white", bg="#313131", font=("Calibri", 13))
    text_label.pack(pady=10,padx=18,anchor='w')

    entry3 = ctk.CTkEntry(new_window2, width=300,font=ctk.CTkFont(size=15))
    entry3.pack(pady=10,padx=18,anchor="w")

    

    def calcular():
        sumatoria = 0
        input_lambda = float(entry1.get())
        input_mu = float(entry2.get())
        nservidores = int(entry3.get())
        
        operacion = optionmenu_1.get()

        # Calculando P0 -----------------------------
        for n in range(nservidores):
                termino = (1/math.factorial(n)) * ((input_lambda/input_mu)**n)
                sumatoria += termino

        operacion_adicional = (1/math.factorial(nservidores)) * ((input_lambda/input_mu)**nservidores) * ((nservidores*input_mu)/(nservidores*input_mu-input_lambda))

        p0 = 1/ (sumatoria + operacion_adicional)

        # --------------------------------------------
        
        if operacion == "Tiempo promedio que la unidad pasa en la linea de espera":


            # Calcular el factorial de (nservidores-1)
            m = nservidores - 1
            factorial = math.factorial(m)

            # Calcular (nservidores*input_mu - input_lambda)^2
            cuadrado = (nservidores*input_mu - input_lambda)**2
                     
            resultado = ((input_mu * ((input_lambda / input_mu) ** nservidores)) / (factorial * cuadrado)) * p0

        elif operacion == "Número promedio de unidades en la linea de espera":
     
            m = nservidores - 1
            factorial = math.factorial(m)

            cuadrado = (nservidores*input_mu - input_lambda)**2
                     
            wq = ((input_mu * ((input_lambda / input_mu) ** nservidores)) / (factorial * cuadrado)) * p0

            # lq
            resultado = input_lambda * wq


        elif operacion == "Tiempo promedio que una unidad pasa en el sistema":
     
            m = nservidores - 1
            factorial = math.factorial(m)

            cuadrado = (nservidores*input_mu - input_lambda)**2
                     
            wq = ((input_mu * ((input_lambda / input_mu) ** nservidores)) / (factorial * cuadrado)) * p0

            resultado = wq + (1/input_mu)
        
        elif operacion == "Número promedio de unidades en el sistema":
     
            m = nservidores - 1
            factorial = math.factorial(m)

            cuadrado = (nservidores*input_mu - input_lambda)**2
                     
            wq = ((input_mu * ((input_lambda / input_mu) ** nservidores)) / (factorial * cuadrado)) * p0

            # lq
            lq = input_lambda * wq

            resultado = lq + input_lambda/input_mu
        
        elif operacion == "Probabilidad de que el sistema esté vacio":
            
            resultado = p0

        elif operacion == "Probabilidad que haya n unidades en el sistema":

            resultado = ((input_lambda / input_mu) ** nservidores) * p0

        elif operacion == "Utilización":

            resultado = input_lambda/(nservidores*input_mu)


        result_label.config(text="Resultado: " + str(round(resultado,6)))


    boton = ctk.CTkButton(new_window2, text="Calcular",font=ctk.CTkFont(size=17), command=calcular)
    boton.pack(pady=20)

    result_label = tk.Label(new_window2, text="", fg="white", bg="#313131", font=("Calibri", 13))
    result_label.pack(pady=10)

# ------------------------------------
#  Ventana principal --------
root = tk.Tk()
root.geometry("450x300")
root.configure(bg="#313131")
root.title("Teoria de colas")

title_label = tk.Label(root, text="Teoria de colas", fg="white", bg="#313131", font=("Calibri", 28))
title_label.pack(padx=10, pady=(40, 20))

add_button = ctk.CTkButton(root, text="M/M/1", width=300, font=ctk.CTkFont(size=20), command=create_window)
add_button.pack(pady=20)

add_button = ctk.CTkButton(root, text="M/M/s", width=300, font=ctk.CTkFont(size=20), command=create_window2)
add_button.pack(pady=20)

root.mainloop()

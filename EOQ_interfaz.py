import tkinter as tkr
import math

# Creacion de la primera ventana
ventana = tkr.Tk()
ventana.geometry("350x200")
ventana.resizable(width=False, height=False)
ventana.title("Costes de investario EOQ")

# Creacion de la segunda ventana
ventana_2 = tkr.Toplevel(ventana)
ventana_2.title("Ventana de resultados")
ventana_2.geometry("350x125")
ventana_2.resizable(width=False, height=False)
ventana_2.withdraw() # <-- para ocultar la ventana una vez inicializado el programa

def ventana_calculos():
    ventana_2.deiconify()
    # ******************************
    # *     Zona ce calculos...    *
    # ******************************

    # Se calcula la cantidad economica de pedido

    CEP = math.sqrt((2*(float(entrada_01.get()))*(float(entrada_04.get())))/float(entrada_02.get()))

    # se calcula el numero de pedidos por periodo

    NPP = float(entrada_01.get())/CEP

    # Se calcula el tiempo entre pedidos

    TEP = float(entrada_06.get())/NPP

    # Se calcula el punto de reorden

    PR = float(entrada_01.get())*float(entrada_05.get())/float(entrada_06.get())

    # Se calculan Costos
    #   [1] Costo total relevante

    CTR = (float(entrada_01.get())*float(entrada_04.get())/CEP) + (CEP*float(entrada_02.get())/2)

    #   [2] Costo total de inventario por periodo

    CTI = float(entrada_01.get())*float(entrada_03.get()) + CTR

    # Pasar los resultados al contenido de la ventana...
    # el RAUND es para limitar decimales, en este caso 3

    entrada_01_2.config(text= round(CEP, 3))
    entrada_02_2.config(text= round(NPP, 3))
    entrada_03_2.config(text= round(TEP, 3))
    entrada_04_2.config(text= round(PR, 3))
    entrada_05_2.config(text= round(CTR, 3))
    entrada_06_2.config(text= round(CTI, 3))

#**************************************************************************************************************

# Creacion de los elemtos de la ventana_1 (ingraso de datos)

etiqueta_01 = tkr.Label(ventana, text="Demanda anual (D) : ")
etiqueta_02 = tkr.Label(ventana, text="Costo de mantenimiento (H) :")
etiqueta_03 = tkr.Label(ventana, text="Costo por unidad (C) : ")
etiqueta_04 = tkr.Label(ventana, text="Costo por pedido (S) : ")
etiqueta_05 = tkr.Label(ventana, text="Tiempo que demora el pedido (L) : ")
etiqueta_06 = tkr.Label(ventana, text="Dias que laboran al amio: ")

entrada_01 = tkr.Entry(ventana)
entrada_02 = tkr.Entry(ventana)
entrada_03 = tkr.Entry(ventana)
entrada_04 = tkr.Entry(ventana)
entrada_05 = tkr.Entry(ventana)
entrada_06 = tkr.Entry(ventana)

boton_01 = tkr.Button(ventana, text="Calcular", command=ventana_calculos )

# Creacion de los elemtos de la ventana_2 (resultados)

etiqueta_01_2 = tkr.Label(ventana_2, text="Cantidad economica de pedido     --> ")
etiqueta_02_2 = tkr.Label(ventana_2, text="Numero de pedidos por periodo    --> ")
etiqueta_03_2 = tkr.Label(ventana_2, text="Tiempo entre pedidos             --> ")
etiqueta_04_2 = tkr.Label(ventana_2, text="Punto de reorden                 --> ")
etiqueta_05_2 = tkr.Label(ventana_2, text="Costo total relevante            --> ")
etiqueta_06_2 = tkr.Label(ventana_2, text="Costo total del inventario       --> ")

entrada_01_2 = tkr.Label(ventana_2)
entrada_02_2 = tkr.Label(ventana_2)
entrada_03_2 = tkr.Label(ventana_2)
entrada_04_2 = tkr.Label(ventana_2)
entrada_05_2 = tkr.Label(ventana_2)
entrada_06_2 = tkr.Label(ventana_2)


# Pocicionamiento de los elementos en la tabla Ventana_1 (ingreso de datos)

etiqueta_01.grid(row=0, column=1, sticky="w")
etiqueta_02.grid(row=1, column=1, sticky="w")
etiqueta_03.grid(row=2, column=1, sticky="w")
etiqueta_04.grid(row=3, column=1, sticky="w")
etiqueta_05.grid(row=4, column=1, sticky="w")
etiqueta_06.grid(row=5, column=1, sticky="w")

entrada_01.grid(row=0, column=2)
entrada_02.grid(row=1, column=2)
entrada_03.grid(row=2, column=2)
entrada_04.grid(row=3, column=2)
entrada_05.grid(row=4, column=2)
entrada_06.grid(row=5, column=2)

boton_01.place(x=150,y=150)

# Pocicionamiento de los elementos en la tabla Ventana_2 (resultados)

etiqueta_01_2.grid(row=0, column=1, sticky="w")
etiqueta_02_2.grid(row=1, column=1, sticky="w")
etiqueta_03_2.grid(row=2, column=1, sticky="w")
etiqueta_04_2.grid(row=3, column=1, sticky="w")
etiqueta_05_2.grid(row=4, column=1, sticky="w")
etiqueta_06_2.grid(row=5, column=1, sticky="w")

entrada_01_2.grid(row=0, column=2, sticky="w")
entrada_02_2.grid(row=1, column=2, sticky="w")
entrada_03_2.grid(row=2, column=2, sticky="w")
entrada_04_2.grid(row=3, column=2, sticky="w")
entrada_05_2.grid(row=4, column=2, sticky="w")
entrada_06_2.grid(row=5, column=2, sticky="w")



ventana.mainloop()
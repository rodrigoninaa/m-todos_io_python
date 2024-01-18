import tkinter as tkr
import math
from tkinter import messagebox

# Creacion de la primera ventana
ventana = tkr.Tk()
ventana.geometry("350x200")
ventana.resizable(width=False, height=False)
ventana.title("EOQ Con Rupturas")
ventana.withdraw()

# Creacion de la segunda ventana
ventana_2 = tkr.Toplevel(ventana)
ventana_2.title("Ventana de resultados")
ventana_2.geometry("350x125")
ventana_2.resizable(width=False, height=False)
ventana_2.withdraw() # <-- para ocultar la ventana una vez inicializado el programa


def mostrar_ventana():
    ventana.deiconify()
    ventana_2.withdraw()

def Limpiar():
    entrada_01.delete(0, "end")
    entrada_02.delete(0, "end")
    entrada_03.delete(0, "end")
    entrada_04.delete(0, "end")


def ventana_calculos():
    ventana.withdraw()
    ventana_2.deiconify()

    D = float(entrada_01.get())
    A = float(entrada_02.get())
    C = float(entrada_03.get())
    S = float(entrada_04.get())
    H = float(entrada_05.get())

    Q = math.sqrt(2*D*S*(A+H)/(H*A))
    Ss = math.sqrt(2*D*S*(A)/((A+H)*H))
    tiempo_entre_pedido = Q/D
    coste_total_ciclo = S + C*Q + H*Ss*Ss/(2*D) + A*(Q-Ss)*(Q-Ss)/(2*D)
    coste_anual = (1/tiempo_entre_pedido)*coste_total_ciclo

    entrada_01_2.config(text= round(Q, 3))
    entrada_02_2.config(text= round(Ss, 3))
    entrada_03_2.config(text= round(tiempo_entre_pedido, 3))
    entrada_04_2.config(text= round(coste_total_ciclo, 3))
    entrada_05_2.config(text= round(coste_anual, 3))

#**************************************************************************************************************

# Creacion de los elemtos de la ventana_1 (ingraso de datos)
    
ventana.deiconify()

etiqueta_01 = tkr.Label(ventana, text="Demanda anual (D) : ")
etiqueta_02 = tkr.Label(ventana, text="Coste adicional c/und :")
etiqueta_03 = tkr.Label(ventana, text="Costo por unidad (C) : ")
etiqueta_04 = tkr.Label(ventana, text="Costo por pedido (S) : ")
etiqueta_05 = tkr.Label(ventana, text="Costo por mantenimiento (H) : ")


entrada_01 = tkr.Entry(ventana)
entrada_02 = tkr.Entry(ventana)
entrada_03 = tkr.Entry(ventana)
entrada_04 = tkr.Entry(ventana)
entrada_05 = tkr.Entry(ventana)


boton_01 = tkr.Button(ventana, text="Calcular", command=ventana_calculos )
boton_02 = tkr.Button(ventana, text="Limpiar", command= Limpiar)

# Creacion de los elemtos de la ventana_2 (resultados)

etiqueta_01_2 = tkr.Label(ventana_2, text="Pedido Optimo (Q) : ")
etiqueta_02_2 = tkr.Label(ventana_2, text="Pedido Optimo (S) : ")
etiqueta_03_2 = tkr.Label(ventana_2, text="Tiempo entre pedidos : ")
etiqueta_04_2 = tkr.Label(ventana_2, text="Costo total de Ciclo : ")
etiqueta_05_2 = tkr.Label(ventana_2, text="Coste anual : ")


entrada_01_2 = tkr.Label(ventana_2)
entrada_02_2 = tkr.Label(ventana_2)
entrada_03_2 = tkr.Label(ventana_2)
entrada_04_2 = tkr.Label(ventana_2)
entrada_05_2 = tkr.Label(ventana_2)



# Pocicionamiento de los elementos en la tabla Ventana_1 (ingreso de datos)

etiqueta_01.grid(row=0, column=1, sticky="w")
etiqueta_02.grid(row=1, column=1, sticky="w")
etiqueta_03.grid(row=2, column=1, sticky="w")
etiqueta_04.grid(row=3, column=1, sticky="w")
etiqueta_05.grid(row=4, column=1, sticky="w")


entrada_01.grid(row=0, column=2)
entrada_02.grid(row=1, column=2)
entrada_03.grid(row=2, column=2)
entrada_04.grid(row=3, column=2)
entrada_05.grid(row=4, column=2)


boton_01.place(x=120,y=150)
boton_02.place(x=180, y= 150)

# Pocicionamiento de los elementos en la tabla Ventana_2 (resultados)

etiqueta_01_2.grid(row=0, column=1, sticky="w")
etiqueta_02_2.grid(row=1, column=1, sticky="w")
etiqueta_03_2.grid(row=2, column=1, sticky="w")
etiqueta_04_2.grid(row=3, column=1, sticky="w")
etiqueta_05_2.grid(row=4, column=1, sticky="w")

entrada_01_2.grid(row=0, column=2, sticky="w")
entrada_02_2.grid(row=1, column=2, sticky="w")
entrada_03_2.grid(row=2, column=2, sticky="w")
entrada_04_2.grid(row=3, column=2, sticky="w")
entrada_05_2.grid(row=4, column=2, sticky="w")



ventana_2.protocol("WM_DELETE_WINDOW", mostrar_ventana)


ventana.mainloop()
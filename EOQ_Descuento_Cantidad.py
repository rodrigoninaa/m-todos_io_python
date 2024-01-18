import tkinter as tkr
import math
from tkinter import messagebox

# Creacion de la primera ventana
ventana = tkr.Tk()
ventana.geometry("400x235")
ventana.resizable(width=False, height=False)
ventana.title("Costes de investario EOQ Descuentos por cantidad")
#ventana.withdraw()

# Creacion de la segunda ventana
ventana_2 = tkr.Toplevel(ventana)
ventana_2.title("Ventana de resultados")
ventana_2.geometry("650x200")
ventana_2.resizable(width=False, height=False)
#ventana_2.withdraw() # <-- para ocultar la ventana una vez inicializado el programa



def ventana_calculos():
    # Para volverlos a editar, para borrar sus datos
    entrada_7_1.config(state="normal")
    entrada_7_2.config(state="normal")
    entrada_7_3.config(state="normal")
    entrada_7_4.config(state="normal")
    entrada_7_5.config(state="normal")
    entrada_8_1.config(state="normal")
    entrada_8_2.config(state="normal")
    entrada_8_3.config(state="normal")
    entrada_8_4.config(state="normal")
    entrada_8_5.config(state="normal")
    entrada_9_1.config(state="normal")
    entrada_9_2.config(state="normal")
    entrada_9_3.config(state="normal")
    entrada_9_4.config(state="normal")
    entrada_9_5.config(state="normal")

    # Para limpiar los cuadros antes de insertar
    entrada_7_1.delete(0, "end")
    entrada_7_2.delete(0, "end")
    entrada_7_3.delete(0, "end")
    entrada_7_4.delete(0, "end")
    entrada_7_5.delete(0, "end")
    entrada_8_1.delete(0, "end")
    entrada_8_2.delete(0, "end")
    entrada_8_3.delete(0, "end")
    entrada_8_4.delete(0, "end")
    entrada_8_5.delete(0, "end")
    entrada_9_1.delete(0, "end")
    entrada_9_2.delete(0, "end")
    entrada_9_3.delete(0, "end")
    entrada_9_4.delete(0, "end")
    entrada_9_5.delete(0, "end")

    #calculos y copia
    cantidad_1 = math.sqrt((2*(float(entrada_01.get()))*(float(entrada_02.get())))/(float(entrada_03.get())*float(entrada_07_3.get())))
    cantidad_2 = math.sqrt((2*(float(entrada_01.get()))*(float(entrada_02.get())))/(float(entrada_03.get())*float(entrada_08_3.get())))
    cantidad_3 = math.sqrt((2*(float(entrada_01.get()))*(float(entrada_02.get())))/(float(entrada_03.get())*float(entrada_09_3.get())))
    #print("cantidad_1: ", cantidad_1)
    #print("cantidad_2: ", cantidad_2)
    #print("cantidad_3: ", cantidad_3)
    
    # Verifica y calcula la cantidad optima
    if cantidad_1 >= float(entrada_07_2.get()): 
        entrada_7_5.insert(0,"No procede")
    elif cantidad_1 <= float(entrada_07_1.get()):
        entrada_7_5.insert(0, entrada_07_1.get())
    else: 
        entrada_7_5.insert(0, round(cantidad_1, 3))


    if cantidad_2 >= float(entrada_08_2.get()): 
        entrada_8_5.insert(0,"No procede")
    elif cantidad_2 <= float(entrada_08_1.get()):
        entrada_8_5.insert(0, entrada_08_1.get())
    else: 
        entrada_8_5.insert(0, round(cantidad_2, 3))


    if cantidad_3 >= float(entrada_09_2.get()): 
        entrada_9_5.insert(0,"No procede")
    elif cantidad_3 <= float(entrada_09_1.get()):
        entrada_9_5.insert(0, entrada_09_1.get())
    else: 
        entrada_9_5.insert(0, round(cantidad_3, 3))

    # Calculando el costo por mantener
    cantidad_1 = float(entrada_7_5.get())*float(entrada_03.get())*float(entrada_07_3.get())/2
    cantidad_2 = float(entrada_8_5.get())*float(entrada_03.get())*float(entrada_08_3.get())/2
    cantidad_3 = float(entrada_9_5.get())*float(entrada_03.get())*float(entrada_09_3.get())/2

    entrada_7_2.insert(0, round(cantidad_1, 3))
    entrada_8_2.insert(0, round(cantidad_2, 3))
    entrada_9_2.insert(0, round(cantidad_3, 3))

    # Calculando el costo de ordenar
    cantidad_1 = float(entrada_02.get())*float(entrada_01.get())/float(entrada_7_5.get())
    cantidad_2 = float(entrada_02.get())*float(entrada_01.get())/float(entrada_8_5.get())
    cantidad_3 = float(entrada_02.get())*float(entrada_01.get())/float(entrada_9_5.get())

    entrada_7_1.insert(0, round(cantidad_1, 3))
    entrada_8_1.insert(0, round(cantidad_2, 3))
    entrada_9_1.insert(0, round(cantidad_3, 3))

    # Calculando costo de producto
    cantidad_1 = float(entrada_02.get())*float(entrada_07_3.get())
    cantidad_2 = float(entrada_02.get())*float(entrada_08_3.get())
    cantidad_3 = float(entrada_02.get())*float(entrada_09_3.get())

    entrada_7_3.insert(0, round(cantidad_1, 3))
    entrada_8_3.insert(0, round(cantidad_2, 3))
    entrada_9_3.insert(0, round(cantidad_3, 3))

    # Calculando el costo total
    cantidad_1 = float(entrada_7_1.get())+float(entrada_7_2.get())+float(entrada_7_3.get())
    cantidad_2 = float(entrada_8_1.get())+float(entrada_8_2.get())+float(entrada_8_3.get())
    cantidad_3 = float(entrada_9_1.get())+float(entrada_9_2.get())+float(entrada_9_3.get())

    entrada_7_4.insert(0, round(cantidad_1, 3))
    entrada_8_4.insert(0, round(cantidad_2, 3))
    entrada_9_4.insert(0, round(cantidad_3, 3))

    entrada_7_1.config(state="readonly")
    entrada_7_2.config(state="readonly")
    entrada_7_3.config(state="readonly")
    entrada_7_4.config(state="readonly")
    entrada_7_5.config(state="readonly")
    entrada_8_1.config(state="readonly")
    entrada_8_2.config(state="readonly")
    entrada_8_3.config(state="readonly")
    entrada_8_4.config(state="readonly")
    entrada_8_5.config(state="readonly")
    entrada_9_1.config(state="readonly")
    entrada_9_2.config(state="readonly")
    entrada_9_3.config(state="readonly")
    entrada_9_4.config(state="readonly")
    entrada_9_5.config(state="readonly")

ventana.deiconify()

# Creacion de los elemtos de la ventana_1 (ingraso de datos)
etiqueta_01 = tkr.Label(ventana, text="Costo por ordenar (S) : ")
etiqueta_02 = tkr.Label(ventana, text="Demanda anula (D) :")
etiqueta_03 = tkr.Label(ventana, text="Mantenimiento porsentaje (I) : ")
etiqueta_04 = tkr.Label(ventana, text=" ")
etiqueta_05 = tkr.Label(ventana, text="Tabla de intervalos : ")
etiqueta_06_1 = tkr.Label(ventana, text="Minimo")
etiqueta_06_2 = tkr.Label(ventana, text="Maximo")
etiqueta_06_3= tkr.Label(ventana, text="Costo por unidad")

#etiquetas de la ventana 2
etiqueta_6_1 = tkr.Label(ventana_2, text="Costo de orden")
etiqueta_6_2 = tkr.Label(ventana_2, text="Costo de mantener")
etiqueta_6_3 = tkr.Label(ventana_2, text="Costo de producto")
etiqueta_6_4 = tkr.Label(ventana_2, text="Costo total")
etiqueta_6_5 = tkr.Label(ventana_2, text="Cantidad a ordenar")

#Cuadros modificables de la ventana 1
entrada_01 = tkr.Entry(ventana)
entrada_02 = tkr.Entry(ventana)
entrada_03 = tkr.Entry(ventana)
entrada_07_1 = tkr.Entry(ventana)
entrada_07_2 = tkr.Entry(ventana)
entrada_07_3 = tkr.Entry(ventana)
entrada_08_1 = tkr.Entry(ventana)
entrada_08_2 = tkr.Entry(ventana)
entrada_08_3 = tkr.Entry(ventana)
entrada_09_1 = tkr.Entry(ventana)
entrada_09_2 = tkr.Entry(ventana)
entrada_09_3 = tkr.Entry(ventana)

#Cuadros modificables de ventana 2
entrada_7_1 = tkr.Entry(ventana_2)
entrada_7_2 = tkr.Entry(ventana_2)
entrada_7_3 = tkr.Entry(ventana_2)
entrada_7_4 = tkr.Entry(ventana_2)
entrada_7_5 = tkr.Entry(ventana_2)
entrada_8_1 = tkr.Entry(ventana_2)
entrada_8_2 = tkr.Entry(ventana_2)
entrada_8_3 = tkr.Entry(ventana_2)
entrada_8_4 = tkr.Entry(ventana_2)
entrada_8_5 = tkr.Entry(ventana_2)
entrada_9_1 = tkr.Entry(ventana_2)
entrada_9_2 = tkr.Entry(ventana_2)
entrada_9_3 = tkr.Entry(ventana_2)
entrada_9_4 = tkr.Entry(ventana_2)
entrada_9_5 = tkr.Entry(ventana_2)

# Pocicionamiento de etiquetas en ventana 1
etiqueta_01.grid(row=0, column=1, sticky="w")
etiqueta_02.grid(row=1, column=1, sticky="w")
etiqueta_03.grid(row=2, column=1, sticky="w")
etiqueta_04.grid(row=3, column=1, sticky="w")
etiqueta_05.grid(row=4, column=1, sticky="w")
etiqueta_06_1.grid(row=5, column=1)
etiqueta_06_2.grid(row=5, column=2)
etiqueta_06_3.grid(row=5, column=3)

# Pocicionamiento de etiquetas en ventana 2
etiqueta_6_1.grid(row=1, column=1)
etiqueta_6_2.grid(row=1, column=2)
etiqueta_6_3.grid(row=1, column=3)
etiqueta_6_4.grid(row=1, column=4)
etiqueta_6_5.grid(row=1, column=5)

# Pocicionamiento de Entradas en ventana 1
entrada_01.grid(row=0, column=2)
entrada_02.grid(row=1, column=2)
entrada_03.grid(row=2, column=2)
entrada_07_1.grid(row=7, column=1)
entrada_07_2.grid(row=7, column=2)
entrada_07_3.grid(row=7, column=3)
entrada_08_1.grid(row=8, column=1)
entrada_08_2.grid(row=8, column=2)
entrada_08_3.grid(row=8, column=3)
entrada_09_1.grid(row=9, column=1)
entrada_09_2.grid(row=9, column=2)
entrada_09_3.grid(row=9, column=3)

# Pocicionamiento de entradas en ventana 2
entrada_7_1.grid(row=2, column=1)
entrada_7_2.grid(row=2, column=2)
entrada_7_3.grid(row=2, column=3)
entrada_7_4.grid(row=2, column=4)
entrada_7_5.grid(row=2, column=5)
entrada_8_1.grid(row=3, column=1)
entrada_8_2.grid(row=3, column=2)
entrada_8_3.grid(row=3, column=3)
entrada_8_4.grid(row=3, column=4)
entrada_8_5.grid(row=3, column=5)
entrada_9_1.grid(row=4, column=1)
entrada_9_2.grid(row=4, column=2)
entrada_9_3.grid(row=4, column=3)
entrada_9_4.grid(row=4, column=4)
entrada_9_5.grid(row=4, column=5)

boton_01 = tkr.Button(ventana, text="Calcular", command=ventana_calculos )
boton_01.place(x=170,y=190)


ventana.mainloop()
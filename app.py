import customtkinter
from PIL import Image, ImageTk
from tkinter import ttk
import subprocess
import tkinter as tk


app = customtkinter.CTk(fg_color="white")  
app.geometry("1920x1080")
app.title("APP v2")


#frames lateral y largo
fm_largo = customtkinter.CTkFrame(app, width=1900, height=180, fg_color="#BFD1E1",corner_radius=0,border_color="#2e2e2e",border_width=1)
fm_largo.pack()

#imagen banner
imagen = Image.open("images\logo_banner.jpg")
imagen_tk = ImageTk.PhotoImage(imagen)
lb_banner = customtkinter.CTkLabel(app, image=imagen_tk,text="")
lb_banner.place(x=0,y=0)

#cpm
img_cpm = Image.open("images\cpm.jpg")
img_cpm = ImageTk.PhotoImage(img_cpm)
lb_cpm = customtkinter.CTkLabel(app, image=img_cpm,text="")
lb_cpm.place(x=25,y=210)

#pert
img_pert = Image.open("images\pert.jpg")
imagen_tk = ImageTk.PhotoImage(img_pert)
lb_pert = customtkinter.CTkLabel(app, image=imagen_tk,text="")
lb_pert.place(x=25,y=490)

#eoq 
img_eoq = Image.open("images\eoq.jpg")
imagen_tk = ImageTk.PhotoImage(img_eoq)
lb_eoq = customtkinter.CTkLabel(app, image=imagen_tk,text="")
lb_eoq.place(x=325,y=490)

#ahp- certidumbre
img_ahp = Image.open("images\Ahp.jpg")
imagen_tk = ImageTk.PhotoImage(img_ahp)
lb_ahp = customtkinter.CTkLabel(app, image=imagen_tk,text="")
lb_ahp.place(x=325,y=210)

#arbol decisiones
img_decisiones = Image.open("images\decisiones.jpg")
imagen_tk = ImageTk.PhotoImage(img_decisiones)
lb_decisiones = customtkinter.CTkLabel(app, image=imagen_tk,text="")
lb_decisiones.place(x=625,y=490)

#arbol- bajo incertidumbre
img_incertidumbre = Image.open("images\incertidumbre.jpg")
imagen_tk = ImageTk.PhotoImage(img_incertidumbre)
lb_ahp = customtkinter.CTkLabel(app, image=imagen_tk,text="")
lb_ahp.place(x=625,y=210)

#montecarlo
img_montecarlo = Image.open("images\Montecarlo.jpg")
imagen_tk = ImageTk.PhotoImage(img_montecarlo)
lb_arbol = customtkinter.CTkLabel(app, image=imagen_tk,text="")
lb_arbol.place(x=925,y=210)

#teoria de colas
img_colas = Image.open("images\Colas.jpg")
imagen_tk = ImageTk.PhotoImage(img_colas)
lb_colas = customtkinter.CTkLabel(app, image=imagen_tk,text="")
lb_colas.place(x=1225,y=210)

#geometrica
img_geo = Image.open("images\geometrica.jpg")
imagen_tk = ImageTk.PhotoImage(img_geo)
lb_geo = customtkinter.CTkLabel(app, image=imagen_tk,text="")
lb_geo.place(x=925,y=490)

#cuadratica
img_cua = Image.open("images\cuadratica.jpg")
imagen_tk = ImageTk.PhotoImage(img_cua)
lb_cua = customtkinter.CTkLabel(app, image=imagen_tk,text="")
lb_cua.place(x=1225,y=490)

#funciones
def funcion_cpm():
    archivo = "CPM.py"  # Reemplaza "ruta_del_archivo.py" por la ruta completa del archivo Python que deseas abrir
    subprocess.call(["python", archivo])
def funcion_pert():
    archivo = "PERT.py"  # Reemplaza "ruta_del_archivo.py" por la ruta completa del archivo Python que deseas abrir
    subprocess.call(["python", archivo])
def funcion_eoq():
    archivo = "EOQ_interfaz.py"  # Reemplaza "ruta_del_archivo.py" por la ruta completa del archivo Python que deseas abrir
    subprocess.call(["python", archivo])
def funcion_ahp():
    archivo = "AHP2.py"  # Reemplaza "ruta_del_archivo.py" por la ruta completa del archivo Python que deseas abrir
    subprocess.call(["python", archivo])
def combobox_decisiones(choice):
    if(choice == "Dibujar Árbol"):
        archivo = "arbol_grafico.py"  # Reemplaza "ruta_del_archivo.py" por la ruta completa del archivo Python que deseas abrir
        subprocess.call(["python", archivo])
    elif(choice == "Teoría de decisiones"):
        archivo = "arbol_decisiones.py"  # Reemplaza "ruta_del_archivo.py" por la ruta completa del archivo Python que deseas abrir
        subprocess.call(["python", archivo])
def funcion_incertidumbre():
    archivo = "incertidumbre.py"  # Reemplaza "ruta_del_archivo.py" por la ruta completa del archivo Python que deseas abrir
    subprocess.call(["python", archivo])
def funcion_montecarlo():
    archivo = "montecarlo.py"  # Reemplaza "ruta_del_archivo.py" por la ruta completa del archivo Python que deseas abrir
    subprocess.call(["python", archivo])
def funcion_colas():
    archivo = "colas.py"  # Reemplaza "ruta_del_archivo.py" por la ruta completa del archivo Python que deseas abrir
    subprocess.call(["python", archivo])
def combobox_eoq(choice):
    if(choice == "Inventarios"):
        archivo = "EOQ_interfaz.py"  # Reemplaza "ruta_del_archivo.py" por la ruta completa del archivo Python que deseas abrir
        subprocess.call(["python", archivo])
    elif(choice == "Descuento Cantidad"):
        archivo = "EOQ_Descuento_Cantidad.py"  # Reemplaza "ruta_del_archivo.py" por la ruta completa del archivo Python que deseas abrir
        subprocess.call(["python", archivo])
    elif(choice == "Ruptura"):
        archivo = "EOQ_Ruptura.py"  # Reemplaza "ruta_del_archivo.py" por la ruta completa del archivo Python que deseas abrir
        subprocess.call(["python", archivo])
def funcion_geometrica():
    archivo = "p_geo.py"  # Reemplaza "ruta_del_archivo.py" por la ruta completa del archivo Python que deseas abrir
    subprocess.call(["python", archivo])
def funcion_cuadratica():
    archivo = "p_cua.py"  # Reemplaza "ruta_del_archivo.py" por la ruta completa del archivo Python que deseas abrir
    subprocess.call(["python", archivo])  
#buttons
btn_cpm = customtkinter.CTkButton(app, text="Ejecutar", command=funcion_cpm, text_color_disabled="#556472",fg_color='#556472',font=('Montserrat',16))
btn_cpm.place(x=100,y=425)
btn_pert = customtkinter.CTkButton(app, text="Ejecutar", command=funcion_pert,text_color_disabled="#556472",fg_color='#556472',font=('Montserrat',16))
btn_pert.place(x=100,y=700)
#EOQ - SELECCION TIPO
combobox_eoqq = customtkinter.StringVar(value="EOQ Tipo 1")
cbb_eoq = customtkinter.CTkComboBox(app, values=["Inventarios", "Descuento Cantidad","Ruptura"],
                                     command=combobox_eoq, variable=combobox_eoqq,justify='center',text_color_disabled="#556472",fg_color='#556472',font=('Montserrat',16))
cbb_eoq.place(x=400,y=700)
combobox_eoqq.set("Ejecutar")
btn_ahp = customtkinter.CTkButton(app, text="Ejecutar",command=funcion_ahp,text_color_disabled="#556472",fg_color='#556472',font=('Montserrat',16))
btn_ahp.place(x=400,y=425)
combobox_deci = customtkinter.StringVar(value="EOQ Tipo 1")
cbb_decisiones = customtkinter.CTkComboBox(app, values=["Dibujar Árbol", "Teoría de decisiones",],
                                     command=combobox_decisiones, variable=combobox_deci,justify='center',text_color_disabled="#556472",fg_color='#556472',font=('Montserrat',16))
cbb_decisiones.place(x=700,y=700)
combobox_deci.set("Ejecutar")
btn_incertidumbre = customtkinter.CTkButton(app, text="Ejecutar",command=funcion_incertidumbre,text_color_disabled="#556472",fg_color='#556472',font=('Montserrat',16))
btn_incertidumbre.place(x=700,y=425)
btn_montecarlo = customtkinter.CTkButton(app, text="Ejecutar",command=funcion_montecarlo,text_color_disabled="#556472",fg_color='#556472',font=('Montserrat',16))
btn_montecarlo.place(x=1000,y=425)
btn_colas = customtkinter.CTkButton(app, text="Ejecutar",command=funcion_colas,text_color_disabled="#556472",fg_color='#556472',font=('Montserrat',16))
btn_colas.place(x=1300,y=425)
btn_geo = customtkinter.CTkButton(app, text="Ejecutar",command=funcion_geometrica,text_color_disabled="#556472",fg_color='#556472',font=('Montserrat',16))
btn_geo.place(x=1000,y=700)
btn_cua = customtkinter.CTkButton(app, text="Ejecutar",command=funcion_cuadratica,text_color_disabled="#556472",fg_color='#556472',font=('Montserrat',16))
btn_cua.place(x=1300,y=700)

app.mainloop()
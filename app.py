import customtkinter
from PIL import Image, ImageTk
import subprocess

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  
app.geometry("1280x720")

#frames
frame = customtkinter.CTkFrame(master=app, width=1250, height=180)
frame.place(x=20,y=20)

#imagen logo
# Carga la imagen desde un archivo
imagen = Image.open("images\logo.jpg")
tamano = (170,170)
imagen1 = imagen.resize(tamano)
# Convierte la imagen a un formato compatible con Tkinter
imagen_tk = ImageTk.PhotoImage(imagen1)

# Crea un widget de etiqueta y muestra la imagen en él
label = customtkinter.CTkLabel(app, image=imagen_tk,text="")
label.place(x=40,y=40)

#imagen banner
imagen = Image.open("images\logobanner.jpg")
tamano = (980,210)
imagen1 = imagen.resize(tamano)
imagen_tk = ImageTk.PhotoImage(imagen1)
lb_banner = customtkinter.CTkLabel(app, image=imagen_tk,text="")
lb_banner.place(x=300,y=30)

#cpm
cpm = customtkinter.CTkFrame(master=app, width=400, height=110)
cpm.place(x=20,y=210)
imagen = Image.open("images\cpm.jpg")
tamano = (400,120)
img_cpm = imagen.resize(tamano)
img_cpm = ImageTk.PhotoImage(img_cpm)
lb_cpm = customtkinter.CTkLabel(app, image=img_cpm,text="")
lb_cpm.place(x=50,y=210)

#pert
pert = customtkinter.CTkFrame(master=app, width=400, height=110)
pert.place(x=20,y=350)  
imagen = Image.open("images\pert.jpg")
tamano = (400,120)
imagen1 = imagen.resize(tamano)
imagen_tk = ImageTk.PhotoImage(imagen1)
lb_pert = customtkinter.CTkLabel(app, image=imagen_tk,text="")
lb_pert.place(x=50,y=350)

#eoq 
eoq = customtkinter.CTkFrame(master=app, width=400, height=110)
eoq.place(x=20,y=490)
imagen = Image.open("images\eoq.jpg")
tamano = (400,100)
imagen1 = imagen.resize(tamano)
imagen_tk = ImageTk.PhotoImage(imagen1)
lb_eoq = customtkinter.CTkLabel(app, image=imagen_tk,text="")
lb_eoq.place(x=50,y=510)

#ahp- certidumbre
ahp = customtkinter.CTkFrame(master=app, width=400, height=110)
ahp.place(x=450,y=210)
imagen = Image.open("images\Ahp.jpg")
tamano = (400,100)
imagen1 = imagen.resize(tamano)
imagen_tk = ImageTk.PhotoImage(imagen1)
lb_ahp = customtkinter.CTkLabel(app, image=imagen_tk,text="")
lb_ahp.place(x=490,y=210)

#arbol grafico
arbol = customtkinter.CTkFrame(master=app, width=400, height=110)
arbol.place(x=450,y=350)
imagen = Image.open("images\Arbol_grafico.jpg")
tamano = (400,100)
imagen1 = imagen.resize(tamano)
imagen_tk = ImageTk.PhotoImage(imagen1)
lb_arbol = customtkinter.CTkLabel(app, image=imagen_tk,text="")
lb_arbol.place(x=490,y=350)

#arbol decisiones
decisiones = customtkinter.CTkFrame(master=app, width=400, height=110)
decisiones.place(x=450,y=490)
imagen = Image.open("images\Arbol_decisiones.jpg")
tamano = (400,100)
imagen1 = imagen.resize(tamano)
imagen_tk = ImageTk.PhotoImage(imagen1)
lb_decisiones = customtkinter.CTkLabel(app, image=imagen_tk,text="")
lb_decisiones.place(x=490,y=510)

#arbol- bajo incertidumbre
ahp = customtkinter.CTkFrame(master=app, width=400, height=110)
ahp.place(x=870,y=210)
imagen = Image.open("images\Bajo_incertidumbre.jpg")
tamano = (400,100)
imagen1 = imagen.resize(tamano)
imagen_tk = ImageTk.PhotoImage(imagen1)
lb_ahp = customtkinter.CTkLabel(app, image=imagen_tk,text="")
lb_ahp.place(x=920,y=210)

#montecarlo


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
def funcion_grafico_arbol():
    archivo = "arbol_grafico.py"  # Reemplaza "ruta_del_archivo.py" por la ruta completa del archivo Python que deseas abrir
    subprocess.call(["python", archivo])
def funcion_decisiones():
    archivo = "arbol_decisiones.py"  # Reemplaza "ruta_del_archivo.py" por la ruta completa del archivo Python que deseas abrir
    subprocess.call(["python", archivo])
def funcion_incertidumbre():
    archivo = "incertidumbre.py"  # Reemplaza "ruta_del_archivo.py" por la ruta completa del archivo Python que deseas abrir
    subprocess.call(["python", archivo])

#buttons
btn_cpm = customtkinter.CTkButton(app, text="EJECUTAR", command=funcion_cpm)
btn_cpm.place(x=150,y=300)
btn_pert = customtkinter.CTkButton(app, text="EJECUTAR", command=funcion_pert)
btn_pert.place(x=150,y=450)
btn_eoq = customtkinter.CTkButton(app, text="EJECUTAR",command=funcion_eoq)
btn_eoq.place(x=150,y=600)
btn_ahp = customtkinter.CTkButton(app, text="EJECUTAR")
btn_ahp.place(x=590,y=300)
btn_arbol_grafico = customtkinter.CTkButton(app, text="EJECUTAR",command=funcion_grafico_arbol)
btn_arbol_grafico.place(x=590,y=450)
btn_decisiones = customtkinter.CTkButton(app, text="EJECUTAR",command=funcion_decisiones)
btn_decisiones.place(x=590,y=600)
btn_incertidumbre = customtkinter.CTkButton(app, text="EJECUTAR",command=funcion_incertidumbre)
btn_incertidumbre.place(x=1020,y=300)


#arbol

app.mainloop()
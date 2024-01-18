import customtkinter
from PIL import Image, ImageTk
import subprocess

app = customtkinter.CTk(fg_color='white')  
app.title("APP")
app.geometry("1280x720")


###
def combobox_callback(choice):
    if(choice == "EOQ Tipo 1"):
        
        cpm = customtkinter.CTkFrame(master=app, width=400, height=110)
        cpm.place(x=20,y=210)
        imagen = Image.open("images\cpm.jpg")
        tamano = (400,120)
        img_cpm = imagen.resize(tamano)
        img_cpm = ImageTk.PhotoImage(img_cpm)
        lb_cpm = customtkinter.CTkLabel(app, image=img_cpm,text="")
        lb_cpm.place(x=50,y=210)

    elif(choice == "EOQ Tipo 2"):
        pert = customtkinter.CTkFrame(master=app, width=400, height=110)
        pert.place(x=20,y=350)  
        imagen = Image.open("images\pert.jpg")
        tamano = (400,120)
        imagen1 = imagen.resize(tamano)
        imagen_tk = ImageTk.PhotoImage(imagen1)
        lb_pert = customtkinter.CTkLabel(app, image=imagen_tk,text="")
        lb_pert.place(x=50,y=350)

combobox_var = customtkinter.StringVar(value="EOQ Tipo 1")
combobox = customtkinter.CTkComboBox(app, values=["EOQ Tipo 1", "EOQ Tipo 2"],
                                     command=combobox_callback, variable=combobox_var)
combobox.place(x=300, y=200)
combobox_var.set("Elige el tipo EOQ")



###




combobox.place(x=0,y=10)


app.mainloop()


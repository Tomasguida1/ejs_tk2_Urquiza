from tkinter import *
from tkinter import ttk
from tkinter import messagebox
raiz = Tk()
raiz.title("reserva de mesas")
raiz.iconbitmap("C:\\Users\\Tomas\\Desktop\\ejstk2\\icono\\restaurant.ico")
raiz.geometry("640x427")
raiz.resizable(0,0)
raiz.resizable(False,False)
img = PhotoImage(file = "restaurant.png")
label = Label(raiz, image = img)
label.place(x = 0 , y = 0)
frame = Frame()
frame.pack()
frame.config(width = 300, height = 200)
frame.config(bg="lightblue")
frame.place(x = 0 , y = 0)
titulo = LabelFrame(raiz, text="reservar mesa",width = 290, height = 190,padx = 10, pady = 10)
titulo.config (bg="lightblue")
titulo.place(x = 0 , y = 0)
op = IntVar()

def abrirventana():
    messagebox.showinfo("enviado con exito","datos enviados con exito Te esperamos!")
    cerrar_ventana()
def cerrar_ventana():
    raiz.destroy()

desayuno = Radiobutton (raiz, text = "desayuno", variable= op,value = 1)
desayuno.place(x = 10 , y = 30)

almuerzo = Radiobutton (raiz, text = "almuerzo", variable= op,value = 2)
almuerzo.place(x = 100 , y = 30)

cena = Radiobutton (raiz, text = "cena", variable= op,value = 3)
cena.place(x = 200 , y = 30)

labeln = Label(raiz, text="A nombre de:")
labeln.place(x = 10 , y = 60)

tarjeta = Entry(raiz)
tarjeta.place(x = 90 , y = 60)

labelt = Label(raiz, text="Numero de telefono")
labelt.place(x = 10 , y = 90)

tarjeta = Entry(raiz)
tarjeta.place(x = 125 , y = 90)

labelc = Label(raiz, text="Cantidad de personas")
labelc.place(x = 10 , y = 120)

mesa = IntVar()
cantpersonas= (1,2,3,4,5,6)
combo = ttk.Combobox (raiz,textvariable=mesa, values = cantpersonas)
combo.place(x = 130 , y = 120)

boton1 = Button(raiz,text="Salir",bg="purple",command=cerrar_ventana).place(x = 100 , y = 150)
boton2 = Button(raiz,text="Enviar",bg="purple",command=abrirventana).place(x = 135 , y = 150)
raiz.mainloop()
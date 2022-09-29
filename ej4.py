from tkinter import *
from tkinter import ttk
from tkinter import messagebox
raiz = Tk()
raiz.title("Menú")
raiz.iconbitmap("C:\\Users\\Tomas\\Desktop\\ejstk2\\icono\\restaurant.ico")
raiz.geometry("640x427")
raiz.resizable(0,0)
raiz.resizable(False,False)

menub =Menu(raiz)
raiz.config(menu= menub, width=300, height=300)
def acercade():
    messagebox.showinfo("info","programa hecho usando la librería tkinter en python")
def licencia():
    messagebox.showinfo("licencia","programa hecho por Tomás Guida")
def mensaje():
    messagebox.showinfo("menú","Que disfrutes tu comida!")
    cerrar_ventana()
def cerrar_ventana():
    raiz.destroy()
opciones = Menu(menub, tearoff=0)
opciones.add_command(label="acerca de",command = acercade)
opciones.add_separator()
opciones.add_command(label="licencia",command = licencia)
menub.add_cascade(label="opciones", menu= opciones)
cuaderno = ttk.Notebook(raiz)
cuaderno.pack(fill="both", expand="yes")
p1 = Frame(cuaderno)
p2 = Frame(cuaderno)
p3 = Frame(cuaderno)
p4 = Frame(cuaderno)
p5 = Frame(cuaderno)
cuaderno.add(p1,text="entrada")
cuaderno.add(p2,text="plato principal")
cuaderno.add(p3,text="postre")
cuaderno.add(p4,text="bebidas")
cuaderno.add(p5,text="comentarios adicionales")
#pagina 1
img1 = PhotoImage(file = "restaurant2.png")
label1 = Label(p1, image = img1)
label1.place(x = 0 , y = 0)
labeln = Label(p1, text="Seleccione la entrada")
labeln.place(x = 250 , y = 100)

pl1 = StringVar()
platoe= ("empanadas de carne", "sopa de calabaza", "ensalada","bastoncitos de pescado")
combo1 = ttk.Combobox (p1,textvariable=pl1, values = platoe)
combo1.place(x = 250 , y = 130)

#pagina 2
img2 = PhotoImage(file = "restaurant2.png")
label2 = Label(p2, image = img2)
label2.place(x = 0 , y = 0)
labeln = Label(p2, text="Seleccione el plato principal")
labeln.place(x = 250 , y = 100)

pl2 = StringVar()
platop= ("fideos con tuco", "pizza fugazzeta", "milanesa con papas","tarta de verdura")
combo2 = ttk.Combobox (p2,textvariable=pl1, values = platop)
combo2.place(x = 250 , y = 130)

#pagina 3
img3 = PhotoImage(file = "restaurant2.png")
label3 = Label(p3, image = img3)
label3.place(x = 0 , y = 0)
labelpo = Label(p3, text="Seleccione el postre")
labelpo.place(x = 250 , y = 100)

pl3 = StringVar()
platopo= ("flan casero", "helado", "ensalada de frutas","budín de pan")
combo3 = ttk.Combobox (p3,textvariable=pl3, values = platopo)
combo3.place(x = 250 , y = 130)

#pagina 4
img4 = PhotoImage(file = "restaurant2.png")
label4 = Label(p4, image = img4)
label4.place(x = 0 , y = 0)
labelb = Label(p4, text="Seleccione la bebida")
labelb.place(x = 250 , y = 100)

op = IntVar()
gaseosa = Radiobutton (p4, text = "gaseosa", variable= op,value = 1)
gaseosa.place(x = 230 , y = 130)

jugo = Radiobutton (p4, text = "jugo", variable= op,value = 2)
jugo.place(x = 300 , y = 130)

cerveza = Radiobutton (p4, text = "cerveza", variable= op,value = 3)
cerveza.place(x = 350 , y = 130)

#pagina 5
img5 = PhotoImage(file = "restaurant2.png")
label5 = Label(p5, image = img5)
label5.place(x = 0 , y = 0)
labele = Label(p5, text="comentarios adicionales")
labele.place(x = 250 , y = 100)

adicionales = Entry(p5)
adicionales.place(x = 250 , y = 130)

boton = Button(p5,text="Enviar",bg="green",command=mensaje).place(x = 290 , y = 150)
raiz.mainloop()
from cProfile import label
from msilib.schema import ComboBox
from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title("Ingreso de usuario")
raiz.iconbitmap("C:\\Users\\Tomas\\Desktop\\ejstk2\\icono\\profile.ico")
raiz.geometry("200x170")
raiz.resizable(0,0)
raiz.resizable(False,False)
raiz.config(bg="green")
def verificar ():
    user = "admin"
    passw = "admin"
    user2 = "guida"
    passw2 = "guida"
    if (usuario.get() == user) or (usuario.get() == user2) and (contrasenia.get() == passw) or (contrasenia.get() == passw2) :
        texto = Label(raiz,text="se inicio la sesion correctamente").grid(row=7, column=2)
        raiz.iconify() 
        abrirventana()                                       
    else:
        texto = Label(raiz,text="usuario o contraseña incorrecta").grid(row=7, column=2) 

def abrirventana():
    ventana2 = Toplevel()
    ventana2.title("Ingreso de datos")
    ventana2.resizable(0,0)
    ventana2.geometry("300x500")
    ventana2.resizable(False,False)
    op = IntVar()
    def boton():
        texto = Label(ventana2,text="se recibieron los datos correctamente").grid(row=20, column=1)
    descripcion = Label(ventana2, text="ingrese apellido,nombre,domicilio,telefono y dni").grid(row=0, column=1)
    nombre = Entry(ventana2)
    nombre.insert(0,"nombre")
    nombre.grid (row=2, column=1, padx= 10 , pady=10)

    apellido = Entry(ventana2)
    apellido.insert(0,"apellido")
    apellido.grid (row=4, column=1)

    labeld = Label(ventana2, text="tipo de documento")
    labeld.grid (row=5, column=1)

    DNI = Radiobutton (ventana2, text = "DNI", variable= op,value = 1)
    DNI.grid (row=6, column=1)

    le = Radiobutton (ventana2, text = "LE", variable= op,value = 2)
    le.grid (row=7, column=1)

    lc = Radiobutton (ventana2, text = "LC", variable= op,value = 3)
    lc.grid (row=8, column=1)

    ci = Radiobutton (ventana2, text = "CI", variable= op,value = 4)
    ci.grid (row=9, column=1)

    pas = Radiobutton (ventana2, text = "PAS", variable= op,value = 5)
    pas.grid (row=10, column=1)

    nrodoc = Entry(ventana2)
    nrodoc.insert(0,"nrodoc")
    nrodoc.grid (row=11, column=1, padx= 10 , pady=10)

    labeld = Label(raiz, text="ingrese fecha de nacimiento (mes/dia/año)")
    labeld.grid (row=12, column=1)

    mes = StringVar()
    mesnac= ("enero","febrero","marzo","abril","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")
    combo = ttk.Combobox (ventana2,textvariable=mes, values = mesnac)
    combo.grid(row = 13, column=1, padx= 10 , pady=10)

    dia = IntVar()
    dianac= (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
    combo2 = ttk.Combobox (ventana2,textvariable=dia, values = dianac)
    combo2.grid(row = 14, column=1, padx= 10 , pady=10)

    anio = Entry(ventana2)
    anio.insert(0,"año")
    anio.grid (row=15, column=1, padx= 10 , pady=10)

    boton1 = Button(ventana2,text="Envíar",bg="red",padx=10,pady=10,command=boton).grid(row=18, column=1)
    ventana2.mainloop()
        
        
descripcion = Label(raiz, text="ingrese usuario y contraseña").grid(row=1, column=2)
usuario = Entry(raiz)
usuario.insert(0,"nombre usuario")
usuario.grid (row=2, column=2, padx= 10 , pady=10)
contrasenia = Entry(raiz)
contrasenia.insert(0,"contraseña")
contrasenia.grid (row=4, column=2, padx= 10 , pady=10)
contrasenia.config(show= "*")


boton1 = Button(raiz,text="Envíar",bg="red",padx=10,pady=10,command=verificar).grid(row=6, column=2)

raiz.mainloop()
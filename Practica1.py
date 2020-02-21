import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox as mBox
from tkinter import Menu

def personales():

    mBox.showinfo('Datos Personales','Nombre: '+ ' '+n.get()+' '+ pa.get()+' '+sa.get()+'\nDirección: '+d.get()+'\nColonia: '+col.get()+'\nCiudad: '+ciu.get()+'\nMunicipio: '+mun.get())

def acerca_de():
    mBox.showinfo('Información','Victoria Raquel Ruíz Madrigal\nSistemas Computacionales')

def imp():
    pas=""
    if opcion1.get()==1:
        pas+="Leer"
    elif opcion2.get()==1:
        pas+="Ver peliculas"
    elif opcion3.get()==1:
        pas+="Redes Sociales"
    elif opcion4.get()==1:
        pas+="Dibujar"
    elif opcion5.get()==1:
        pas+="Bailar"

    mBox.showinfo('Datos Personales','Nombre: '+ ' '+n.get()+' '+ pa.get()+' '+sa.get()+'\nDirección: '+d.get()+'\nColonia: '+col.get()+'\nCiudad: '+ciu.get()+'\nMunicipio: '+mun.get()+'\nPasatiempos: '+pas+'\nEstadoCivil: '+opcion.get())
def extras():
    pas=""
    if opcion1.get()==1:
        pas+="Leer"
    elif opcion2.get()==1:
        pas+="Ver peliculas"
    elif opcion3.get()==1:
        pas+="Redes Sociales"
    elif opcion4.get()==1:
        pas+="Dibujar"
    elif opcion5.get()==1:
        pas+="Bailar"
    mBox.showinfo("Segunda pestaña", "Pasatiempos: "+pas+"\nEstadoCivil: "+opcion.get())


ventana = tk.Tk()
ventana.title ("Sistema Escolar")

barra_menu = Menu (ventana )
ventana.config(menu = barra_menu)

opciones_menu = Menu (barra_menu)
opciones_menu1 = Menu (barra_menu)
opciones_menu.add_command (label="Imprimir", command=imp)
opciones_menu.add_command (label="Salir")
barra_menu.add_cascade(label="Sistema", menu = opciones_menu)
opciones_menu1.add_command (label="Acerca de", command=acerca_de)
barra_menu.add_cascade(label="Ayuda", menu = opciones_menu1)


tabControl = ttk.Notebook (ventana)
tab1= ttk.Frame(tabControl)
tabControl.add(tab1, text ="Datos Personales")
tabControl.grid(column=1, row=0)

boton = ttk.Button (tab1, text="Imprimir Datos Personales", command = personales)
boton.grid(column=3, row=9)

label1 = ttk.Label (tab1, text = "Nombre:").grid(column=1, row=1)
nombre = tk.StringVar()
n= ttk.Entry (tab1, width =20, textvariable=nombre)
n.grid(column=2, row=1)

label2 = ttk.Label (tab1, text = "Primer Apellido:") .grid(column=1, row=2)
primerA = tk.StringVar()
pa= ttk.Entry (tab1, width =20, textvariable=primerA)
pa.grid(column=2, row=2)

label3 = ttk.Label (tab1, text ="Segundo Apellido:").grid(column=1, row=3)
segundoA = tk.StringVar()
sa= ttk.Entry (tab1, width =20, textvariable=segundoA)
sa.grid(column=2, row=3)

label4 = ttk.Label (tab1, text ="Dirección:").grid(column=1, row=4)
direccion = tk.StringVar()
d= ttk.Entry (tab1, width =20, textvariable=direccion)
d.grid(column=2, row=4)

label5 = ttk.Label (tab1, text ="Colonia:").grid(column=1, row=5)
colonia = tk.StringVar()
col= ttk.Combobox (tab1, width =20, textvariable=colonia)
col['values']=("Adolfo Lopez Mateos", "Chapultepec Sur", "Guadalupe Victoria")
col.grid(column=2, row=5)


label6 = ttk.Label (tab1, text ="Ciudad:").grid(column=1, row=6)
ciudad = tk.StringVar()
ciu= ttk.Combobox (tab1, width =20, textvariable=ciudad)
ciu ['values']=("Leon", "Queretaro", "Guadalajara")
ciu.grid(column=2, row=6)

label7 = ttk.Label (tab1, text = "Municipio:").grid(column=1, row=7)
municipio = tk.StringVar()
mun = ttk.Combobox (tab1, width = 20, textvariable = municipio)
mun ['values']= ("Indaparapeo", "Morelia", "Lázaro Cárdenas")
mun.grid(column=2, row=7)


#SEGUNDA PESTAÑA

tab2= ttk.Frame(tabControl)
tabControl.add(tab2, text ="Datos Extras")

boton = ttk.Button (tab2, text = "Imprimir", command = extras)
boton.grid(column = 5, row = 10)


label1 = ttk.Label (tab2, text = "Pasatiempos:").grid(column=1, row=1)

opcion1 = tk.IntVar()
casilla1 = tk.Checkbutton(tab2, text = "Leer", variable = opcion1)
casilla1.deselect()
casilla1.grid(column = 1, row = 2)

opcion2 = tk.IntVar()
casilla2 = tk.Checkbutton(tab2, text = "Ver películas", variable = opcion2)
casilla2.deselect()
casilla2.grid(column = 2, row = 2)

opcion3 = tk.IntVar()
casilla3 = tk.Checkbutton(tab2, text = "Redes Sociales", variable = opcion3)
casilla3.deselect()
casilla3.grid(column = 3, row = 2)

opcion4 = tk.IntVar()
casilla4 = tk.Checkbutton(tab2, text = "Dibujar", variable = opcion4)
casilla4.deselect()
casilla4.grid(column = 4, row = 2)

opcion5 = tk.IntVar()
casilla5 = tk.Checkbutton(tab2, text = "Bailar", variable = opcion5)
casilla5.deselect()
casilla5.grid(column = 5, row = 2)


    

def est():

    selector = opcion.get()

label2 = ttk.Label (tab2, text = "Estado Civil:").grid(column=1, row=5)

opcion = tk.StringVar()
radio1 = tk.Radiobutton (tab2, text= "Casado", variable =opcion, value="Casado", command = est)
radio1.grid (column = 1,row = 6, sticky = tk.W)
radio1.select()

radio2 = tk.Radiobutton (tab2, text= "Soltero", variable =opcion, value="Soltero", command = est)
radio2.grid (column = 2,row = 6, sticky = tk.W)

radio3 = tk.Radiobutton (tab2, text= "Viudo", variable =opcion, value="viudo", command = est)
radio3.grid (column = 3,row = 6, sticky = tk.W)

radio4 = tk.Radiobutton (tab2, text= "Union libre", variable =opcion, value="Union Libre", command = est)
radio4.grid (column = 4,row = 6, sticky = tk.W)

radio3 = tk.Radiobutton (tab2, text= "Divorciado", variable =opcion, value="Divorciado", command = est)
radio3.grid (column = 5,row = 6, sticky = tk.W)

label = ttk.Label (tab2, text = "Objetivo de la vida").grid(column=1, row=8)
scroll_ancho=15
scroll_alto=2
caja = scrolledtext.ScrolledText(tab2, width = scroll_ancho, height = scroll_alto, wrap=tk.WORD)
caja.grid(column=1, row = 9)

ventana.mainloop()
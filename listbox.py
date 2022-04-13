from tkinter import *

elementos = ['Catrina','Phoebe', 'Mila', 'Coco', 'Flaco', 'Nora']

root = Tk()
root.title('Mascotas')

frame = Frame(root)
frame.pack(fill = 'both')

etiqueta = Label(frame,text='Selecciona el nombre de tu próxima mascota')
etiqueta.grid(column = 0, row = 0,sticky ='n')

frame2 = Frame(root)
frame2.pack(fill = 'both')
lista_elementos = StringVar(value = elementos)
listbox = Listbox(frame2, listvariable = lista_elementos)
listbox.grid(column = 0, row = 1, padx= 50,pady= 10, sticky = 'w')

root.mainloop()

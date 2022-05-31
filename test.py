import tkinter
def funcion():
    print ("Victor")
root = tkinter.Tk()
root.geometry('200x200')
boton = tkinter.Button(root, text="Cual es tu nombre", command=funcion)
boton.pack()
root.mainloop()
from tkinter import *
from tkinter import ttk,messagebox        
 

from pip import main
from setuptools import Command

from clases.CARPETA import CARPETA
from settings.settings import CARPETA_ADDRESS

class App(ttk.Frame):
        
    def __init__(self, master=None):
        super().__init__(master)   
        
        self.master.iconbitmap('./resource/isotipo.ico')
        self.master.title("Humanly Software - Imagenologia")
        self.master.geometry("800x300")
        
        
        self.boton = Button(self.master, text="Cual es tu nombre", command=self.saludar)
        self.boton.pack()
        self.boton.place(x=650,y=35)
        
        self.init()
        
        
    def saludar(self):
        
        nuevo_ruta = f"{CARPETA_ADDRESS}\\{self.combo.get()}"
        
        
        
        carpeta = CARPETA(nuevo_ruta)
        lis = carpeta.files_List()
        
        
        contador = 1
        for item in lis:
            self.listbox.insert(contador,item)
            contador+=1
            
        
        
        

    
    def init(self):
        self.combobox_udns()
        self.list_dicom()
                                   
    def font_size_general(self):
       return ("Arial",12)
        
        
    def combobox_udns(self):
        data = CARPETA(CARPETA_ADDRESS)
        
        folder_list =  data.handle_folder_list()
        
        self.label=ttk.Label(self.master, text= "sucursal", font = self.font_size_general())
        self.label.pack()
        self.label.place(x=25,y=15)

        self.combo = ttk.Combobox(self.master, values = folder_list, state = "readonly",width= 100)
        self.combo.set("Seleccionar")
        self.combo.place(x = 20, y = 40)
        
        
    def list_dicom(self):
        self.listbox  = Listbox(self.master, width = 69, bg = "white",activestyle = 'dotbox', font = "Helvetica",fg = "yellow")                
        self.listbox.pack()
        self.listbox.place(x=20,y=80)
        





if __name__ == '__main__':    
    myapp = App()    
    myapp.mainloop()
    
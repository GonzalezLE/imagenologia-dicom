from tkinter import *
from tkinter import ttk,messagebox
from turtle import color
from tkcalendar import DateEntry
import datetime
 

from clases.CARPETA import CARPETA
from settings.settings import CARPETA_ADDRESS

class App(ttk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)   
        
        self.master.iconbitmap('./resource/isotipo.ico')
        self.master.title("Humanly Software - Imagenologia")
        self.master.geometry("800x300")
        self.master.resizable(0,0)
                
        self.init()
        
        
    def saludar(self):
        
        inicio = self.calendario_fecha_inicio.get_date()
        fin =  self.calendario_fecha_fin.get_date()
        
        
        nuevo_ruta = f"{CARPETA_ADDRESS}\\{self.combo.get()}"
        carpeta = CARPETA(nuevo_ruta)
        lis = carpeta.files_List()
        
        self.listbox.delete(0,'end')
        
        contador = 1
        for item in lis:
            self.listbox.insert(contador,item)
            contador+=1            


    def init(self):
        self.combobox_udns()
        self.list_dicom()
        self.handle_create_butto()
        self.handle_create_input_data()

                                   
    def font_size_general(self):
       return ("Arial",12)
        
        
    def combobox_udns(self):
        data = CARPETA(CARPETA_ADDRESS)
        
        folder_list =  data.handle_folder_list()
        
        self.label=ttk.Label(self.master, text= "Sucursal", font = self.font_size_general())
        self.label.pack()
        self.label.place(x=25,y=15)

        self.combo = ttk.Combobox(self.master, values = folder_list, state = "readonly",width= 45)
        self.combo.set("Seleccionar")
        self.combo.place(x = 20, y = 40)
        
        
    def list_dicom(self):
        self.listbox  = Listbox(self.master, width = 69, bg = "white",activestyle = 'dotbox', font = "Helvetica")                
        self.listbox.pack()
        self.listbox.place(x=20,y=80)


    def handle_create_butto(self):        
        self.boton = Button(self.master, text="Ver lista", command=self.saludar)
        self.boton.pack()
        self.boton.place(x=650,y=35)
        
        
    def get_date(self):
        currentDatatime = datetime.datetime.now()
        date = currentDatatime.date()
        return date.year, date.month, date.day
    
    
    def handle_create_input_data(self):
        self.label_fecha_inicio=ttk.Label(self.master, text= "Fecha inicio", font = self.font_size_general())
        self.label_fecha_inicio.pack()
        self.label_fecha_inicio.place(x=350,y=15)
        
        anio, mes , dia = self.get_date()
        self.calendario_fecha_inicio = DateEntry(
            self.master,
            width=12,
            month= mes-1,
            background='#ef8133',
            foreground='#ffffff',
            borderwidth=5,
            )
        self.calendario_fecha_inicio.pack()
        self.calendario_fecha_inicio.place(x=350 ,y=40)
        
        
        self.label_fecha_fin=ttk.Label(self.master, text= "Fecha fin", font = self.font_size_general())
        self.label_fecha_fin.pack()
        self.label_fecha_fin.place(x=480,y=15)
        
        self.calendario_fecha_fin = DateEntry(
            self.master,
            width=12,                        
            background='#ef8133',
            foreground='#ffffff',
            borderwidth=5,
            )
        self.calendario_fecha_fin.pack()
        self.calendario_fecha_fin.place(x=480 ,y=40)
        
        
        
        
        





if __name__ == '__main__':    
    myapp = App()    
    myapp.mainloop()
    
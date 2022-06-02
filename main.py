import os
import re
from tkinter import *
from tkinter import ttk,messagebox
from turtle import color
from tkcalendar import DateEntry
import datetime
 

from clases.CARPETA import CARPETA
from settings.settings import CARPETA_ADDRESS,FOLDER_UDN

class App(ttk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)   
        
        self.master.iconbitmap('./resource/isotipo.ico')
        self.master.title("Humanly Software - Imagenologia")
        self.master.geometry("800x300")
        self.master.resizable(0,0)
                
        self.init()
        
        
    def find_dicom(self):
        
        inicio = self.calendario_fecha_inicio.get_date()
        inicio = str(inicio)
                        
        year,month,day= inicio.split('-')        
        filter = f'{year[2]}{year[3]}{month}'
                        
        nuevo_ruta = f"{CARPETA_ADDRESS}\\{self.combo.get()}"
        carpeta = CARPETA(nuevo_ruta)
        
        lis = carpeta.files_List(filter)
        
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
   
    
    def modification_date(filename): 
        t = os.path.getmtime(filename) 
        return datetime.datetime.fromtimestamp(t)
        
        
    def combobox_udns(self):
        data = CARPETA(CARPETA_ADDRESS)
        
        folder_list =  data.handle_folder_list()
        
        folder_list_filter =[]
        
        for folder in folder_list:
            if folder in FOLDER_UDN:
                folder_list_filter.append(folder)
                
                
        
        self.label=ttk.Label(self.master, text= "Sucursal", font = self.font_size_general())
        self.label.pack()
        self.label.place(x=25,y=15)

        self.combo = ttk.Combobox(self.master, values = folder_list_filter, state = "readonly",width= 45)
        self.combo.set("Seleccionar")
        self.combo.place(x = 20, y = 40)
        
        
    def list_dicom(self):
        self.listbox  = Listbox(self.master, width = 69, bg = "white",activestyle = 'dotbox', font = "Helvetica")                
        self.listbox.pack()
        self.listbox.place(x=20,y=80)


    def handle_create_butto(self):        
        self.boton = Button(self.master, text="Ver lista", command=self.find_dicom)
        self.boton.pack()
        self.boton.place(x=550,y=35)
        
        
    def get_date(self):
        currentDatatime = datetime.datetime.now()
        date = currentDatatime.date()
        return date.year, date.month, date.day
    
    
    def handle_create_input_data(self):
        self.label_fecha_inicio=ttk.Label(self.master, text= "Fecha a buscar", font = self.font_size_general())
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


        
if __name__ == '__main__':    
    myapp = App()    
    myapp.mainloop()
    
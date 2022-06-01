import os
import time
from turtle import width

class CARPETA():
    
    def __init__(self,folder_address):
        self._FOLDER_ADDRESS = folder_address
        
        
    def files_List(self):    
        
        content = os.listdir(self._FOLDER_ADDRESS)
        
        respuesta = []
        for file in content:
            
            full_route = fr"{self._FOLDER_ADDRESS}\{file}"
            
            ti_c = os.path.getctime(full_route)             
            print(ti_c)
            
            
            c_ti = time.ctime(ti_c)                                             
            
            
            
            
            
            respuesta.append(f"{full_route}{c_ti}")
            # print(full_route,c_ti)

        return respuesta
            
    def handle_folder_list(self):    
    
        with os.scandir(self._FOLDER_ADDRESS) as ficheros:
            subdirectorios = [fichero.name for fichero in ficheros if fichero.is_dir()]
        
        return subdirectorios
            
        
        
        
        
        
            
    
        
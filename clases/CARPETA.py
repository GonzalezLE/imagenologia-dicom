from datetime import datetime
import os.path,time
from turtle import width
import re
class CARPETA():
    
    def __init__(self,folder_address):
        self._FOLDER_ADDRESS = folder_address
        
        
    def modification_date(filename): 
        t = os.path.getmtime(filename) 
        return datetime.datetime.fromtimestamp(t)        
    
        
    def files_List(self ,patron='211116'):            
        
        content = os.listdir(self._FOLDER_ADDRESS)        
        respuesta = []
        
        for file in content:
            
            full_route = fr"{self._FOLDER_ADDRESS}\{file}"
                        
            if re.search(patron,full_route):                               
                respuesta.append(f"{full_route}")
            

        return respuesta
            
    def handle_folder_list(self):    
    
        with os.scandir(self._FOLDER_ADDRESS) as ficheros:
            subdirectorios = [fichero.name for fichero in ficheros if fichero.is_dir()]
        
        return subdirectorios
            
        
        
        
        
        
            
    
        
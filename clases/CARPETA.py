import os
import time
from turtle import width

class CARPETA():
    
    def __init__(self,folder_address):
        self._FOLDER_ADDRESS = folder_address
        
        
    def files_List(self):    
        
        content = os.listdir(self._FOLDER_ADDRESS)
        
        for file in content:
            
            full_route = fr"{self._FOLDER_ADDRESS}\{file}"
            
            ti_c = os.path.getctime(full_route)             
            
            c_ti = time.ctime(ti_c)                                             
            print(full_route,c_ti)
            
            
    def Folder_list(self):    
    
        with os.scandir(self._FOLDER_ADDRESS) as ficheros:
            subdirectorios = [fichero.name for fichero in ficheros if fichero.is_dir()]
        
        print(subdirectorios)
            
        
        
        
        
        
            
    
        
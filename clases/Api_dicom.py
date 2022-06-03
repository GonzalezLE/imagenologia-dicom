import requests


class Api_dicom():
    def __init__(self, url):
        self.url = url
        
    def  insert(self,json):
        try:            
            respuesta=requests.post(self.url,data=json)                
            if respuesta.status_code == 200:
                print(respuesta.text)
                return True
            else:
                return False
        except requests.exceptions.ConnectionError as errc:
            print(errc)
            return False
        









        
        
import requests
import app

class Apimed():
    
    
    def __init__(self, url):
        self.url = url        
    
    def mostrar_profesionales():
        url = "http://localhost:5000/medicos"
        r = requests.get(url)
        try:
            r.status_code == 200
            data = r.json()     
            print(data)
            print("¡Profesionales mostrados con Exito!")        
        except:
            print("Error en la conexión, no se pueden mostrar profesionales!")

    def mostrar_profesional(id):
        url = f"http://localhost:5000/medicos/{id}"
        r = requests.get(url)   
        try:            
            r.status_code == 200
            data = r.json()     
            print(data)
            print("¡Profesional mostrado con Exito!")
        except:
            print("Error en la conexión, no se puede mostrar el profesional!")  

    def registrar_especialista(json_data):    
        
        headers = {'Content-Type': 'application/json'}                
        url = "http://localhost:5000/medicos"
        r = requests.post(url, data=json_data, headers=headers)
        try:
            r.status_code == 200
            data = r.json()     
            print(data)
            print("¡Profesional creado con Exito!")  
        except:
            print('Error en la conexión, no se puede crear el profesional!')        

    def actualizar_especialista(id, json_data):
        headers = {'Content-Type': 'application/json'}
        url= f"http://localhost:5000/medicos/{id}"
        r = requests.put(url, data=json_data, headers = headers)
        try:
            r.status_code == 200
            data = r.json()     
            print(data)
            print("Datos del profesional actualizados")  
        except:
            print('Error al actualizar los datos')

    def eliminar_especialista(id):

        url= f"http://localhost:5000/medicos/{id}"
        r = requests.delete(url)      
        try:
            r.status_code == 200
            data = r.json()     
            print(data)
            print("¡Profesional eliminado con Exito!")  
        except:
            print('Error al eliminar los datos')

    


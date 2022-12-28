import requests
# from flask import Flask, jsonify, request
# import json



class Api():
    
    
    def __init__(self, url):
        self.url = url        
    
    def mostrar_productos():
        url = "http://localhost:5000/productos"
        try:
            response = requests.get(url)
            # Para mostrar conexion = print(response)
            # Para mostrar en formato json = response = response.json()            
            print(response.text)        
            #print(response.status_code)
        except:
            print("Error, no se puede mostrar productos en este momento!")

    def mostrar_producto(id):
        url = f"http://localhost:5000/productos/{id}"   
        try:            
            response = requests.get(url)
            # Para mostrar en formato json = response = response.json()            
            print(response.text)
        except:
            print('Error al intentar mostrar los datos')  

    def crear_producto(json_data):    
        
        headers = {'Content-Type': 'application/json'}                
        url = "http://localhost:5000/productos"
        try:
            response = requests.post(url, data=json_data, headers=headers)
            # Para mostrar en formato json = response = response.json()        
            print(response.text)
            print('Los datos del producto que seleccionaste fueron ingresados correctamente')
        except:
            print('Error, no se pudo crear el nuevo producto')        

    def actualizar_producto(id, json_data):
        headers = {'Content-Type': 'application/json'}
        url= f"http://localhost:5000/productos/{id}"
        
            
        try:
            response = requests.put(url, data=json_data, headers = headers)
            # Para mostrar en formato json = response = response.json()
            print(response.text)
            response.status_code == 200
            print('Los datos del producto que seleccionaste fueron actualizados correctamente')
        except:
            print('Error al actualizar los datos')

    def eliminar_producto(id):

        url= f"http://localhost:5000/productos/{id}"      

        try:
            response = requests.delete(url)
            response.status_code == 204
            print('Los datos del producto que seleccionaste fueron eliminados correctamente')
        except:
            print('Error al eliminar los datos')

        


url = "http://localhost:5000/productos"
obj = Api(url)

    


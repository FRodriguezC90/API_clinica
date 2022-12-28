from api_conector import Apimed
import json


import os
def limpiarpantalla():
    os.system('cls')

class Menu:
    def __init__():
        print('''
        ================BIENVENIDO==============
        1) Muestre a todos los profesionales.-
        2) Mostrar un profesional.-
        3) Crear un nuevo profesional.-         
        4) Editar un profesional.-               
        5) Elimine un profesional.-               
        ''')
        op = input("""=======Seleccione un Número=====\n""").capitalize()        
        limpiarpantalla()      
        if op == '1':           
            print("Muestre a todos los profesionales...")
            Apimed.mostrar_profesionales()
            input("""Presiona una tecla para continuar""")
            limpiarpantalla()
            Menu.__init__()
        
        elif op == '2':
            id = int(input("Ingrese el id del profesional\n"))
            limpiarpantalla()
            input("""Mostrar un profesional...""")
            Apimed.mostrar_profesional(id)
            input("""Presiona una tecla para continuar""")
            limpiarpantalla()
            Menu.__init__()
        elif op == '3':
            input("""Crear un nuevo profesional...""")
            id = int(input("Ingrese el id del nuevo profesional:\n"))
            Especialidad = input("Ingrese la especialidad del profesional:\n")
            Nombre = input("Ingrese el nombre del profesional:\n")
            Egresado = input("Ingrese lugar de egreso del profesional:\n")
            Edad = int(input("Ingrese Edad de Profesional:\n"))
            data = {'id': id, "Especialidad": Especialidad, "Nombre": Nombre, "Egresado": Egresado, "Edad": Edad}
            json_data = json.dumps(data)
            limpiarpantalla()            
            input("""Profesional Añadido correctamente""")
            print(json_data)
            Apimed.registrar_especialista(json_data)
            input("""Presiona una tecla para continuar""")
            limpiarpantalla()
            Menu.__init__()           
        elif op == '4':
            input("""Editar un profesional...""")
            id = int(input("Ingrese el id del profesional que desea modificar:\n"))
            Apimed.mostrar_profesionales(id)
            Especialidad = input("Ingrese la nueva especialidad del profesional:\n")
            Nombre = input("Ingrese el nuevo nombre del profesional:\n")
            Egresado = input("Ingrese nuevo lugar de egreso del profesional:\n")
            Edad = int(input("Ingrese la nueva edad de Profesional:\n"))
            data = {'id': id, "Especialidad": Especialidad, "Nombre": Nombre, "Egresado": Egresado, "Edad": Edad}
            json_data = json.dumps(data)
            limpiarpantalla()
            input("""Profesional modificado!""")
            Apimed.actualizar_especialista(id, json_data)
            input("""Presiona una tecla para continuar""")
            limpiarpantalla()
            Menu.__init__()           
        elif op == '5':
            input("""Eliminar un profesional...""")
            id = int(input("Ingrese el id del profesional que desea eliminar"))
            Apimed.eliminar_especialista(id)
            limpiarpantalla()
            Menu.__init__()
        else:
            input("""Intentelo denuevo""")
            limpiarpantalla()            
            pass
Menu.__init__()
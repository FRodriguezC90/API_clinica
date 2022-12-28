from api_conector import Api
import json


import os
def limpiarpantalla():
    os.system('cls')

class Menu:
    def __init__():
        print('''
        ====================MENU=================
        = a) Mostrar los productos disponibles  =
        = b) Mostrar un producto en especifico  =
        = c) Crear un nuevo producto            =
        = d) Editar un producto                 =
        = e) Eliminar un producto               =
        =========================================
        =========================================
        =    Para salir del programa presione   =
        =        cualquier tecla !!!            =
        =========================================
        ''')
        op = input("""
        =========================================
        ==========Ingrese una opcion=============
        =========================================\n----->       
        """).capitalize()        
        limpiarpantalla()      
        if op == 'A':           
            print("===============TODOS LOS PRODUCTOS===============")
            Api.mostrar_productos()
            input("""
            ==============================================
            ========PRESIONE ENTER PARA CONTINUAR!========
            ==============================================
            """)
            limpiarpantalla()
            Menu.__init__()
        
        elif op == 'B':
            id = int(input("Ingrese el id del producto que desea mostrar (Ej: 1, 2, 3, 4, 5, 6, 7, 8...):\n---->"))
            limpiarpantalla()
            print("""        
            =============PRODUCTO SELECCIONADO============
            """)
            Api.mostrar_producto(id)
            input("""
            ==============================================
            ========PRESIONE ENTER PARA CONTINUAR!========
            ==============================================
            """)
            limpiarpantalla()
            Menu.__init__()
        elif op == 'C':
            id = int(input("Ingrese el id del nuevo producto (Ej: 10, 11, 12, 13, 14...):\n----->"))
            nombre = input("Ingrese el nombre del nuevo producto:\n----->")
            descripcion = input("Ingrese una descripción para el nuevo producto:\n----->")
            valor = int(input("Ingrese un valor para el nuevo producto:\n----->"))
            data = {'id': id, 'nombre': nombre, 'descripcion': descripcion, 'valor': valor}
            json_data = json.dumps(data)
            limpiarpantalla()            
            print("""
            ====================PRODUCTO CREADO========================
            """)
            print(json_data)
            input("""
            ===========PRESIONE ENTER PARA VER LA NUEVA LISTA==========
            """)
            Api.crear_producto(json_data)
            input("""
            ==============================================
            ========PRESIONE ENTER PARA CONTINUAR!========
            ==============================================
            """)
            limpiarpantalla()
            Menu.__init__()           
        elif op == 'D':
            id = int(input("Ingrese el id del producto que desea modificar (1, 2, 3, 4, 5, 6...):\n----->"))
            Api.mostrar_producto(id)
            nombre = input("Ingrese el nuevo nombre o mantenga el anterior:\n----->")
            descripcion = input("Ingrese nueva descripción o mantenga la anterior:\n----->")
            valor = int(input("Ingrese un nuevo valor o mantenga el anterior:\n----->"))            
            data = {'id': id, 'nombre': nombre, 'descripcion': descripcion, 'valor': valor}
            json_data = json.dumps(data)
            limpiarpantalla()
            print("""
            ==================PRODUCTO MODIFICADO======================
            """)
            Api.actualizar_producto(id, json_data)
            input("""
            ==============================================
            ========PRESIONE ENTER PARA CONTINUAR!========
            ==============================================
            """)
            limpiarpantalla()
            Menu.__init__()           
        elif op == 'E':
            id = int(input("Ingrese el id del producto que quiere eliminar (1, 2, 3, 4, 5, 6, 7, 8.....):\n----->"))
            Api.eliminar_producto(id)
            Api.mostrar_productos()
            input("""
            ==============================================
            ========PRESIONE ENTER PARA CONTINUAR!========
            ==============================================
            """)
            limpiarpantalla()
            Menu.__init__()
        else:
            input("""
            ==============================================
            ====================ADIOS!====================
            ==============================================\n\n
            presione Enter\n----->
            """)
            limpiarpantalla()            
            pass
Menu.__init__()
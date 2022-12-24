#  API =        Lugar para disponibilizar recursos y/o funciones

# 1. Objetivo:  Crear una API para consulta, creación, edición de
# una clinica y sus especialistas

# 2. URL Base:  localhost
#               
# 3. Endpoints:
#    -localhost/api_clinica (GET)
#    -localhost/api_clinica/id (POST)
#    -localhost/api_clinica/id (GET)
#    -localhost/api_clinica/id (PUT)
#    -localhost/api_clinica/id (DELETE)

# 4. Que recursos: Medicos

from flask import Flask, jsonify, request 
 
app =  Flask(__name__)

medicos = [
    {
        "id" : 1,
        "Especialidad" : "Traumatologo",
        "Nombre"       : "Arturo Salas Lobos",
        "Egresado"     : "Universidad de Concepcion",
        "Edad"         : 32  
    },
    {
        "id" : 2,
        "Especialidad" : "Cardiologo",
        "Nombre"       : "Pia Fernandez Lagos",
        "Egresado"     : "Universidad de Chile",
        "Edad"         : 45  
    },
    {
        "id" : 3,
        "Especialidad" : "Oftalmologo",
        "Nombre"       : "Daniel Vidal Perez",
        "Egresado"     : "Universidad Catolica",
        "Edad"         : 35  
    },
]

# Consultar (todos)
@app.route('/medicos',methods=['GET'])
def obtener_medicos():
    return jsonify(medicos)

# Consultar (id)
@app.route('/medicos/<int:id>',methods =['GET'])
def obtener_medicos_id(id):
    for medico in medicos:
        if medico.get('id') == id:
            return jsonify(medico)

# Editar por id
@app.route('/medicos/<int:id>',methods =['PUT'])
def editar_medicos_id(id):
    medico_edit = request.get_json()
    for indice, medico in enumerate(medicos):
        if medico.get('id') == id:
            medicos[indice].update(medico_edit)
            return jsonify(medicos[indice])

# Agregar medico
@app.route('/medicos',methods =['POST'])
def agregar_medico():
    nuevo_medico = request.get_json()
    medicos.append(nuevo_medico)

    return jsonify(medicos)

# Borrar medico
@app.route('/medicos/<int:id>',methods =['DELETE'])
def borrar_medico(id):
    for indice, medico in enumerate(medicos):
        if medico.get("id") == id:
            del medicos[indice]
    
    return jsonify(medicos)





app.run(port=5000, host='localhost', debug= True)



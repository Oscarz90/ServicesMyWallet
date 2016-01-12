from ServicesMyWallet import app
from ServicesMyWallet import db

from flask import request

from bson import json_util

#Referencia a la coleccion usuario
usuario = db.usuario

#Obtencion de todos los Usuarios
@app.route("/usuarios", methods=['GET'])
def obtenerUsuarios():
  
  usuarios =usuario.find({"nombre":"Oscar"})
  
  respuesta_json = []
  
  for result in usuarios:
    respuesta_json.append(result)
  
  return json_util.dumps(usuarios,default=json_util.default)
  
  #return "obtenerUsuarios"

#Guardado de un usuario
@app.route("/usuarios", methods=['POST'])
def guardarUsuario():
  '''UsuarioInsertar={
                  "nickname": "Lorel",
                  "email": "lorel@live.com.mx",
                  "password": "lorel",
                  "nombre": "Lorel",
                  "apellido": "Sainez"'''
  #usuario.insert(UsuarioInsertar)
	#valores = request.get_json()
  print(request.json)
  return "hola"
  

#Obtencion de un usuario por id
@app.route("/usuarios/<id>", methods=['GET'])
def obtenerUsuarioPorId(id):
  return "obtenerUsuarioPorId"

#Actualizar un usuario por id
@app.route("/usuarios/<id>", methods=['PUT'])
def actualizarUsuarioPorId(id):
	return "actualizarUsuarioPorId"

#Eliminar un usuario por id
@app.route("/usuarios/<id>", methods=['DELETE'])
def eliminarUsuarioPorId(id):
	return "eliminarUsuarioPorId"
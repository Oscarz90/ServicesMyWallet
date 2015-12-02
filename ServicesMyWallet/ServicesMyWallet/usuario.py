import json
from ServicesMyWallet import app
from ServicesMyWallet import db
from bson import json_util
from bson.objectid import ObjectId

#Referencia a la coleccion usuario
usuario = db.usuario

#Obtencion de todos los Usuarios
@app.route("/usuarios", methods=['GET'])
def obtenerUsuarios():
  
  usuarios = usuario.find({})
  
  json_results = []
  
  for result in usuarios:
    json_results.append(result)

  return json.dumps(json_results, default=json_util.default)
  
  #return "obtenerUsuarios"

#Guardado de un usuario
@app.route("/usuarios", methods=['POST'])
def guardarUsuario():
	return "guardarUsuario"

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
from ServicesMyWallet import app
from ServicesMyWallet import db
from flask import request, jsonify ,json
#Serializar 
from bson.json_util import dumps


#Referencia a la coleccion usuario
usuario = db.usuario

#Obtencion de todos los Usuarios
@app.route("/usuarios", methods=['GET'])
def obtenerUsuarios():
  #Obtiene todos los usuarios
 
  usuarios =usuario.find()
  #Metodo 1
  #return dumps(usuarios)

  
  #Metodo 2
  respuesta=dumps(usuarios)
  #return jsonify(respuesta=respuesta)
  return jsonify({'respuesta':respuesta})
  #return json.dumps(respuesta)
  

  
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
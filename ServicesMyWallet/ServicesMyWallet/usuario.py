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
  print(type(respuesta))
  #return jsonify(respuesta=respuesta)
  return jsonify({'respuesta':respuesta})
  #return json.dumps(respuesta)
  

  
  #return "obtenerUsuarios"

#Guardado de un usuario
@app.route("/usuarios", methods=['POST'])
def guardarUsuario():
  peticion = request.get_json()
  print(peticion)
  print(request.json)

  resultado = usuario.insert_one(peticion)
  print(type(resultado.inserted_id))
  return jsonify({'respuesta': resultado.inserted_id})
  

#Obtencion de un usuario por id
@app.route("/usuarios/<nickname>", methods=['GET'])
def obtenerUsuarioPorId(nickname):
  respuesta= usuario.find_one({'nickname':nickname})
   #Metodo 2
  respuestaJson=dumps(respuesta)
  #return jsonify(respuesta=respuesta)
  return jsonify({'respuesta':respuestaJson})

#Actualizar un usuario por id
@app.route("/usuarios/<nickname>", methods=['PUT'])
def actualizarUsuarioPorId(nickname):
  peticion = request.get_json()
  resultado = usuario.update_one({'nickname':nickname},{'$set': {'nombre': peticion['nombre']}})
  return jsonify({'nose':'sabe'})

#Eliminar un usuario por id
@app.route("/usuarios/<id>", methods=['DELETE'])
def eliminarUsuarioPorId(id):
	return "eliminarUsuarioPorId"
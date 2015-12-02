import json
from ServicesMyWallet import app
#from ServicesMyWallet import db
from bson import json_util
from bson.objectid import ObjectId


#Referencia a la coleccion cartera
#cartera = db.cartera

#Obtencion de todas las Carteras
@app.route("/usuarios/<idUsuario>/carteras", methods=['GET'])
def obtenerCarteras(idUsuario):
  return "obtenerCarteras"

#Guardado de una cartera
@app.route("/usuarios/<idUsuario>/carteras", methods=['POST'])
def guardarCarteras(idUsuario):
	return "guardarCarteras"

#Obtencion de una cartera por id
@app.route("/usuarios/<idUsuario>/carteras/<idCartera>", methods=['GET'])
def obtenerCarteraPorId(idUsuario,idCartera):
	return "obtenerCarteraPorId"

#Actualizar una cartera por id
@app.route("/usuarios/<idUsuario>/carteras/<idCartera>", methods=['PUT'])
def actualizarCarteraPorId(idUsuario,idCartera):
	return "actualizarCarteraPorId"

#Eliminar una cartera por id
@app.route("/usuarios/<idUsuario>/carteras/<idCartera>", methods=['DELETE'])
def eliminarCarteraPorId(idUsuario,idCartera):
	return "eliminarCarteraPorId"

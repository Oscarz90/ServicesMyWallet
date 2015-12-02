import json
from ServicesMyWallet import app
#from ServicesMyWallet import db
from bson import json_util
from bson.objectid import ObjectId



#Referencia a la coleccion cartera
#cargo = db.cargo

#Obtencion de todas los cargos
@app.route("/usuarios/<idUsuario>/carteras/<idCartera>/cargos", methods=['GET'])
def obtenerCargos(idUsuario,idCartera):
  return "obtenerCargos"

#Guardado de un cargo
@app.route("/usuarios/<idUsuario>/carteras/<idCartera>/cargos", methods=['POST'])
def guardarCargos(idUsuario,idCartera):
  return "guardarCargos"+str(idUsuario)+" "+str(idCartera)

#Obtencion de un cargo por id
@app.route("/usuarios/<idUsuario>/carteras/<idCartera>/cargos/<idCargo>", methods=['GET'])
def obtenerCargoPorId(idUsuario,idCartera,idCargo):
  return "obtenerCargoPorId"

#Actualizar un cargo por id
@app.route("/usuarios/<idUsuario>/carteras/<idCartera>/cargos/<idCargo>", methods=['PUT'])
def actualizarCargoPorId(idUsuario,idCartera,idCargo):
  return "actualizarCargoPorId"

#Eliminar un cargo por id
@app.route("/usuarios/<idUsuario>/carteras/<idCartera>/cargos/<idCargo>", methods=['DELETE'])
def eliminarCargoPorId(idUsuario,idCartera,idCargo):
  return "eliminarCargoPorId"

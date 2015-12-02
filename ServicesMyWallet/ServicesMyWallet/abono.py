import json
from ServicesMyWallet import app
#from ServicesMyWallet import db
from bson import json_util
from bson.objectid import ObjectId



#Referencia a la coleccion cartera
#abono = db.abono

#Obtencion de todas los cargos
@app.route("/usuarios/<idUsuario>/carteras/<idCartera>/abonos", methods=['GET'])
def obtenerAbonos(idUsuario,idCartera):
  return "obtenerAbonos"

#Guardado de un cargo
@app.route("/usuarios/<idUsuario>/carteras/<idCartera>/abonos", methods=['POST'])
def guardarAbonos(idUsuario,idCartera):
  return "guardarAbonos"

#Obtencion de un cargo por id
@app.route("/usuarios/<idUsuario>/carteras/<idCartera>/abonos/<idAbono>", methods=['GET'])
def obtenerAbonoPorId(idUsuario,idCartera,idAbono):
  return "obtenerAbonoPorId"

#Actualizar un cargo por id
@app.route("/usuarios/<idUsuario>/carteras/<idCartera>/abonos/<idAbono>", methods=['PUT'])
def actualizarAbonoPorId(idUsuario,idCartera,idAbono):
  return "actualizarAbonoPorId"

#Eliminar un cargo por id
@app.route("/usuarios/<idUsuario>/carteras/<idCartera>/abonos/<idAbono>", methods=['DELETE'])
def eliminarAbonoPorId(idUsuario,idCartera,idAbono):
  return "eliminarAbonoPorId"

from flask import Flask
from pymongo import MongoClient

# Iniciar Aplicacion Flask
app = Flask(__name__)
# Conexion a Host de la Base de Datos
client = MongoClient('ds049864.mongolab.com:49864')
client.mywalletdb.authenticate('admin','ab472689')
# Obtencion Referencia a Base de Datos
db = client.mywalletdb

import ServicesMyWallet.usuario
import ServicesMyWallet.cartera
import ServicesMyWallet.cargo
import ServicesMyWallet.abono
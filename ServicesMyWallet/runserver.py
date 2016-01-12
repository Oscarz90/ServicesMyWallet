#Importar Aplicacion Flask del Paquete ServicesMyWallet
from ServicesMyWallet import app

if __name__ == "__main__":
	#Iniciar Aplicacion Flask en Modo debug
	app.run(debug=True)
### Flask a Python Framework

**1. Crear el directorio del Proyecto**
---
	$ mkdir MyRestAPI
	$ cd MyRestAPI
	
**2. Crear un entorno virtual**
---
Vamos a crear un entorno virtual (también llamado un virtualenv). Aislará la configuración Python/Flask en base de cada proyecto, lo que significa que cualquier cambio que realice en un sitio web no afectará a otros que también estés desarrollando.

#### Mac Os X, Linux y Windows

	$ python3 -m venv MyRestAPIEnv


Este comando creará una carpeta llamada "**_MyRestAPIEnv_**" que contiene nuestro entorno virtual básicamente un monton de archivos y carpetas.
 
**3. Activar el entorno Virtual**
---
Ahora activaremos nuestro entorno virtual para poder trabajar sobre él y que las configuraciones y descargas de paquetes que hagamos esten solamente en nuestro Proyecto y no de forma global.
#### Windows:
	C:\Users\Name\MyRestAPI> MyRestAPIEnv\Scripts\activate
#### Mac OS X y Linux:
	~/MyRestAPI $ . MyRestAPIEnv/bin/activate
Sabrás que tienes el entorno virtual activado cuando veas este mensaje en la consola:
#### Windows:
	(MyRestAPIEnv) C:\Users\Name\MyRestAPI>
#### Mac OS X y Linux:
	(MyRestAPIEnv) ~/MyRestAPI $

**4. Instalar Pip
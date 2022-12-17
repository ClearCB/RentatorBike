from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHeader, crearHtmlHead, crearCodigoHtml
from src.variables.variablesHtml import footerBase, headBase, headerBase, bodyMarcas
from src.capaNegocio.crearArchivos import crearArchivo

# En este módulo vamos a crear funciones que van a crear un archivo "marcas.html"

# Definimos el head de marcas.html
headMarcas = crearHtmlHead(headBase,"Marcas disponibles", "Página donde aparecen un link a todas las marcas disponibles", "cube, specialized, giant, cannondale, marca, brand, alquilar, rental, bike","../cssStyles/","marcas")

# Definimos el header de marcas.html
headerMarcas = crearHeader(headerBase,"../","")

# Definimos una función que ejecuta la función necesaria para crear el archivo correctamente.
def crearMarcasHtml():

    # Creamos el código html de marcas.html
    crearArchivo(crearCodigoHtml(headMarcas,headerMarcas,bodyMarcas,footerBase),".\\docs\\second_pages","marcas","html")
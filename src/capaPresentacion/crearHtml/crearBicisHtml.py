from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHeader, crearHtmlHead, crearCodigoHtml
from src.capaPresentacion.crearHtml.crearBodyHtml import bodyBicis
from src.variables.variablesHtml import footerBase, headBase, headerBase
from src.capaNegocio.crearArchivos import crearArchivo

# En este módulo vamos a crear funciones que van a crear un archivo "bicis.html" con el contenido html correcto

# Definimos variable headBicis
headBicis = crearHtmlHead(headBase,"Bicis disponibles", "Página donde aparecen todas las bicicletas disponibles", "bicicletas, disponible, up, down alquilar, rental, bike","../cssStyles/","bicis")

# Definimos variable headerBicis
headerBicis = crearHeader(headerBase,"../","")

# Definimos una función que ejecuta la función necesaria para crear el archivo correctamente.
def crearBicisHtml():

    crearArchivo(crearCodigoHtml(headBicis,headerBicis,bodyBicis(),footerBase),".\\docs\\second_pages","bicis","html")

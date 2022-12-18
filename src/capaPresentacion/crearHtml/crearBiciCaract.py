from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHeader, crearHtmlHead, crearCodigoHtml
from src.capaPresentacion.crearHtml.crearBodyHtml import bodyCaractirsticaHtml
from src.variables.variablesHtml import footerBase, headBase, headerBase
from src.capaNegocio.crearArchivos import crearArchivo

# En este módulo vamos a crear funciones que van a crear un archivo "bicisBicisCaract.html" con el contenido html correcto

# Definimos variable headBicisCaract
headBicisCaract= crearHtmlHead(headBase,"Bicicletas por caracteristica", "Página donde aparecen las bicicletas filtradas por sus caracteristica", "bicicletas, cuadro, talla, ruedas, tamaño, groupset","../cssStyles/","bicisfiltro")

# Definimos variable headerBicisCaract
headerBicisCaract = crearHeader(headerBase,"../","")

# Definimos una función que ejecuta la función necesaria para crear el archivo correctamente.
def crearBicisCaractHtml():

    crearArchivo(crearCodigoHtml(headBicisCaract,headerBicisCaract,bodyCaractirsticaHtml(),footerBase),".\\docs\\second_pages","biciscaracteristica","html")

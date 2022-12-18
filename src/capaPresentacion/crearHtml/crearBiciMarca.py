from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHeader, crearHtmlHead, crearCodigoHtml
from src.capaPresentacion.crearHtml.crearBodyHtml import bodyMarcaHtml
from src.variables.variablesHtml import footerBase, headBase, headerBase
from src.capaNegocio.crearArchivos import crearArchivo

# En este módulo vamos a crear funciones que van a crear un archivo "bicipormarca.html" con el contenido html correcto

# Definimos variable headbicipormarca
headBiciPorMarca = crearHtmlHead(headBase,"Bicis por marca", "Página donde aparecen todas las bicicletas filtradas por su marca", "bicicletas, marcas, specialized, cannondale, giant, cube, alquilar, rental, bike","../cssStyles/","bicisfiltro")

# Definimos variable headerBiciPorMarca
headerBiciPorMarca = crearHeader(headerBase,"../","")

# Definimos una función que ejecuta la función necesaria para crear el archivo correctamente.
def crearBiciMarcaHtml():

    crearArchivo(crearCodigoHtml(headBiciPorMarca,headerBiciPorMarca,bodyMarcaHtml(),footerBase),".\\docs\\second_pages","bicispormarca","html")
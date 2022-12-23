from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHeader, crearHtmlHead, crearCodigoHtml
from src.capaPresentacion.crearHtml.crearBodyHtml import bodyCategoriaHtml
from src.variables.variablesHtml import footerBase, headBase, headerBase
from src.capaNegocio.crearArchivos import crearArchivo

# En este módulo vamos a crear funciones que van a crear un archivo "biciscategoria.html" con el contenido html correcto

# Definimos variable headBiciCategoria
headBiciCateg = crearHtmlHead(headBase,"Bicicletas por categoría", "Página donde aparecen las bicicletas filtradas por su categoria", "bicicletas, tipos, mtb, carretera, electrica, ciudad, alquilar, rental, bike","../cssStyles/","bicisfiltro")

# Definimos variable headBiciCategoria
headerBiciCateg = crearHeader(headerBase,"../","")

# Definimos una función que ejecuta la función necesaria para crear el archivo correctamente.
def crearBiciCategoriaHtml():

    crearArchivo(crearCodigoHtml(headBiciCateg,headerBiciCateg,bodyCategoriaHtml(),footerBase),".\\docs\\second_pages","biciscategoria","html")

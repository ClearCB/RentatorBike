from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHtmlHead, crearHeader, crearCodigoHtml
from src.variables.variablesHtml import bodyIndex, footerBase, headBase, headerBase
from src.capaNegocio.crearArchivos import crearArchivo

# En este módulo vamos a crear funciones que van a crear un archivo "index.html"

# Definimos una variable de indexHead
indexHead = crearHtmlHead(headBase, "Rentator", "Página principal de un buscador de bicicletas para alquilar", "Bicicletas, inicio, index, alquilar, rental, bike","cssStyles/","index")

# Definimos una variable de indexHeader
indexHeader = crearHeader(headerBase, "","second_pages/")

# Definimos una función que ejecuta la función necesaria para crear el archivo correctamente.
def crearIndexHtml():

    # Creamos el archivo index.html con el codigo html en la ruta indicada
    crearArchivo(crearCodigoHtml(indexHead,indexHeader,bodyIndex,footerBase),".\\docs","index","html")

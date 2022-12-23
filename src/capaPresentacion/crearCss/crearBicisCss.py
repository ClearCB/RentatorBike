from src.capaNegocio.crearArchivos import crearArchivo
from src.variables.variablesCss import bicisCss

#Funcion que define el codigo css del archivo bicis.css
def bicisStylesCss():

    return bicisCss

#Funcion que crea el archivo bicis.css en la ruta indicada.
def crearBicisCss():
    crearArchivo(bicisStylesCss(), ".\\docs\\cssStyles", "bicis", "css")

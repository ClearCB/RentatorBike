from src.capaNegocio.crearArchivos import crearArchivo
from src.variables.variablesCss import marcasCss

#Funcion que define el codigo css del archivo marcas.css
def marcasStylesCss():

    return marcasCss

#Funcion que crea el archivo marcas.css en la ruta indicada.
def crearMarcasCss():

    crearArchivo(marcasStylesCss(), ".\\docs\\cssStyles", "marcas", "css")

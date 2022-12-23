from src.capaNegocio.crearArchivos import crearArchivo
from src.variables.variablesCss import bicisFiltroCss

#Funcion que define el codigo css del archivo bicisFiltro.css
def bicisfiltroStylesCss():

    return bicisFiltroCss


#Funcion que crea el archivo bicisFiltro.css en la ruta indicada.
def crearBicisFiltroCss():

    crearArchivo(bicisfiltroStylesCss(), ".\\docs\\cssStyles", "bicisfiltro", "css")


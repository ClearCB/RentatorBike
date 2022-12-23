from src.capaNegocio.crearArchivos import crearArchivo
from src.variables.variablesCss import biciSolitariaCss

#Funcion que define el codigo Css del archivo biciSolitaria.css
def biciSolitariaStylesCss():

    return biciSolitariaCss

#Funcion que crea el archivo biciSolitaria.css en la ruta indicada.
def crearBiciSolitariaCss():
    crearArchivo(biciSolitariaStylesCss(), ".\\docs\\cssStyles", "bicisolitaria", "css")


from src.capaPresentacion.crearCss.cssSecundarioUtilidades import indexStylesCss, bicisStylesCss, biciSolitariaStylesCss, marcasStylesCss, rentalsStylesCss, tiposStylesCss, bicisfiltroStylesCss
from src.capaNegocio.crearArchivos import crearArchivo

def crearBicisCss():
    crearArchivo(bicisStylesCss(), ".\\docs\\cssStyles", "bicis", "css")

def crearBiciSolitariaCss():
    crearArchivo(biciSolitariaStylesCss(), ".\\docs\\cssStyles", "bicisolitaria", "css")




def crearBicisFiltroCss():
    crearArchivo(bicisfiltroStylesCss(), ".\\docs\\cssStyles", "bicisfiltro", "css")




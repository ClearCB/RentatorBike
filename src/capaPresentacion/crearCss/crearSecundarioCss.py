from src.capaPresentacion.crearCss.cssSecundarioUtilidades import bicisStylesCss, biciSolitariaStylesCss, marcasStylesCss, rentalsStylesCss, tiposStylesCss, bicisfiltroStylesCss
from src.capaPresentacion.crearArchivos import crearArchivo

def crearBicisCss():
    crearArchivo(bicisStylesCss(), ".\\docs\\cssStyles", "bicis", "css")

def crearBiciSolitariaCss():
    crearArchivo(biciSolitariaStylesCss(), ".\\docs\\cssStyles", "bicisolitaria", "css")

def crearMarcasCss():
    crearArchivo(marcasStylesCss(), ".\\docs\\cssStyles", "marcas", "css")

def crearRentalsCss():
    crearArchivo(rentalsStylesCss(), ".\\docs\\cssStyles", "rentals", "css")

def crearTiposCss():
    crearArchivo(tiposStylesCss(), ".\\docs\\cssStyles", "tipos", "css")

def crearBicisFiltroCss():
    crearArchivo(bicisfiltroStylesCss(), ".\\docs\\cssStyles", "bicisfiltro", "css")

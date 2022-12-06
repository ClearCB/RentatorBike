from src.capaPresentacion.crearCss.cssSecundarioUtilidades import indexStylesCss, bicisStylesCss, biciSolitariaStylesCss, marcasStylesCss, rentalsStylesCss, tiposStylesCss, bicisfiltroStylesCss
from src.capaNegocio.crearArchivos import crearArchivo

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

def crearIndexCss():
    crearArchivo(indexStylesCss(), ".\\docs\\cssStyles", "index", "css")

def crearCssSecundario():

    crearBicisCss()
    crearBiciSolitariaCss()
    crearMarcasCss()
    crearRentalsCss()
    crearTiposCss()
    crearBicisFiltroCss()
    crearIndexCss()
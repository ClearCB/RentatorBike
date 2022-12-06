from src.capaPresentacion.crearCss.cssSecundarioUtilidades import indexStylesCss, bicisStylesCss, biciSolitariaStylesCss, marcasStylesCss, rentalsStylesCss, tiposStylesCss, bicisfiltroStylesCss
from src.capaNegocio.crearArchivos import crearArchivo





def crearBicisFiltroCss():
    crearArchivo(bicisfiltroStylesCss(), ".\\docs\\cssStyles", "bicisfiltro", "css")




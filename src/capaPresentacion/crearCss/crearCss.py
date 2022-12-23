from src.capaPresentacion.crearCss.crearBicisCss import crearBicisCss
from src.capaPresentacion.crearCss.crearBicisFiltroCss import crearBicisFiltroCss
from src.capaPresentacion.crearCss.crearBiciSolitariaCss import crearBiciSolitariaCss
from src.capaPresentacion.crearCss.crearIndexCss import crearIndexCss
from src.capaPresentacion.crearCss.crearMarcasCss import crearMarcasCss
from src.capaPresentacion.crearCss.crearRentalsCss import crearRentalsCss
from src.capaPresentacion.crearCss.funcionCssBase import crearCssBase

# Esta funcion nos creará todos los archivos css necesarios para nuestra pagina
def crearCss():

    crearBicisCss()
    crearBicisFiltroCss()
    crearBiciSolitariaCss()
    crearIndexCss()
    crearMarcasCss()
    crearRentalsCss()
    crearCssBase()

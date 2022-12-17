from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHeader, crearHtmlHead, crearCodigoHtml
from src.capaPresentacion.crearHtml.crearyBodyHtml import bodyRentalsHtml
from src.variables.variablesHtml import footerBase, headBase, headerBase
from src.capaNegocio.crearArchivos import crearArchivo

# En este módulo vamos a crear funciones que van a crear un archivo "rentals.html" con el contenido html correcto

# Definimos variable headRentals
headRentals = crearHtmlHead(headBase,"Rentals cercanos", "Página donde aparecen todos los rental de bikes cercanos", "bicicletas, alquilar, rental, bike, ubicacion, contacto, redes, sociales","../cssStyles/","rentals")

# Definimos variable headerRentals
headerRentals = crearHeader(headerBase, "../","")

# Definimos una función que ejecuta la función necesaria para crear el archivo correctamente.
def crearRentalsHtml():

    crearArchivo(crearCodigoHtml(headRentals,headerRentals,bodyRentalsHtml(),footerBase),".\\docs\\second_pages","rentals","html")
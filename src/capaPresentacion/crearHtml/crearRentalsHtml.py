from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHeader, crearHtmlHead
from src.capaPresentacion.crearHtml.crearyBodyHtml import crearBodyRentals
from src.capaPresentacion.variables.variablesHtml import footer
from src.capaNegocio.crearArchivos import crearArchivo

# En este módulo vamos a crear funciones que van a crear un archivo "rentals.html" con el contenido html correcto

# Definimos una funcion que unifica el html
def rentalsHtml():

    rentals = ''''''
    rentals += crearHtmlHead("Rentals cercanos", "Página donde aparecen todos los rental de bikes cercanos", "bicicletas, alquilar, rental, bike, ubicacion, contacto, redes, sociales","../cssStyles/","rentals")
    rentals += crearHeader("../","")
    rentals += crearBodyRentals()
    rentals += footer

    return rentals # Devolvemos la variable rentals que contiene el código del archivo rentals.html

# Definimos una función que ejecuta la función necesaria para crear el archivo correctamente.
def crearRentalsHtml():

    crearArchivo(rentalsHtml(),".\\docs\\second_pages","rentals","html")
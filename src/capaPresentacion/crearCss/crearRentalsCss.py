from src.capaNegocio.crearArchivos import crearArchivo
from src.variables.variablesCss import rentalsCss

#Funcion que define el codigo css del archivo rentals.css
def rentalsStylesCss():
    
    return rentalsCss

#Funcion que crea el archivo rentals.css en la ruta indicada.
def crearRentalsCss():
    crearArchivo(rentalsStylesCss(), ".\\docs\\cssStyles", "rentals", "css")

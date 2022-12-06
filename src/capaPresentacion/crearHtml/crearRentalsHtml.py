from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHeader, crearHtmlHead, crearFooter
from src.capaNegocio.crearArchivos import crearArchivo

# En este módulo vamos a crear funciones que van a crear un archivo "rentals.html"

# En primer lugar, creamos una función que devuelva el valor del body del rentals.html
def crearBodyRentals(listaRentals):

    # Definimos parte del body de rentals
    bodyRentals = ''''''

    # Recorremos la lista de los rentals para determinar los valores que queremos
    for rental in listaRentals:

        nombreRental = rental["company_name"]
        iconoRental = rental["icono"]
        direccionCalle = rental["address"]["street"]
        direccionZip = rental["address"]["zip"]
        direccionPais = rental["address"]["country"]
        direccionCiudad = rental["address"]["town"]
        contactoNum = rental["contact"]["num"]
        contactoEmail = rental["contact"]["email"]
        redesInsta = rental["social_media"]["instagram"]
        redesTwitter = rental["social_media"]["twitter"]
        bicisdisponibles = rental["bikes"]["bikes_up"]["_idbikes"]
        bicisnodisponibles = rental["bikes"]["bikes_down"]["_idbikes"]
        fotoRental = rental["img"]

        bodyRentals += f'''
            <div class="rentals">
                <div class="rentals__container">
                    <div class="rentals__titulo__logo">
                        <h3 class="rentals__titulo">
                            {nombreRental} 
                        </h3>
                        <div class="rentals__logo">
                            <img  class="rentalIcono" src="{iconoRental}" alt="foto del icono del rental {nombreRental}">
                        </div>
                    </div>
                    <div class="rentals__description">
                        <ul>
                            <li>Ubicacion: {direccionCalle}, {direccionCiudad} ({direccionPais}). {direccionZip}</li>
                            <li>Contacto: num({contactoNum}) / email({contactoEmail})</li>
                            <li>Redes sociales: instagram({redesInsta}) / twitter({redesTwitter})</li>
                            <li>Bicis disponibles:{bicisdisponibles}</li>
                            <li>Bicis no disponibles:{bicisnodisponibles}</li>
                        </ul>
                    </div>
                    <div class="rentals__img__location">
                        <a href="#"><img class=fotoRental src="{fotoRental}" alt="foto de la ubicacion del rental {nombreRental}"></a>
                    </div>
                </div>
            </div>'''

    return bodyRentals

# Definimos una funcion que unifica el html
def rentalsHtml(listaRentals):

    rentals = ''''''
    rentals += crearHtmlHead("Rentals cercanos", "Página donde aparecen todos los rental de bikes cercanos", "bicicletas, alquilar, rental, bike, ubicacion, contacto, redes, sociales","../cssStyles/","rentals")
    rentals += crearHeader("../","")
    rentals += crearBodyRentals(listaRentals)
    rentals += crearFooter()


    return rentals # Devolvemos la variable rentals que contiene el código del archivo rentals.html

# Definimos una función que ejecuta la función necesaria para crear el archivo correctamente.
def crearRentalsHtml(listaRentals):

    crearArchivo(rentalsHtml(listaRentals),".\\docs\\second_pages","rentals","html")
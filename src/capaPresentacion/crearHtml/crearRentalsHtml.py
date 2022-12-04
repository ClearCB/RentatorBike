from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHeader, crearHtmlHead, crearFooter
from src.capaDatos.listarDatosMongo import listarRentals

listaRentals = listarRentals()

def crearBodyRentalsTop():

    rentalsBodyHtmlTop ='''
        <section class="rental_lista">
            <h3 class="titleRental">Rentals disponibles</h3>
            <hr>
            <div class="rental_lista_div">
                <ul class="lista">
                '''

    return rentalsBodyHtmlTop

def crearBodyRentalsMid(listaRentals):

    rentalsBodyHtmlMid = ''''''
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

        rentalsBodyHtmlMid += f'''
                        <li class="rental"><h3> {nombreRental} <br><br><br><img  class="rentalIcono" src="{iconoRental}" alt="foto del icono del rental {nombreRental}"></h3> 
                            <ul class="contenidoDeRental">
                                <li class="imparLista">Ubicacion: calle {direccionCalle}, {direccionZip}. {direccionCiudad}, {direccionPais}</li>
                                <li class="parLista">Contacto: num ({contactoNum}) email ({contactoEmail})</li>
                                <li class="imparLista">Instagram:{redesInsta} /  Twitter: {redesTwitter}</li>
                                <li class="parLista">Bicis disponibles:{bicisdisponibles}</li>
                                <li class="imparLista">Bicis no disponibles:{bicisnodisponibles}</li>
                            </ul>
                            <a href="#"><img class=fotoRental src="{fotoRental}" alt="foto de la ubicacion del rental {nombreRental}"></a>
                        </li>'''

    return rentalsBodyHtmlMid


def crearBodyRentalsBot():
    rentalsBodyHtmlBot='''
                </ul>
            </div>
        </section>'''

    return rentalsBodyHtmlBot

def rentalsHtml():

    head = crearHtmlHead("Rentals cercanos", "Página donde aparecen todos los rental de bikes cercanos", "bicicletas, alquilar, rental, bike, ubicacion, contacto, redes, sociales","../cssStyles/","rentals")
    header = crearHeader("","../")
    bodyTop = crearBodyRentalsTop()
    bodyMid = crearBodyRentalsMid(listaRentals)
    bodyBot = crearBodyRentalsBot()
    footer = crearFooter()

    try:
        with open("C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\second_pages\\rentals.html","w", encoding="utf-8") as archivo:
            archivo.write(head)

    except FileNotFoundError:
        print("El directorio no existe, ejecuta correctamente el programa y vuelve a intentarlo.")

    else:
        with open("C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\second_pages\\rentals.html","a", encoding="utf-8") as archivo:
            archivo.write(header)
            archivo.write(bodyTop)
            archivo.write(bodyMid)
            archivo.write(bodyBot)
            archivo.write(footer)
            print("El archivo 'rentals.html' creado correctamente.")

rentalsHtml()
from src.capaPresentacion.crearHtml.funcionHtmlBase import crearContenedorRental
from src.capaDatos.listarDatosMongo import listarBicis, listarRentals, respuestaText
from src.capaDatos.peticionMongo import respuestaMongo
# En este modulo vamos a poner todos los "body" de las funciones que
# creen un body


datosMongo = respuestaText(respuestaMongo())
listaBicis = listarBicis(datosMongo)
listaRentals = listarRentals(datosMongo)

# Función que devuelve el valor del body del rentals.html
def crearBodyRentals(listaRentals):

    # Definimos parte del body de rentals
    bodyRentals = '''
        <h3 class="titleBicis"> Bicis disponibles </h3>
        <hr>
        <section>
            <div id="contenedorPadre">'''

    # Recorremos la lista de los rentals para determinar los valores que queremos en el contenedor
    for rental in listaRentals:

        bodyRentals+=crearContenedorRental(rental)

    bodyRentals +='''
            </div>
        </section>'''

    return bodyRentals

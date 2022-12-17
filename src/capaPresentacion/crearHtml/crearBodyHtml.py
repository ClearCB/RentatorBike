from src.capaDatos.listarDatosMongo import listarBicis, listarRentals, respuestaText
from src.capaDatos.peticionMongo import respuestaMongo
from src.capaPresentacion.crearHtml.funcionHtmlBase import crearContenedorRental
# En este modulo vamos a poner todos los "body" de las funciones que
# creen un body

respuesta = respuestaText(respuestaMongo()) 
listaBicis = listarBicis(respuesta)
listaRentals = listarRentals(respuesta)

# Función que construye el body del rentals.html
def crearBodyRentals(lista):

    # Definimos parte del body de rentals
    bodyRentals = '''
        <h3 class="titleBicis"> Bicis disponibles </h3>
        <hr>
        <section>
            <div id="contenedorPadre">'''

    # Recorremos la lista de los rentals para determinar los valores que queremos en el contenedor
    for rental in lista:

        bodyRentals+=crearContenedorRental(rental)

    bodyRentals +='''
            </div>
        </section>'''

    return bodyRentals

# Devuelve la variable del codigo html del body de rentals.html
def bodyRentalsHtml():

    return crearBodyRentals(listaRentals)

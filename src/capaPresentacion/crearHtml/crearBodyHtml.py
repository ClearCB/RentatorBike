from src.capaDatos.listarDatosMongo import listarBicis, listarRentals, respuestaText
from src.capaDatos.peticionMongo import respuestaMongo
from src.capaPresentacion.crearHtml.funcionHtmlBase import crearContenedorRental, crearContenedorBici
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

# Devuelve una variable con el html del body de rentals.html
def bodyRentals():

    return crearBodyRentals(listaRentals)

# Creamos una función que devuelva el valor del body del bicis.html
def crearBodyBicis(lista):

    # Definimos parte del body html
    bicisBodyHtml ='''
        <h3 class="titleBicis"> Bicis disponibles </h3>
        <hr>
        <section>
            <div id="contenedorPadre">'''
    
    for bici in lista: # Recorremos la lista de las bicis para conseguir los valores que queremos

        bicisBodyHtml += crearContenedorBici(bici)
    
    bicisBodyHtml+='''
            </div>
        </section>'''

    return bicisBodyHtml

# Devuelve una variable con el html del body de bicis.html
def bodyBicis():

    return crearBodyBicis(listaBicis)
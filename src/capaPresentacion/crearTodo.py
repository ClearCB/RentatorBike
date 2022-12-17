from src.capaDatos.listarDatosMongo import listarBicis, listarRentals, respuestaText
from src.capaDatos.peticionMongo import respuestaMongo
from src.capaPresentacion.crearHtml.crearBiciSolitariaHtml import crearBiciSolitariaHtml
from src.capaPresentacion.crearHtml.crearRentalsHtml import crearRentalsHtml
from src.capaPresentacion.crearHtml.crearMarcasHtml import crearMarcasHtml
from src.capaPresentacion.crearHtml.crearIndexHtml import crearIndexHtml


respuesta = respuestaText(respuestaMongo()) 
listaBicis = listarBicis(respuesta)
listaRentals = listarRentals(respuesta)


def crearTodo():

    crearIndexHtml()
    crearRentalsHtml()
    crearMarcasHtml()
    crearBiciSolitariaHtml(listaBicis)
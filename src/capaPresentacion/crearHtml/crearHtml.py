from src.capaDatos.listarDatosMongo import listarBicis, listarRentals, respuestaText
from src.capaDatos.peticionMongo import respuestaMongo
from src.capaPresentacion.crearHtml.crearBiciSolitariaHtml import crearBiciSolitariaHtml
from src.capaPresentacion.crearHtml.crearRentalsHtml import crearRentalsHtml
from src.capaPresentacion.crearHtml.crearMarcasHtml import crearMarcasHtml
from src.capaPresentacion.crearHtml.crearIndexHtml import crearIndexHtml
from src.capaPresentacion.crearHtml.crearBiciCaract import crearBicisCaractHtml
from src.capaPresentacion.crearHtml.crearBiciCateg import crearBiciCategoriaHtml
from src.capaPresentacion.crearHtml.crearBiciMarca import crearBiciMarcaHtml
from src.capaPresentacion.crearHtml.crearBicisHtml import crearBicisHtml


respuesta = respuestaText(respuestaMongo()) 
listaBicis = listarBicis(respuesta)
listaRentals = listarRentals(respuesta)


def crearHtml():

    crearIndexHtml()
    crearRentalsHtml()
    crearMarcasHtml()
    crearBiciSolitariaHtml(listaBicis)
    crearBicisCaractHtml()
    crearBiciCategoriaHtml()
    crearBicisHtml()
    crearBiciMarcaHtml()
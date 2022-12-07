from src.capaDatos.listarDatosMongo import listarBicis, listarRentals, respuestaText
from src.capaDatos.peticionMongo import respuestaMongo
from src.capaNegocio.comandosGit import guardarCambios, actualizarGitHubPagina
from src.capaNegocio.crearDirectorios import crearRutasDocs
from src.capaPresentacion.crearHtml.crearBicisHtml import crearBicisHtml
from src.capaPresentacion.crearHtml.crearBiciSolitariaHtml import crearBiciSolitariaHtml
from src.capaPresentacion.crearHtml.crearIndexHtml import crearIndexHtml
from src.capaPresentacion.crearHtml.crearRentalsHtml import crearRentalsHtml
from src.capaPresentacion.crearHtml.crearTiposHtml import crearTiposHtml
from src.capaPresentacion.crearHtml.crearMarcasHtml import crearMarcasHtml
from src.capaPresentacion.crearHtml.crearBiciCaractHtml import crearBiciCaracteristicaHtml
from src.capaPresentacion.crearHtml.crearBiciCategHtml import crearBiciCategoriaHtml
from src.capaPresentacion.crearHtml.crearBiciMarcaHtml import crearBiciMarcaHtml


# Nombrar variables necesarias
datosMongo = respuestaText(respuestaMongo())
listaBicis = listarBicis(datosMongo)
listaRentals = listarRentals(datosMongo)

# Funcion principal
def generarPáginasEstáticas(listaBicis,listaRentals):

    crearRutasDocs()
    crearIndexHtml()
    crearMarcasHtml()
    crearTiposHtml()
    crearBicisHtml(listaBicis)
    crearBiciCaracteristicaHtml(listaBicis)
    crearBiciCategoriaHtml(listaBicis)
    crearBiciMarcaHtml(listaBicis)
    crearRentalsHtml(listaRentals)
    crearBiciSolitariaHtml(listaBicis)
    # guardarCambios()
    # actualizarGitHubPagina()

generarPáginasEstáticas(listaBicis,listaRentals)


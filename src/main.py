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
    crearBiciSolitariaHtml(listaBicis)
    crearRentalsHtml(listaRentals)

generarPáginasEstáticas(listaBicis,listaRentals)


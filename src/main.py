from src.capaDatos.listarDatosMongo import listarBicis, listarRentals, respuestaText
from src.capaDatos.peticionMongo import respuestaMongo
from src.capaNegocio.comandosGit import guardarCambios, actualizarGitHubPagina
from src.capaNegocio.crearDirectorios import crearRutasDocs
from src.capaPresentacion.crearHtml.crearBicisHtml import crearBicisHtml
from src.capaPresentacion.crearHtml.crearBiciSolitariaHtml import crearBiciSolitariaHtml
from src.capaPresentacion.crearHtml.crearIndexHtml import crearIndexHtml
from src.capaPresentacion.crearHtml.crearRentalsHtml import crearRentalsHtml
from src.capaPresentacion.crearHtml.crearMarcasHtml import crearMarcasHtml
from src.capaPresentacion.crearHtml.crearBiciCaractHtml import crearBiciCaracteristicaHtml
from src.capaPresentacion.crearHtml.crearBiciCategHtml import crearBiciCategoriaHtml
from src.capaPresentacion.crearHtml.crearBiciMarcaHtml import crearBiciMarcaHtml
from src.capaPresentacion.crearCss.funcionCssBase import crearCssBase
from src.capaPresentacion.crearCss.crearRentalsCss import crearRentalsCss
from src.capaPresentacion.crearCss.crearMarcasCss import crearMarcasCss
from src.capaPresentacion.crearCss.crearIndexCss import crearIndexCss
from src.capaPresentacion.crearCss.crearBiciSolitariaCss import crearBiciSolitariaCss
from src.capaPresentacion.crearCss.crearBicisFiltroCss import crearBicisFiltroCss
from src.capaPresentacion.crearCss.crearBicisCss import crearBicisCss
from src.CRUD.crud import CRUD
from src.check.checkDatos import checkGeneralDatos
from src.check.checkNegocio import checkDirectorios


# Nombrar variables necesarias
datosMongo = respuestaText(respuestaMongo())
listaBicis = listarBicis(datosMongo)
listaRentals = listarRentals(datosMongo)


# Funcion principal
def generarPáginasEstáticas(listaBicis,listaRentals):

    if checkGeneralDatos(respuestaMongo(),listaBicis,listaRentals) == False:
        raise Exception("Los datos no son correctos, revisa el programa y vuelve a ejecutarlo para evitar problemas")
    CRUD()
    crearRutasDocs()
    if checkDirectorios() == False:
        raise Exception("Los directorios no existe, por favor, revisa los datos y vuelve a ejecutar el programa para evitar problemas.")
    crearCssBase()
    crearIndexHtml()
    crearIndexCss()
    crearMarcasHtml()
    crearMarcasCss()
    crearBicisHtml(listaBicis)
    crearBicisCss()
    crearBiciCaracteristicaHtml(listaBicis)
    crearBiciCategoriaHtml(listaBicis)
    crearBiciMarcaHtml(listaBicis)
    crearBicisFiltroCss()
    crearRentalsHtml(listaRentals)
    crearRentalsCss()
    crearBiciSolitariaHtml(listaBicis)
    crearBiciSolitariaCss()
    guardarCambios()
    actualizarGitHubPagina()

generarPáginasEstáticas(listaBicis,listaRentals)


from src.capaPresentacion.crearTodo import crearTodo
from src.capaNegocio.crearDirectorios import crearRutasDocs
from src.capaNegocio.comandosGit import actualizarPages
from src.check.checkDatos import checkGeneralDatos
from src.capaDatos.peticionMongo import respuestaMongo
from src.check.checkNegocio import checkDirectorios
from src.capaDatos.listarDatosMongo import listarBicis, listarRentals, respuestaText
from src.capaDatos.peticionMongo import respuestaMongo
respuesta = respuestaText(respuestaMongo()) 
listaBicis = listarBicis(respuesta)
listaRentals = listarRentals(respuesta)


# Este modulo se va a encargar de crear y ejecutar todas las funciones para que se 
# visualicen los cambios en la base de datos de MongoDB en la pagina web estática
# servida por gitHub Pages en link : 'https://clearcb.github.io/RentatorBike/'

def generarGitHubPages():

    if checkGeneralDatos(respuestaMongo(),listaBicis,listaRentals) == False:
        raise Exception("Los datos no son correctos, revisa el programa y vuelve a ejecutarlo para evitar problemas")
    crearRutasDocs()
    if checkDirectorios() == False:
        raise Exception("Los directorios no existe, por favor, revisa los datos y vuelve a ejecutar el programa para evitar problemas.")
    crearRutasDocs()
    crearTodo()
    actualizarPages()

if __name__ == '__main__':

    generarGitHubPages()
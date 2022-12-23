import os
# En este modulo vamos a comprobar y poner una barricada de la capa Negocio.

def checkUnDirectorio(ruta):

    try:

        if not(os.path.exists(ruta) and os.path.isdir(ruta)):
            raise Exception

    except:
        return False

# Comprueba que existen todos los directorios necesarios para el correcto funcionamiento del programa
def checkDirectorios():

    rutaDocs = os.path.relpath("./docs")
    rutaCss = os.path.relpath("./docs/cssStyles")
    rutaSecondPages = os.path.relpath("./docs/second_pages")
    rutaPaginasSecundarias = os.path.relpath("./docs/second_pages/bicissolitarias")

    checkUnDirectorio(rutaDocs)
    checkUnDirectorio(rutaCss)
    checkUnDirectorio(rutaSecondPages)
    checkUnDirectorio(rutaPaginasSecundarias)

    return True
import os
# En este modulo vamos a comprobar y poner una barricada de la capa Negocio.

# Comprueba que existen todos los directorios necesarios para el correcto funcionamiento del programa
def checkDirectorios():

    rutaDocs = os.path.relpath("./docs")
    rutaCss = os.path.relpath("./docs/cssStyles")
    rutaSecondPages = os.path.relpath("./docs/second_pages")
    rutaPaginasSecundarias = os.path.relpath("./docs/second_pages/bicissolitarias")

    try:

        if not(os.path.exists(rutaDocs) and os.path.isdir(rutaDocs)):
            return False

        if not(os.path.exists(rutaCss) and os.path.isdir(rutaCss)):
            return False

        if not(os.path.exists(rutaSecondPages) and os.path.isdir(rutaSecondPages)):
            return False

        if not(os.path.exists(rutaPaginasSecundarias) and os.path.isdir(rutaPaginasSecundarias)):
            return False

    except FileNotFoundError:
        return False

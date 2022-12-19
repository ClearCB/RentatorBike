import os

# Este modulo se va a encargar de la creación de los directorios que vamos a necesitar para la página

# Definimos una función que toma como parámetros las rutas que queremos de los directorios y los crea
def creacionDirectorios(ruta,nombreDirectorio):

    ruta = os.path.relpath(ruta) # Nombramos la ruta relativa para que se creen las carpetas en el directorio actual

    try: # Comprobamos que se pueden crear correctamente y en el caso de que ya existan, no ocurrirá nada
        os.makedirs(ruta, exist_ok=True)
        print(f"El directorio {nombreDirectorio} ha sido creado correctamente")
    except OSError: # En el caso de que no se pueda crear, el programa lanzará una excepción
        print(f"El directorio {nombreDirectorio} no ha podido crearse")
        return False

# Definimos una función que nos crea los directorios que necesitamos para desplegar la página estática
def crearRutasDocs():

    #Asignamos la rutas de los directorios
    pathBiciSolitarias = ".\\docs\\second_pages\\bicissolitarias"
    pathPaginaSecundaria = ".\\docs\\second_pages"
    pathCcsStyles = ".\\docs\\cssStyles"

    # Creamos los directorios
    creacionDirectorios(pathBiciSolitarias, "bicissolitarias")
    creacionDirectorios(pathPaginaSecundaria, "second_pages")
    creacionDirectorios(pathCcsStyles, "cssStyles")
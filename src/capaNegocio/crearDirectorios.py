# Este modulo se va a encargar de la creación de los directorios que vamos a necesitar para la página 

# Importamos la libreria os con la cual podremos crear los directorios.

import os


# Esta funcion se encarga de la creacion de los directorios, contiene un bloque de try-except para comprobar
# que estos se crearon correctamente y en el caso de que ya existan, continua con el programa.
def creacionDirectorios():

    videos = "C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\videos"
    biciSolitarias = "C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\bicissolitarias"
    ccsStyles = "C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\cssStyles"

    # Primero comprobamos que existan los directorios, en caso contrario los creamos.

    if os.path.exists(videos):
        pass
    else:
        try:
            os.makedirs(videos, exist_ok=True)
            print(f"El directorio 'videos' ha sido creado correctamente")
        except OSError:
            print(f"El directorio 'videos' no ha podido crearse")


    if os.path.exists(biciSolitarias):
        pass
    else:
        try:
            os.makedirs(biciSolitarias, exist_ok=True)
            print(f"El directorio 'biciSolitarias' ha sido creado correctamente")
        except OSError:
            print(f"El directorio 'biciSolitarias' no ha podido crearse")

    if os.path.exists(ccsStyles):
        pass
    else:
        try:
            os.makedirs(ccsStyles, exist_ok=True)
            print(f"El directorio 'ccsStyles' ha sido creado correctamente")
        except OSError:
            print(f"El directorio 'ccsStyles' no ha podido crearse")
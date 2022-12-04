import os

# Este modulo se va a encargar de la creación de los directorios que vamos a necesitar para la página 

# Importamos la libreria os con la cual podremos crear los directorios.



# Esta funcion se encarga de la creacion de los directorios, contiene un bloque de try-except para comprobar
# que estos se crearon correctamente y en el caso de que ya existan, continua con el programa.
# Le asignamos como parametros el path de donde queremos ubicar los directorios creados.

def creacionDirectorios(pathVideos,pathBiciSolitarias,pathCcsStyles):

    # Primero comprobamos que existan los directorios, en caso contrario los creamos.

    if os.path.exists(pathVideos) and os.path.isdir(pathVideos):
        pass
    else:
        try:
            os.makedirs(pathVideos, exist_ok=True)
            print(f"El directorio 'videos' ha sido creado correctamente")
        except OSError:
            print(f"El directorio 'videos' no ha podido crearse")


    if os.path.exists(pathBiciSolitarias) and os.path.isdir(pathBiciSolitarias):
        pass
    else:
        try:
            os.makedirs(pathBiciSolitarias, exist_ok=True)
            print(f"Los directorios 'second_pages' y 'bicisolitarias' han sido creados correctamente")
        except OSError:
            print(f"El directorio 'biciSolitarias' no ha podido crearse")


    if os.path.exists(pathCcsStyles) and os.path.isdir(pathCcsStyles):
        pass
    else:
        try:
            os.makedirs(pathCcsStyles, exist_ok=True)
            print(f"El directorio 'ccsStyles' ha sido creado correctamente")
        except OSError:
            print(f"El directorio 'ccsStyles' no ha podido crearse")


pathVideos = "C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\videos"
pathBiciSolitarias = "C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\second_pages\\bicissolitarias"
pathCcsStyles = "C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\cssStyles"


creacionDirectorios(pathVideos,pathBiciSolitarias,pathCcsStyles)
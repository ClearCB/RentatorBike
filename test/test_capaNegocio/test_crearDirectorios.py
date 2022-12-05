from src.capaNegocio.crearDirectorios import creacionDirectorios
import pytest
import os

# Este test va a comprobar que el modulo la funcion creacionDirectorios del modulo crearDirectorios funciona correctamente 
# y lanza las excepciones.

# Nombramos las rutas de los directorios
pathVideos = ".\\dirTest\\videos"
pathBiciSolitarias = ".\\dirTest\\second_pages\\bicissolitarias"
pathPaginaSecundaria = ".\\dirTest\\second_pages"
pathCcsStyles = ".\\dirTest\\cssStyles"

# Comprobamos que se crean correctamente
@pytest.mark.test_creacionDirectorios
def test_creacionDirectoriosVideos():

    creacionDirectorios(pathVideos, "videos") # Creamos el directorio
    assert os.path.exists(pathVideos) != False # La ruta existe
    assert os.path.isdir(pathVideos) == True # En la ruta existe un directorio

# Comprobamos que si no puede crearse un directorio, lanza error y termina la ejecución
@pytest.mark.test_errorCreacionDirectorios
def test_errorCreacionDirectorios():


    with open("C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\dirTest\\second_pages", "w") as file: # Abrimos un archivo para generar un error
        file.write("Este texto es de prueba")
        print("El archivo second_pages creado correctamente")

    assert creacionDirectorios(pathPaginaSecundaria, "second_pages")  == False # Nos devuelve False si no puede crear el directorio
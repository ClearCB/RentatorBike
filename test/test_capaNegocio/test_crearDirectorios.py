from src.capaNegocio.crearDirectorios import creacionDirectorios, crearRutasDocs
import pytest
import os
import shutil

# Este test va a comprobar que el modulo la funcion creacionDirectorios del modulo crearDirectorios funciona correctamente 
# y lanza las excepciones.

# Nombramos las rutas de los directorios
pathBiciSolitarias = os.path.relpath(".\\docs\\second_pages\\bicissolitarias")
pathPaginaSecundaria = os.path.relpath(".\\docs\\second_pages")
pathCcsStyles = os.path.relpath(".\\docs\\cssStyles")

# Comprobamos que se crean correctamente
@pytest.mark.test_creacionDirectorios
def test_creacionDirectoriosVideos():

    creacionDirectorios(pathCcsStyles, "cssStyles") # Creamos el directorio
    assert os.path.exists(pathCcsStyles) == True # La ruta existe
    assert os.path.isdir(pathCcsStyles) == True # En la ruta existe un directorio
    shutil.rmtree(pathCcsStyles)

# Comprobamos que si no puede crearse un directorio, lanza error y termina la ejecución
@pytest.mark.test_errorCreacionDirectorios
def test_errorCreacionDirectorios():

    ruta = os.path.relpath("./docs/second_pages")
    with open(ruta, "w") as file: # Abrimos un archivo para generar un error
        file.write("Este texto es de prueba")
        print("El archivo second_pages creado correctamente")

    assert creacionDirectorios(pathPaginaSecundaria, "second_pages")  == False # Nos devuelve False si no puede crear el directorio
    os.remove(ruta)

# Este test comprueba que la funcion que crea los directorios donde toca se ejecuta correctamente
@pytest.mark.test_crearDRutasDocs
def test_crearRutasDocs():

    crearRutasDocs()
    pathBiciSolitarias = os.path.relpath(".\\docs\\second_pages\\bicissolitarias")
    pathPaginaSecundaria = os.path.relpath(".\\docs\\second_pages")
    pathCcsStyles = os.path.relpath(".\\docs\\cssStyles")
    assert os.path.exists(pathCcsStyles) == True
    assert os.path.exists(pathBiciSolitarias) == True
    assert os.path.exists(pathPaginaSecundaria) == True
    shutil.rmtree(pathBiciSolitarias)
    shutil.rmtree(pathPaginaSecundaria)
    shutil.rmtree(pathCcsStyles)
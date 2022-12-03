# Este test va a comprobar que el modulo la funcion creacionDirectorios del modulo crearDirectorios funciona correctamente
from src.capaNegocio.crearDirectorios import creacionDirectorios
import pytest
import os

# Nombramos las rutas de los directorios

pathVideos = "C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\videos"
pathBiciSolitarias = "C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\bicissolitarias"
pathCcsStyles = "C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\cssStyles"

# En primer lugar, ejecutamos la funcion para que cree los directorios y después comprobamos que existen.

@pytest.mark.test_creacionDirectoriosVideos
def test_creacionDirectoriosVideos():

    creacionDirectorios(pathVideos,pathBiciSolitarias,pathCcsStyles)
    assert os.path.exists(pathVideos) != False

@pytest.mark.test_creacionDirectoriosBicisSolitarias
def test_creacionDirectoriosBicisSolitarias():

    creacionDirectorios(pathVideos,pathBiciSolitarias,pathCcsStyles)
    assert os.path.exists(pathBiciSolitarias) != False

@pytest.mark.test_creacionDirectoriosCssStyles
def test_creacionDirectoriosCssStyles():

    creacionDirectorios(pathVideos,pathBiciSolitarias,pathCcsStyles)
    assert os.path.exists(pathCcsStyles) != False


# Ahora comprobaremos que en el caso de que existan, el programa no hace nada

@pytest.mark.test_creacionDirectoriosExisten
def test_creacionDirectoriosVideosExiste():

    assert creacionDirectorios(pathVideos,pathBiciSolitarias,pathCcsStyles) == None

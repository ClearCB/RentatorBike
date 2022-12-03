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

    creacionDirectorios()
    assert os.path.exists(pathVideos) != False

@pytest.mark.test_creacionDirectoriosBicisSolitarias
def test_creacionDirectoriosBicisSolitarias():

    creacionDirectorios()
    assert os.path.exists(pathBiciSolitarias) != False

@pytest.mark.test_creacionDirectoriosCssStyles
def test_creacionDirectoriosCssStyles():

    creacionDirectorios()
    assert os.path.exists(pathCcsStyles) != False
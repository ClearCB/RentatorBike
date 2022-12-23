from src.check.checkNegocio import checkUnDirectorio, checkDirectorios
from src.capaNegocio.crearArchivos import crearArchivo
from src.capaNegocio.crearDirectorios import crearRutasDocs, creacionDirectorios
import pytest
import os
import shutil

# Comprobamos que si no existe el directorio se capta bien la excepcion
@pytest.mark.test_checkUnDirectorio
def test_checkUnDirectorio():

    assert checkUnDirectorio(os.path.relpath("ququ")) == False

# Comprobamos que si existe pero no es un directorio, devuelve False correctamente
@pytest.mark.test_checkNoEsDirectorio
def test_checkNoEsDirectorio():

    assert checkUnDirectorio(os.path.relpath("./src/main.py")) == False

# Comprobamos que si todo funciona correctamente, comprueba que se checkean los directorios correctamente
@pytest.mark.test_checkDirectorios
def test_checkDirectorios():

    crearRutasDocs()
    assert checkDirectorios() == True
    shutil.rmtree(os.path.relpath("./docs"))
    creacionDirectorios(os.path.relpath("./docs"), "docs")
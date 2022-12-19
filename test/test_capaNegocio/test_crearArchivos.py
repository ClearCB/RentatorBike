from src.capaNegocio.crearArchivos import crearArchivo
import pytest 
import os

# Comprobamos que se crea correctamente el archivo
@pytest.mark.test_crearArchivo
def test_crearArchivo():

    crearArchivo("hola", ".\\", "archivo", "txt")
    ruta = os.path.relpath(".\\archivo.txt")
    assert os.path.isfile(ruta) == True
    os.remove(ruta)

# Comprobamos que en caso de que no pueda crear el archivo, lanza error
@pytest.mark.test_noExisteDirectorio
def test_noExisteDirectorio():

    assert crearArchivo("hola", ".\\docs/jhaja", "archivo", "txt") == False
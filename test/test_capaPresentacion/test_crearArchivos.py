from src.capaNegocio.crearArchivos import crearArchivo
import pytest 
import os

@pytest.mark.test_crearArchivo
def test_crearArchivo():

    crearArchivo("hola", "..\\", "archivo", "txt")
    ruta = os.path.relpath("..\\archivo.txt")
    assert os.path.isfile(ruta) == True


@pytest.mark.test_noExisteDirectorio
def test_noExisteDirectorio():


    crearArchivo("hola", "..\\docs", "archivo", "txt")
    ruta = os.path.relpath(".\\docs\\prueba.txt")
    assert os.path.isfile(ruta) == False
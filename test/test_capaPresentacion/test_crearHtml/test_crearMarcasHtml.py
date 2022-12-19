from src.capaPresentacion.crearHtml.crearMarcasHtml import crearMarcasHtml
from src.capaNegocio.crearDirectorios import creacionDirectorios
import pytest
import os
import shutil

# Estos test se encargan de comprobar que el body se crea correctamente y de comprobar que el archivo marcas.html existe

# Comprueba que el archivo marcas.html se crea correctamente
@pytest.mark.test_crearMarcasHtml
def test_crearMarcasHtml():

    creacionDirectorios(os.path.relpath(".\\docs\\second_pages"), "second_pages")
    crearMarcasHtml()
    ruta = os.path.relpath(".\\docs\\second_pages\\marcas.html")
    assert os.path.isfile(ruta) == True
    shutil.rmtree(os.path.relpath(".\\docs\\second_pages"))
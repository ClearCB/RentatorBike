from src.capaPresentacion.crearHtml.crearBicisHtml import crearBicisHtml
from src.capaNegocio.crearDirectorios import creacionDirectorios
import pytest
import os
import shutil

# Estos test se encargan de comprobar que el archivo index.html existe

# Comprueba que el archivo index.html se crea correctamente
@pytest.mark.test_crearIndexHtml
def test_crearIndexHtml():

    creacionDirectorios(os.path.relpath(".\\docs\\second_pages"), "second_pages")
    crearBicisHtml()
    ruta = os.path.relpath(".\\docs\\second_pages/bicis.html")
    assert os.path.isfile(ruta) == True
    shutil.rmtree(os.path.relpath(".\\docs\\second_pages"))
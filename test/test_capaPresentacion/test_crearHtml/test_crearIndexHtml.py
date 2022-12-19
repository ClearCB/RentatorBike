from src.capaPresentacion.crearHtml.crearIndexHtml import crearIndexHtml
from src.capaNegocio.crearDirectorios import creacionDirectorios
import pytest
import os
import shutil

# Estos test se encargan de comprobar que el archivo index.html existe

# Comprueba que el archivo index.html se crea correctamente
@pytest.mark.test_crearIndexHtml
def test_crearIndexHtml():

    crearIndexHtml()
    ruta = os.path.relpath(".\\docs\\index.html")
    assert os.path.isfile(ruta) == True
    os.remove(ruta)

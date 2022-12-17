from src.capaPresentacion.crearHtml.crearIndexHtml import crearIndexHtml
import pytest
import os

# Estos test se encargan de comprobar que el body se crea correctamente y de comprobar que el archivo index.html existe

# Comprueba que el archivo index.html se crea correctamente
@pytest.mark.test_crearIndexHtml
def test_crearIndexHtml():

    crearIndexHtml()
    ruta = os.path.relpath(".\\docs\\index.html")
    assert os.path.isfile(ruta) == True

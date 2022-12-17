from src.capaPresentacion.crearHtml.crearBicisHtml import crearBicisHtml
import pytest
import os

# Estos test se encargan de comprobar que el archivo index.html existe

# Comprueba que el archivo index.html se crea correctamente
@pytest.mark.test_crearIndexHtml
def test_crearIndexHtml():

    crearBicisHtml()
    ruta = os.path.relpath(".\\docs\\second_pages/bicis.html")
    assert os.path.isfile(ruta) == True
    os.remove(ruta)
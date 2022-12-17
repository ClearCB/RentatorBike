from src.capaPresentacion.crearHtml.crearMarcasHtml import crearMarcasHtml
import pytest
import os

# Estos test se encargan de comprobar que el body se crea correctamente y de comprobar que el archivo marcas.html existe

# Comprueba que el archivo marcas.html se crea correctamente
@pytest.mark.test_crearMarcasHtml
def test_crearMarcasHtml():

    crearMarcasHtml()
    ruta = os.path.relpath(".\\docs\\second_pages\\marcas.html")
    assert os.path.isfile(ruta) == True
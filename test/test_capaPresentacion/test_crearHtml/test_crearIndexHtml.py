from src.capaPresentacion.crearHtml.crearIndexHtml import crearIndexHtml,indexHtml
from src.capaPresentacion.variables.variablesHtmlTest import indexHtmlTest
import pytest
import os

# Estos test se encargan de comprobar que el body se crea correctamente y de comprobar que el archivo index.html existe

# Este test comprueba que se crea correctamente el html del index
@pytest.mark.test_indexHtml
def test_indexHtml():

    assert indexHtml() == indexHtmlTest


# Comprueba que el archivo index.html se crea correctamente
@pytest.mark.test_crearIndexHtml
def test_crearIndexHtml():

    crearIndexHtml()
    ruta = os.path.relpath(".\\docs\\index.html")
    assert os.path.isfile(ruta) == True

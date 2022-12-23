from src.capaPresentacion.crearCss.funcionCssBase import footerStylesCss, headerStylesCss, navStylesCss, baseStylesCss, crearCssBase
from src.capaNegocio.crearDirectorios import creacionDirectorios
from src.variables.variablesCss import footerCss, headerCss, baseCss, navCss
import pytest
import os
import shutil

# Este test comprueba que las funciones que devuelven una variable con el código css de las partes header, base, nav y footer.

# Este test comprueba que se devuelve correctamente el código de la parte footercss
@pytest.mark.test_crearFooterCss
def test_crearFooterCss():

    assert footerStylesCss() == footerCss

# Este test comprueba que se devuelve correctamente el código de la parte headercss
@pytest.mark.test_crearHeaderCss
def test_crearHeaderCss():

    assert headerStylesCss() == headerCss

# Este test comprueba que se devuelve correctamente el código de la parte navcss
@pytest.mark.test_crearNavCss
def test_crearNavCss():

    assert navStylesCss() == navCss

# Este test comprueba que se devuelve correctamente el código de la parte basecss
@pytest.mark.test_crearBaseCss
def test_crearBaseCss():

    assert baseStylesCss() == baseCss

# Este test comprueba que se crea correctamente los archivos
@pytest.mark.test_crearCssBase
def test_crearCssBase():

    creacionDirectorios(os.path.relpath(".\\docs\\cssStyles"), "cssStyles")
    crearCssBase()
    ruta = os.path.relpath(".\\docs\\cssStyles\\base.css")
    assert os.path.isfile(ruta) == True
    ruta = os.path.relpath(".\\docs\\cssStyles\\nav.css")
    assert os.path.isfile(ruta) == True
    ruta = os.path.relpath(".\\docs\\cssStyles\\header.css")
    assert os.path.isfile(ruta) == True
    ruta = os.path.relpath(".\\docs\\cssStyles\\footer.css")
    assert os.path.isfile(ruta) == True

    shutil.rmtree(os.path.relpath(".\\docs\\cssStyles"))
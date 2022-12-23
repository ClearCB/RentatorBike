from src.capaPresentacion.crearCss.crearBicisCss import bicisStylesCss, crearBicisCss
from src.capaPresentacion.crearCss.crearBicisFiltroCss import bicisfiltroStylesCss, crearBicisFiltroCss
from src.capaPresentacion.crearCss.crearBiciSolitariaCss import biciSolitariaStylesCss, crearBiciSolitariaCss
from src.capaPresentacion.crearCss.crearIndexCss import indexStylesCss, crearIndexCss
from src.capaPresentacion.crearCss.crearMarcasCss import marcasStylesCss, crearMarcasCss
from src.capaPresentacion.crearCss.crearRentalsCss import rentalsStylesCss, crearRentalsCss
from src.variables.variablesCss import bicisCss, bicisFiltroCss, biciSolitariaCss, indexCss, marcasCss, rentalsCss
from src.capaNegocio.crearDirectorios import creacionDirectorios
import pytest
import pytest
import os
import shutil

# Este test comprobará que las funcionalidades que crean el css de las paginas en solitario lo hacen correctamente

# Este test comprueba que se crea correctamente el codigo css de la pagina bicis.html
@pytest.mark.test_crearBicisCss
def test_crearBicisCss():

    assert bicisStylesCss() == bicisCss

# Este test comprueba que se crea correctamente el codigo css de la pagina por filtro css
@pytest.mark.test_crearBiciFiltroCss
def test_crearBiciFiltroCss():

    assert bicisfiltroStylesCss() == bicisFiltroCss

# Este test comprueba que se crea correctamente el codigo css de la pagina bicisolitaria.html
@pytest.mark.test_crearBiciSolitariaCss
def test_crearBiciSolitariaCss():

    assert biciSolitariaStylesCss() == biciSolitariaCss

# Este test comprueba que se crea correctamente el codigo css de la pagina bicisolitaria.html
@pytest.mark.test_crearIndexCss
def test_crearIndexCss():

    assert indexStylesCss() == indexCss

# Este test comprueba que se crea correctamente el codigo css de la pagina marcas.html
@pytest.mark.test_crearMarcasCss
def test_crearMarcasCss():

    assert marcasStylesCss() == marcasCss

# Este test comprueba que se crea correctamente el codigo css de la pagina rentals.html
@pytest.mark.test_crearRentalsCss
def test_crearRentalsCss():

    assert rentalsStylesCss() == rentalsCss

# Este test comprueba que se crea correctamente los archivos
@pytest.mark.test_crearCssPorPagina
def test_crearCssPorPagina():

    creacionDirectorios(os.path.relpath(".\\docs\\cssStyles"), "cssStyles")

    crearBicisCss()
    crearBiciSolitariaCss()
    crearBicisFiltroCss()
    crearIndexCss()
    crearMarcasCss()
    crearRentalsCss()

    ruta = os.path.relpath(".\\docs\\cssStyles\\bicis.css")
    assert os.path.isfile(ruta) == True
    ruta = os.path.relpath(".\\docs\\cssStyles\\bicisolitaria.css")
    assert os.path.isfile(ruta) == True
    ruta = os.path.relpath(".\\docs\\cssStyles\\bicisfiltro.css")
    assert os.path.isfile(ruta) == True
    ruta = os.path.relpath(".\\docs\\cssStyles\\index.css")
    assert os.path.isfile(ruta) == True
    ruta = os.path.relpath(".\\docs\\cssStyles\\marcas.css")
    assert os.path.isfile(ruta) == True
    ruta = os.path.relpath(".\\docs\\cssStyles\\rentals.css")
    assert os.path.isfile(ruta) == True

    shutil.rmtree(os.path.relpath(".\\docs\\cssStyles"))
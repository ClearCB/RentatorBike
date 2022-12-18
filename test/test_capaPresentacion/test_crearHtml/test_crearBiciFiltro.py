from src.capaPresentacion.crearHtml.crearBiciCaract import crearBicisCaractHtml
from src.capaPresentacion.crearHtml.crearBiciCateg import crearBiciCategoriaHtml
from src.capaPresentacion.crearHtml.crearBiciMarca import crearBiciMarcaHtml
import pytest
import os

# Estos test se encargan de comprobar que los archivos de bici por filtro se crean correctamente

# Comprueba que el archivo biciscaracteristica.html se crea correctamente
@pytest.mark.test_crearBicisCaractHtml
def test_crearBicisCaractHtml():

    crearBicisCaractHtml()
    ruta = os.path.relpath(".\\docs\\second_pages/biciscaracteristica.html")
    assert os.path.isfile(ruta) == True
    os.remove(ruta)

# Comprueba que el archivo bicispormarca.html se crea correctamente
@pytest.mark.test_crearBiciMarcaHtml
def test_crearBiciMarcaHtml():

    crearBiciMarcaHtml()
    ruta = os.path.relpath(".\\docs\\second_pages/bicispormarca.html")
    assert os.path.isfile(ruta) == True
    os.remove(ruta)

# Comprueba que el archivo biciscategoria.html se crea correctamente
@pytest.mark.test_crearBiciCategoriaHtml
def test_crearBiciCategoriaHtml():

    crearBiciCategoriaHtml()
    ruta = os.path.relpath(".\\docs\\second_pages/biciscategoria.html")
    assert os.path.isfile(ruta) == True
    os.remove(ruta)
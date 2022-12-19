from src.capaPresentacion.crearHtml.crearBiciCaract import crearBicisCaractHtml
from src.capaPresentacion.crearHtml.crearBiciCateg import crearBiciCategoriaHtml
from src.capaPresentacion.crearHtml.crearBiciMarca import crearBiciMarcaHtml
from src.capaNegocio.crearDirectorios import creacionDirectorios
import pytest
import os
import shutil

# Estos test se encargan de comprobar que los archivos de bici por filtro se crean correctamente

# Comprueba que el archivo biciscaracteristica.html se crea correctamente
@pytest.mark.test_crearBicisCaractHtml
def test_crearBicisCaractHtml():

    creacionDirectorios(os.path.relpath(".\\docs\\second_pages"), "second_pages")
    crearBicisCaractHtml()
    ruta = os.path.relpath(".\\docs\\second_pages/biciscaracteristica.html")
    assert os.path.isfile(ruta) == True
    shutil.rmtree(os.path.relpath(".\\docs\\second_pages"))


# Comprueba que el archivo bicispormarca.html se crea correctamente
@pytest.mark.test_crearBiciMarcaHtml
def test_crearBiciMarcaHtml():

    creacionDirectorios(os.path.relpath(".\\docs\\second_pages"), "second_pages")
    crearBiciMarcaHtml()
    ruta = os.path.relpath(".\\docs\\second_pages/bicispormarca.html")
    assert os.path.isfile(ruta) == True
    shutil.rmtree(os.path.relpath(".\\docs\\second_pages"))
    
# Comprueba que el archivo biciscategoria.html se crea correctamente
@pytest.mark.test_crearBiciCategoriaHtml
def test_crearBiciCategoriaHtml():

    creacionDirectorios(os.path.relpath(".\\docs\\second_pages"), "second_pages")
    crearBiciCategoriaHtml()
    ruta = os.path.relpath(".\\docs\\second_pages/biciscategoria.html")
    assert os.path.isfile(ruta) == True
    shutil.rmtree(os.path.relpath(".\\docs\\second_pages"))
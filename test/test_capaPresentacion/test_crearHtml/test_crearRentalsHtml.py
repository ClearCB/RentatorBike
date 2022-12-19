from src.capaPresentacion.crearHtml.crearRentalsHtml import crearRentalsHtml
from src.capaNegocio.crearDirectorios import creacionDirectorios
import pytest
import os
import shutil

# Estos test se encargan de comprobar que el archivo index.html existe

# Comprueba que el archivo index.html se crea correctamente
@pytest.mark.test_crearRentalHtml
def test_crearRentalHtml():

    creacionDirectorios(os.path.relpath(".\\docs\\second_pages"), "second_pages")
    crearRentalsHtml()
    ruta = os.path.relpath(".\\docs\\second_pages/rentals.html")
    assert os.path.isfile(ruta) == True
    shutil.rmtree(os.path.relpath(".\\docs\\second_pages"))
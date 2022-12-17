from src.capaPresentacion.crearHtml.crearRentalsHtml import crearRentalsHtml
import pytest
import os

# Estos test se encargan de comprobar que el archivo index.html existe

# Comprueba que el archivo index.html se crea correctamente
@pytest.mark.test_crearRentalHtml
def test_crearRentalHtml():

    crearRentalsHtml()
    ruta = os.path.relpath(".\\docs\\second_pages/rentals.html")
    assert os.path.isfile(ruta) == True
    os.remove(ruta)
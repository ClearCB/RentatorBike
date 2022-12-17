from src.capaPresentacion.crearHtml.crearyBodyHtml import crearBodyRentals
from src.variables.variablesHtmlTest import listaRentalsTest, rentalBodyTest
import pytest

# En este modulo vamos a comprobar que la funcion que crea que el body html de rentals

@pytest.mark.test_crearBodyRentals
def test_crearBodyRentals():

    assert crearBodyRentals(listaRentalsTest) == rentalBodyTest
from src.capaPresentacion.crearHtml.crearBodyHtml import crearBodyRentals, crearBodyBicis
from src.variables.variablesHtmlTest import listaRentalsTest, rentalBodyTest, listaBiciTest,  bicisBodyTest
import pytest

# En este modulo vamos a comprobar que la funcion que crea que el body html de rentals

@pytest.mark.test_crearBodyRentals
def test_crearBodyRentals():

    assert crearBodyRentals(listaRentalsTest) == rentalBodyTest

@pytest.mark.test_crearBodyBicis
def test_crearBodyBicis():

    assert crearBodyBicis(listaBiciTest) == bicisBodyTest
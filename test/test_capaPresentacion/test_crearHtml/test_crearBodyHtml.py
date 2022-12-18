from src.capaPresentacion.crearHtml.crearBodyHtml import crearBodyRentals, crearBodyBicis, crearBodyCaracteristica, crearBodyCategoria, crearBodyMarca
from src.variables.variablesHtmlTest import listaRentalsTest, rentalBodyTest, listaBiciTest,  bicisBodyTest, bodyPorMarcaTest, bodyPorCaractTest, bodyPorCategTest,listaFiltroTest
import pytest

# En este modulo vamos a comprobar que la funcion que crea que el body html de rentals

@pytest.mark.test_crearBodyRentals
def test_crearBodyRentals():

    assert crearBodyRentals(listaRentalsTest) == rentalBodyTest

@pytest.mark.test_crearBodyBicis
def test_crearBodyBicis():

    assert crearBodyBicis(listaBiciTest) == bicisBodyTest

@pytest.mark.test_crearBodyCaracteristica
def test_crearBodyCaracteristica():

    assert crearBodyCaracteristica(listaFiltroTest) == bodyPorCaractTest

@pytest.mark.test_crearBodyCategoria
def test_crearBodyCategoria():

    assert crearBodyCategoria(listaFiltroTest) == bodyPorCategTest

@pytest.mark.test_crearBodyMarca
def test_crearBodyMarca():

    assert crearBodyMarca(listaFiltroTest) == bodyPorMarcaTest
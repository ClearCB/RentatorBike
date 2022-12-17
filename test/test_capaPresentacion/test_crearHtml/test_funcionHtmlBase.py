from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHtmlHead, crearHeader, crearContenedorRental
from src.capaPresentacion.variables.variablesHtmlTest import headTest, headTestCambiado, headerTest, headerTestCambiado, listaRentalsTest, contenedorRentalTest
import pytest

# Vamos a realizar los test de las funcionalidades del modulo htmlBase para comprobar
# que se comportan como queremos


# Comprobamos que la función sustituye correctamente los valores que queremos.
@pytest.mark.test_crearHtmlHead
def test_crearHtmlHead():

    # Comprobamos que la función con los parámetros es igual a la variable que buscamos.
    assert crearHtmlHead(headTest, "Rentator", "Página principal de un buscador de bicicletas para alquilar", "Bicicletas, inicio, index, alquilar, rental, bike", "TEST", 'index') == headTestCambiado

# Comprobamos que la función sustituye correctamente los valores que queremos
@pytest.mark.test_crearHeader
def test_crearHeader():

    assert crearHeader(headerTest, "", "TEST") ==  headerTestCambiado

# Comprobamos que la funcion crea correctamente el contenedor deseado
@pytest.mark.test_crearContenedorRental
def test_crearContenedorRental():

    assert crearContenedorRental(listaRentalsTest) == contenedorRentalTest
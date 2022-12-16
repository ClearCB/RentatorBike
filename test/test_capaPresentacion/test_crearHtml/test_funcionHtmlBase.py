from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHtmlHead, crearHeader
from src.capaPresentacion.variables.variablesHtml import head, header
from src.capaPresentacion.variables.variablesHtmlTest import headTest, headerTest
import pytest

# Vamos a realizar los test de las funcionalidades del modulo htmlBase para comprobar
# que se comportan como queremos


# En primer lugar, un test que nos permite comprobar que los parametros asignados se introducen en la variable head para conseguir así una función
# común a todos los archivos .html
@pytest.mark.test_crearHtmlHead
def test_crearHtmlHead():

    # Comprobamos que la función con los parámetros es igual a la variable que buscamos.
    assert crearHtmlHead(head, "Rentator", "Página principal de un buscador de bicicletas para alquilar", "Bicicletas, inicio, index, alquilar, rental, bike", "TEST", 'index') == headTest

# Comprobamos que la función crea un header para el index igual al que le pasamos en la variable
@pytest.mark.test_crearHeader
def test_crearHeader():

    assert crearHeader(header, "", "TEST") ==  headerTest


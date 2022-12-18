from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHtmlHead, crearHeader, crearContenedorRental, crearCodigoHtml, biciSolitariaHtml, crearContenedorBici, esFiltro
from src.variables.variablesHtmlTest import headTest, headTestCambiado, headerTest, headerTestCambiado, rentalsTest, contenedorRentalTest, footerTest, codigoHtmlTest,  htmlBiciSolitaria, biciTest
from src.variables.variablesHtmlTest import htmlBiciSolitariaCambiado, biciTest, contenedorBici, biciFiltrada
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

    assert crearContenedorRental(rentalsTest) == contenedorRentalTest

# Comprobamos que la función crea correctamente el codigo html esperado
@pytest.mark.test_crearCodigoHtml
def test_crearCodigoHtml():

    assert crearCodigoHtml(headTestCambiado, headerTestCambiado, contenedorRentalTest, footerTest) == codigoHtmlTest

# Comprobamos que la funcion biciSolitaria susitituye correctamente los valores deseados en la plantilla de bici solitaria html
@pytest.mark.test_biciSolitariaHtml
def test_biciSolitariaHtml():

    assert biciSolitariaHtml(htmlBiciSolitaria, biciTest) == htmlBiciSolitariaCambiado

# Comprobamos la funcionalidad que crea los contenedores de las bicis
@pytest.mark.test_contenedorBici
def test_contenedorBici():

    assert crearContenedorBici(biciTest) == contenedorBici

# Comprueba que la función ejecuta correctamente el filtro e inserta las bicis correspondientes.
@pytest.mark.test_esFiltro
def test_esFiltro():

    assert esFiltro(biciTest,"marca","cube") == biciFiltrada
    assert esFiltro(biciTest,"caracteristicaRueda","29") == biciFiltrada
    assert esFiltro(biciTest,"caracteristicaMarco","xl") == biciFiltrada
    assert esFiltro(biciTest,"caracteristicaGroup","kask") == biciFiltrada
    assert esFiltro(biciTest,"categoria","bici de ciudad") == biciFiltrada
    assert esFiltro(biciTest,"categoria","hello") == None
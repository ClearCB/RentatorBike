from src.capaPresentacion.crearHtml.funcionHtmlBase import biciSolitariaHtml
from src.capaPresentacion.crearHtml.crearBiciSolitariaHtml import crearBiciSolitariaHtml, todasBiciSolitariasHtml
from src.variables.variablesHtmlTest import listaBiciTest, biciHtmlPA0102, biciHtmlPA0201, htmlBiciSolitaria
import pytest
import os

# Este modulo comprobará que la funcion crearBiciSolitariahtml, creará correctamente 2 html individuales con los parámetros correctos.

# Comprobamos que el mecanismo de la función que crea varios codigo html por bici funciona correctamente.
# Replicamos la funcion crearBiciSolitariaHtml
@pytest.mark.test_crearBiciSolitariaHtml
def test_crearBiciSolitariaHtml():

    for bici in listaBiciTest: # Recorremos la lista de las bicis

        id = bici["_idbike"]
        bicisolitaria = biciSolitariaHtml(htmlBiciSolitaria, bici) # Creamos un html con los datos de la bici en concreto
        if id == "PA0102":
        
            assert bicisolitaria == biciHtmlPA0102

        if id == "PA0201":

            assert bicisolitaria == biciHtmlPA0201

# Este test comprueba que los archivos se crean correctamente si se pasa una lista
@pytest.mark.test_crearBicisSolitarias
def test_crearBicisSolitarias():

    assert crearBiciSolitariaHtml(listaBiciTest) == None
    ruta = os.path.relpath(".\\docs\\second_pages\\bicissolitarias/bicissolitariaPA0102.html")
    assert os.path.isfile(ruta) == True
    ruta = os.path.relpath(".\\docs\\second_pages\\bicissolitarias/bicissolitariaPA0201.html")
    assert os.path.isfile(ruta) == True

@pytest.mark.test_todasBicisSolitarias
def test_todasBicisSolitarias():

    todasBiciSolitariasHtml()
    ruta = os.path.relpath(".\\docs\\second_pages\\bicissolitarias/bicissolitariaPA0201.html")
    assert os.path.isfile(ruta) == True
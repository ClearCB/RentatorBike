# Este test va a comprobar que si la funcion peticionMongo no obtiene la respuesta adecuada
# nos lanza una excepcion y el programa no se ejecuta.
from src.capaDatos.peticionMongo import conseguirRespuestaDatos, mongoKey, mongoUrl
import pytest

@pytest.mark.test_conseguirRespuestaDatos
def test_conseguirRespuestaDatos():

    assert str(conseguirRespuestaDatos(mongoKey(),mongoUrl())) == "<Response [200]>"

@pytest.mark.test_conseguirRespuestaDatosKeyError
def test_conseguirRespuestaDatosKeyError():

    assert conseguirRespuestaDatos("keyerror","https://data.mongodb-api.com/app/data-exlmr/endpoint/data/v1/action/aggregate") == None

@pytest.mark.test_conseguirRespuestaDatosConexionError
def test_conseguirRespuestaDatosConexionError():

    assert conseguirRespuestaDatos("keyerror","https://datacom/app/data-exlmr/endpoint/data/v1/action/aggregate") == None
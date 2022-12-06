from src.capaDatos.peticionMongo import conseguirRespuestaDatos, mongoKey, mongoUrl
import pytest

# Este test va a comprobar que si la funcion peticionMongo obtiene la respuesta adecuada
@pytest.mark.test_conseguirRespuestaDatos
def test_conseguirRespuestaDatos():

    assert str(conseguirRespuestaDatos(mongoKey(),mongoUrl())) == "<Response [200]>"

# Este test va a comprobar que si la funcion peticionMongo no obtiene respuesta, el programa no devuelve nada y no se puede continuar
@pytest.mark.test_conseguirRespuestaDatosKeyError
def test_conseguirRespuestaDatosKeyError():

    assert conseguirRespuestaDatos("keyerror","https://data.mongodb-api.com/app/data-exlmr/endpoint/data/v1/action/aggregate") == None

# Este test va a comprobar que si la funcion peticionMongo no obtiene respuesta, el programa no devuelve nada y no se puede continuar
@pytest.mark.test_conseguirRespuestaDatosConexionError
def test_conseguirRespuestaDatosConexionError():

    assert conseguirRespuestaDatos("keyerror","https://datacom/app/data-exlmr/endpoint/data/v1/action/aggregate") == None
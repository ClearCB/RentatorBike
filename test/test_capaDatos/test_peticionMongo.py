from src.capaDatos.peticionMongo import conseguirRespuestaDatos, mongoEnvVariable ,respuestaMongo
import pytest

# Este test comprueba que si no se encuentra correctamente la variable de entorno, nos da error
@pytest.mark.test_mongoEnvVariable
def test_mongoEnvVariable():

    assert mongoEnvVariable("NAADA") == False

# Este test va a comprobar que si la funcion peticionMongo obtiene la respuesta adecuada
@pytest.mark.test_conseguirRespuestaDatos
def test_conseguirRespuestaDatos():

    assert str(conseguirRespuestaDatos(mongoEnvVariable("KEY"),mongoEnvVariable("URL"))) == "<Response [200]>"

# Este test va a comprobar que si la funcion peticionMongo no obtiene respuesta, el programa no devuelve nada y no se puede continuar
@pytest.mark.test_conseguirRespuestaDatosKeyError
def test_conseguirRespuestaDatosKeyError():

    assert conseguirRespuestaDatos("keyerror","https://data.mongodb-api.com/app/data-exlmr/endpoint/data/v1/action/aggregate") == None

# Este test va a comprobar que si la funcion peticionMongo no obtiene respuesta, el programa no devuelve nada y no se puede continuar
@pytest.mark.test_conseguirRespuestaDatosConexionError
def test_conseguirRespuestaDatosConexionError():

    assert conseguirRespuestaDatos("keyerror","https://datacom/app/data-exlmr/endpoint/data/v1/action/aggregate") == None

# Este test comprueba si se unen correctamente
@pytest.mark.test_respuestaMongo
def test_respuestaMongo():

    assert str(respuestaMongo()) == "<Response [200]>"
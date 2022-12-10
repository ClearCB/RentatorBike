from src.CRUD.actions import actionSintax
import pytest

# Estos test comprobaran que las variables de entorno son llamadas correctamente, y en caso de que no puedan conseguirse, detecta el error.

# Este comprueba que la variable de entorno actions se llama correctamente y puede transformarse.
@pytest.mark.test_actionSintaxSearch
def test_actionSintaxSearch():

    assert actionSintax("find") == "https://data.mongodb-api.com/app/data-exlmr/endpoint/data/v1/action/find"

@pytest.mark.test_actionSintaxCreate
def test_actionSintaxCreate():

    assert actionSintax("insertOne") == "https://data.mongodb-api.com/app/data-exlmr/endpoint/data/v1/action/insertOne"

@pytest.mark.test_actionSintaxUpdate
def test_actionSintaxUpdate():

    assert actionSintax("updateOne") == "https://data.mongodb-api.com/app/data-exlmr/endpoint/data/v1/action/updateOne"

@pytest.mark.test_actionSintaxDelete
def test_actionSintaxDelete():

    assert actionSintax("deleteOne") == "https://data.mongodb-api.com/app/data-exlmr/endpoint/data/v1/action/deleteOne"
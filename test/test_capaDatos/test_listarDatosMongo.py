from src.capaDatos.listarDatosMongo import listarRentals, listarBicis
import pytest

# Este test comprueba que se listan correctamente los datos
@pytest.mark.test_listarRentalsUno
def test_listarRentalsUno():

    doc = {"where":"hehe","documents":[{"where":[{"id_rental":"hehe"}]}]}
    assert listarRentals(doc) == [{"id_rental":"hehe"}]

# Este test comprueba que se listan correctamente los datos
@pytest.mark.test_listarBicisUno
def test_listarBicisUno():

    doc = {"hola":"hjaha", "documents":["2","3"]}
    assert listarBicis(doc) == ["2","3"]

# Este test comprueba que si no se pueden listar correctamente los datos lanza un error
@pytest.mark.test_listarRentalsErrorUno
def test_listarRentalsUno():

    doc = {"where":"hehe","docw":[{"where":[{"id_rental":"hehe"}]}]}
    assert listarRentals(doc) == False

# Este test comprueba que se listan correctamente los datos
@pytest.mark.test_listarBicisErrorUno
def test_listarBicisUno():

    doc = {"hola":"hjaha", "docw":["2","3"]}
    assert listarBicis(doc) == False

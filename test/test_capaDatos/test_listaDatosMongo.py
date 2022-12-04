from src.capaDatos.listarDatosMongo import listarRentals, listarBicis
import pytest

@pytest.mark.test_listarRentalsUno
def test_listarRentalsUno():

    doc = {"where":"hehe","documents":[{"where":[{"id_rental":"hehe"}]}]}
    assert listarRentals(doc) == [{"id_rental":"hehe"}]

@pytest.mark.test_listarBicisUno
def test_listarBicisUno():

    doc = {"hola":"hjaha", "documents":["2","3"]}
    assert listarBicis(doc) == ["2","3"]

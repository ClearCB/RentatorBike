from src.capaPresentacion.crearHtml.crearMarcasHtml import crearBodyMarcas, marcasHtml
import pytest
import os

@pytest.mark.test_crearBodyMarcas
def test_crearBodyMarcas():

    body ='''
        <section>
            <h3 class="titleBike">Marcas de bicicletas</h3>
            <hr>
            <div id="container">
                <a href="bicispormarca.html#cube"><div class="box"> Cube</div></a>
                <a href="bicispormarca.html#specialized"><div class="box"> Specialized</div></a>
                <a href="bicispormarca.html#giant"><div class="box"> Giant</div></a>
                <a href="bicispormarca.html#cannondale"><div class="box"> Cannondale</div></a>
            </div>
        </section>'''

    assert crearBodyMarcas() == body

@pytest.mark.test_crearMarcasHtml()
def test_crearMarcasHtml():

    marcasHtml()
    assert os.path.isfile("C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\second_pages\\marcas.html") == True

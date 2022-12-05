from src.capaPresentacion.crearHtml.crearMarcasHtml import crearBodyMarcas, crearMarcasHtml
import pytest
import os

# Estos test se encargan de comprobar que el body se crea correctamente y de comprobar que el archivo marcas.html existe

# Comprueba que el body se crea correctamente
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

# Comprueba que el archivo marcas.html se crea correctamente
@pytest.mark.test_crearMarcasHtml
def test_crearMarcasHtml():

    crearMarcasHtml()
    ruta = os.path.relpath(".\\docs\\second_pages\\marcas.html")
    assert os.path.isfile(ruta) == True
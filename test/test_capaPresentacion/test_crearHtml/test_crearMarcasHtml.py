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
                <a href="bicispormarca.html#cube"><div class="box"> <img src="http://imgfz.com/i/hex2z4u.png" width="200" height="200" alt="logo cube"></div></a>
                <a href="bicispormarca.html#specialized"><div class="box"><img src="http://imgfz.com/i/uDo52nq.png" width="200" height="200" alt="logo specialized"></div></a>
                <a href="bicispormarca.html#giant"><div class="box"><img src="http://imgfz.com/i/PmJ14L8.png" width="200" height="200" alt="logo giant"></div></a>
                <a href="bicispormarca.html#cannondale"><div class="box"><img src="http://imgfz.com/i/Cp5nJfo.jpeg" width="200" height="200" alt="logo cannondale"></div></a>
            </div>
        </section>'''

    assert crearBodyMarcas() == body

# Comprueba que el archivo marcas.html se crea correctamente
@pytest.mark.test_crearMarcasHtml
def test_crearMarcasHtml():

    crearMarcasHtml()
    ruta = os.path.relpath(".\\docs\\second_pages\\marcas.html")
    assert os.path.isfile(ruta) == True
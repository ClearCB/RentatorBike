from src.capaPresentacion.crearHtml.crearTiposHtml import crearBodyTipos, tiposHtml
import pytest
import os

@pytest.mark.test_crearBodyTipos
def test_crearBodyTipos():

    body ='''
        <h3 class="titleBicis">Tipos de bicicletas</h3><hr>
        <section id="tiposbici">
            <h4>MTB</h4>
            <div class="flex-container">
                <div class="flex-item" >
                        <a href="biciscategoria.html#mtb"><img src="{imagenBici}" alt="una imagen de una bicicleta con la categoria {categoria} de la marca {marca}" ></a>
                </div>
                <div class="flex-item">
                    <p></p>
                </div>
            </div>
            <h4>MTB electrica</h4>
            <div class="flex-container">
                <div class="flex-item" >
                    <a href="biciscategoria.html#emtb"><img src="{imagenBici}" alt="una imagen de una bicicleta con la categoria {categoria} de la marca {marca}" ></a>
                </div>
                <div class="flex-item">
                    <p></p>
                </div>
            </div>
            <h4>Bici de carretera</h4>
            <div class="flex-container">
                <div class="flex-item" >
                    <a href="biciscategoria.html#carretera"><img src="{imagenBici}" alt="una imagen de una bicicleta con la categoria {categoria} de la marca {marca}" ></a>
                </div>
                <div class="flex-item">
                    <p></p>
                </div>
            </div>
            <h4>Bici de carretera electrica</h4>
            <div class="flex-container">
                <div class="flex-item" >
                    <a href="biciscategoria.html#ecarretera"><img src="{imagenBici}" alt="una imagen de una bicicleta con la categoria {categoria} de la marca {marca}" ></a>
                </div>
                <div class="flex-item">
                    <p></p>
                </div>
            </div>
            <h4>Bici de ciudad</h4>
            <div class="flex-container">
                <div class="flex-item" >
                    <a href="biciscategoria.html#ciudad"><img src="{imagenBici}" alt="una imagen de una bicicleta con la categoria {categoria} de la marca {marca}" ></a>
                </div>
                <div class="flex-item">
                    <p></p>
                </div>
            </div>
            <h4>Bici de ciudad electrica</h4>
            <div class="flex-container">
                <div class="flex-item" >
                    <a href="biciscategoria.html#eciudad"><img src="{imagenBici}" alt="una imagen de una bicicleta con la categoria {categoria} de la marca {marca}" ></a>
                </div>
                <div class="flex-item">
                    <p></p>
                </div>
            </div>
        </section>'''

    assert crearBodyTipos() == body

@pytest.mark.test_crearTiposHtml
def test_crearTiposHtml():

    tiposHtml()
    assert os.path.isfile("C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\second_pages\\tipos.html") == True

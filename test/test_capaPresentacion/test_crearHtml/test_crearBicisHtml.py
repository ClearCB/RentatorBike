from src.capaPresentacion.crearHtml.crearBicisHtml import crearBodyBicis, bicisHtml
import pytest
import os

@pytest.mark.test_crearBodyBicis
def test_crearBodyBicis():

    body ='''
        <h3 class="titleBicis"> Bicis disponibles </h3>
        <hr>
        <section>
            <div id="contenedorPadre">
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicisolitaria.html"><img src="{imagenBici}" alt="bicicleta de la marca {marca} y tipo {tipo}"></a>
                    </div>   
                    <div class="contenedor_info">
                        <h5>{tipo}</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: {estado}</li> 
                                <li>Groupset: {groupset}</li> 
                                <li>Talla: {talla}</li> 
                                <li>Tamaño de ruedas: {ruedas}</li> 
                                <li>Precio por dia: {precio}</li> 
                                <li>Complementos disponibles: {complementos}</li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en {rental}</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>'''

    assert crearBodyBicis() == body

@pytest.mark.test_crearBicisHtml
def test_crearBicisHtml():

    bicisHtml()
    assert os.path.isfile("C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\second_pages\\bicis.html") == True

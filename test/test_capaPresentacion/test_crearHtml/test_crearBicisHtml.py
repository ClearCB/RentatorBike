from src.capaPresentacion.crearHtml.crearBicisHtml import crearBodyBicis, bicisHtml
from src.capaDatos.listarDatosMongo import respuestaText, listarBicis
from src.capaDatos.peticionMongo import conseguirRespuestaDatos, mongoKey, mongoUrl
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
                        <a href="./bicissolitarias/bicissolitariaPA0102.html"><img src="http://imgfz.com/i/YaJj6u9.jpeg" alt="bicicleta de la marca specialized y tipo bici de ciudad electrica"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>bici de ciudad electrica</h5>
                        <div class="infoBike">
                            <ul> 
                                <li><b>Estado</b>: down</li> 
                                <li><b>Marca</b>: specialized</li> 
                                <li><b>Groupset</b>: kask</li> 
                                <li><b>Talla</b>: s</li> 
                                <li><b>Tamaño de ruedas</b>: 26</li> 
                                <li><b>Precio por dia</b>: 15</li> 
                                <li><b>Complementos disponibles</b>: casco luz bomba guardabarros candado potenciometro </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en bibike</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaPA0201.html"><img src="http://imgfz.com/i/rBA18ZL.jpeg" alt="bicicleta de la marca specialized y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>e-mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li><b>Estado</b>: up</li> 
                                <li><b>Marca</b>: specialized</li> 
                                <li><b>Groupset</b>: specialized</li> 
                                <li><b>Talla</b>: l</li> 
                                <li><b>Tamaño de ruedas</b>: 27</li> 
                                <li><b>Precio por dia</b>: 14</li> 
                                <li><b>Complementos disponibles</b>: casco luz bomba guardabarros candado potenciometro </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en rentbima</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaPA0202.html"><img src="http://imgfz.com/i/yxr1LVT.jpeg" alt="bicicleta de la marca specialized y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>e-mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li><b>Estado</b>: down</li> 
                                <li><b>Marca</b>: specialized</li> 
                                <li><b>Groupset</b>: orbea</li> 
                                <li><b>Talla</b>: xl</li> 
                                <li><b>Tamaño de ruedas</b>: 29</li> 
                                <li><b>Precio por dia</b>: 16</li> 
                                <li><b>Complementos disponibles</b>: casco luz bomba guardabarros candado potenciometro sillita de bebe </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en rentbima</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaMA0101.html"><img src="http://imgfz.com/i/B1zMU2r.jpeg" alt="bicicleta de la marca specialized y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li><b>Estado</b>: up</li> 
                                <li><b>Marca</b>: specialized</li> 
                                <li><b>Groupset</b>: kask</li> 
                                <li><b>Talla</b>: m</li> 
                                <li><b>Tamaño de ruedas</b>: 26</li> 
                                <li><b>Precio por dia</b>: 18</li> 
                                <li><b>Complementos disponibles</b>: casco luz bomba guardabarros candado potenciometro sillita de bebe </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en habikemall</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaMA0102.html"><img src="http://imgfz.com/i/i649ZwL.jpeg" alt="bicicleta de la marca giant y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>e-mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li><b>Estado</b>: down</li> 
                                <li><b>Marca</b>: giant</li> 
                                <li><b>Groupset</b>: specialized</li> 
                                <li><b>Talla</b>: m</li> 
                                <li><b>Tamaño de ruedas</b>: 26</li> 
                                <li><b>Precio por dia</b>: 17</li> 
                                <li><b>Complementos disponibles</b>: casco luz bomba guardabarros candado potenciometro </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en habikemall</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaMA0201.html"><img src="http://imgfz.com/i/A4W1wGp.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>bici de ciudad</h5>
                        <div class="infoBike">
                            <ul> 
                                <li><b>Estado</b>: up</li> 
                                <li><b>Marca</b>: cube</li> 
                                <li><b>Groupset</b>: kask</li> 
                                <li><b>Talla</b>: l</li> 
                                <li><b>Tamaño de ruedas</b>: 29</li> 
                                <li><b>Precio por dia</b>: 15</li> 
                                <li><b>Complementos disponibles</b>: casco luz bomba guardabarros candado potenciometro </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en rybm</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaMA0202.html"><img src="http://imgfz.com/i/kaSt31V.jpeg" alt="bicicleta de la marca giant y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li><b>Estado</b>: down</li> 
                                <li><b>Marca</b>: giant</li> 
                                <li><b>Groupset</b>: orbea</li> 
                                <li><b>Talla</b>: xs</li> 
                                <li><b>Tamaño de ruedas</b>: 26</li> 
                                <li><b>Precio por dia</b>: 15</li> 
                                <li><b>Complementos disponibles</b>: casco luz bomba guardabarros candado </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en rybm</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaAL0101.html"><img src="http://imgfz.com/i/lDAfFpc.jpeg" alt="bicicleta de la marca giant y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li><b>Estado</b>: up</li> 
                                <li><b>Marca</b>: giant</li> 
                                <li><b>Groupset</b>: specialized</li> 
                                <li><b>Talla</b>: l</li> 
                                <li><b>Tamaño de ruedas</b>: 26</li> 
                                <li><b>Precio por dia</b>: 14</li> 
                                <li><b>Complementos disponibles</b>: casco luz guardabarros candado potenciometro sillita de bebe </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en bikeandgo</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaAL0102.html"><img src="http://imgfz.com/i/rovgac9.jpeg" alt="bicicleta de la marca specialized y tipo bici de ciudad electrica"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>bici de ciudad electrica</h5>
                        <div class="infoBike">
                            <ul> 
                                <li><b>Estado</b>: down</li> 
                                <li><b>Marca</b>: specialized</li> 
                                <li><b>Groupset</b>: kask</li> 
                                <li><b>Talla</b>: xl</li> 
                                <li><b>Tamaño de ruedas</b>: 26</li> 
                                <li><b>Precio por dia</b>: 16</li> 
                                <li><b>Complementos disponibles</b>: casco luz bomba guardabarros candado potenciometro sillita de bebe </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en bikeandgo</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaAL0201.html"><img src="http://imgfz.com/i/yXMpcKR.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>bici de ciudad</h5>
                        <div class="infoBike">
                            <ul> 
                                <li><b>Estado</b>: up</li> 
                                <li><b>Marca</b>: cube</li> 
                                <li><b>Groupset</b>: kask</li> 
                                <li><b>Talla</b>: l</li> 
                                <li><b>Tamaño de ruedas</b>: 26</li> 
                                <li><b>Precio por dia</b>: 18</li> 
                                <li><b>Complementos disponibles</b>: casco luz bomba guardabarros candado potenciometro sillita de bebe </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en speedyrent</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaAL0202.html"><img src="http://imgfz.com/i/q5d318P.jpeg" alt="bicicleta de la marca giant y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li><b>Estado</b>: down</li> 
                                <li><b>Marca</b>: giant</li> 
                                <li><b>Groupset</b>: specialized</li> 
                                <li><b>Talla</b>: m</li> 
                                <li><b>Tamaño de ruedas</b>: 27</li> 
                                <li><b>Precio por dia</b>: 17</li> 
                                <li><b>Complementos disponibles</b>: casco luz bomba guardabarros potenciometro </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en speedyrent</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaSO0101.html"><img src="http://imgfz.com/i/DYxBSaC.jpeg" alt="bicicleta de la marca cannondale y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>e-mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li><b>Estado</b>: up</li> 
                                <li><b>Marca</b>: cannondale</li> 
                                <li><b>Groupset</b>: giro</li> 
                                <li><b>Talla</b>: </li> 
                                <li><b>Tamaño de ruedas</b>: 26</li> 
                                <li><b>Precio por dia</b>: 15</li> 
                                <li><b>Complementos disponibles</b>: casco luz bomba guardabarros candado potenciometro </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en energylegs</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaSO0102.html"><img src="http://imgfz.com/i/I8Q0myp.jpeg" alt="bicicleta de la marca cube y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>e-mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li><b>Estado</b>: down</li> 
                                <li><b>Marca</b>: cube</li> 
                                <li><b>Groupset</b>: giro</li> 
                                <li><b>Talla</b>: l</li> 
                                <li><b>Tamaño de ruedas</b>: 27</li> 
                                <li><b>Precio por dia</b>: 15</li> 
                                <li><b>Complementos disponibles</b>: casco luz bomba guardabarros candado potenciometro </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en energylegs</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaSO0201.html"><img src="http://imgfz.com/i/pMB1Qkq.jpeg" alt="bicicleta de la marca giant y tipo bici de carretera"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>bici de carretera</h5>
                        <div class="infoBike">
                            <ul> 
                                <li><b>Estado</b>: up</li> 
                                <li><b>Marca</b>: giant</li> 
                                <li><b>Groupset</b>: giro</li> 
                                <li><b>Talla</b>: m</li> 
                                <li><b>Tamaño de ruedas</b>: 26</li> 
                                <li><b>Precio por dia</b>: 14</li> 
                                <li><b>Complementos disponibles</b>: casco luz bomba guardabarros candado potenciometro </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en rentingmanakia</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaSO0202.html"><img src="http://imgfz.com/i/n0APhL1.jpeg" alt="bicicleta de la marca specialized y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>bici de ciudad</h5>
                        <div class="infoBike">
                            <ul> 
                                <li><b>Estado</b>: down</li> 
                                <li><b>Marca</b>: specialized</li> 
                                <li><b>Groupset</b>: orbea</li> 
                                <li><b>Talla</b>: xl</li> 
                                <li><b>Tamaño de ruedas</b>: 27</li> 
                                <li><b>Precio por dia</b>: 16</li> 
                                <li><b>Complementos disponibles</b>: casco luz bomba guardabarros candado potenciometro sillita de bebe </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en rentingmanakia</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaCA0101.html"><img src="http://imgfz.com/i/7VOlN5y.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad electrica"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>bici de ciudad electrica</h5>
                        <div class="infoBike">
                            <ul> 
                                <li><b>Estado</b>: up</li> 
                                <li><b>Marca</b>: cube</li> 
                                <li><b>Groupset</b>: kona</li> 
                                <li><b>Talla</b>: l</li> 
                                <li><b>Tamaño de ruedas</b>: 26</li> 
                                <li><b>Precio por dia</b>: 18</li> 
                                <li><b>Complementos disponibles</b>: casco luz bomba guardabarros candado potenciometro sillita de bebe </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en touristbike</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaCA0102.html"><img src="http://imgfz.com/i/U8Mt6wR.jpeg" alt="bicicleta de la marca giant y tipo bici de carretera electrica"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>bici de carretera electrica</h5>
                        <div class="infoBike">
                            <ul> 
                                <li><b>Estado</b>: down</li> 
                                <li><b>Marca</b>: giant</li> 
                                <li><b>Groupset</b>: giro</li> 
                                <li><b>Talla</b>: xs</li> 
                                <li><b>Tamaño de ruedas</b>: 26</li> 
                                <li><b>Precio por dia</b>: 17</li> 
                                <li><b>Complementos disponibles</b>: casco luz bomba guardabarros candado potenciometro sillita de bebe </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en touristbike</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaCA0201.html"><img src="http://imgfz.com/i/tXK4M06.jpeg" alt="bicicleta de la marca cannondale y tipo bici de carretera electrica"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>bici de carretera electrica</h5>
                        <div class="infoBike">
                            <ul> 
                                <li><b>Estado</b>: up</li> 
                                <li><b>Marca</b>: cannondale</li> 
                                <li><b>Groupset</b>: specialized</li> 
                                <li><b>Talla</b>: m</li> 
                                <li><b>Tamaño de ruedas</b>: 29</li> 
                                <li><b>Precio por dia</b>: 15</li> 
                                <li><b>Complementos disponibles</b>: casco luz bomba guardabarros candado potenciometro </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en rentalride</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaCA0202.html"><img src="http://imgfz.com/i/edw4hMz.jpeg" alt="bicicleta de la marca cube y tipo bici de carretera"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>bici de carretera</h5>
                        <div class="infoBike">
                            <ul> 
                                <li><b>Estado</b>: down</li> 
                                <li><b>Marca</b>: cube</li> 
                                <li><b>Groupset</b>: kona</li> 
                                <li><b>Talla</b>: xs</li> 
                                <li><b>Tamaño de ruedas</b>: 27</li> 
                                <li><b>Precio por dia</b>: 15</li> 
                                <li><b>Complementos disponibles</b>: casco luz bomba guardabarros candado </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en rentalride</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaPA0101.html"><img src="http://imgfz.com/i/CiZJnhA.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>bici de ciudad</h5>
                        <div class="infoBike">
                            <ul> 
                                <li><b>Estado</b>: up</li> 
                                <li><b>Marca</b>: cube</li> 
                                <li><b>Groupset</b>: kask</li> 
                                <li><b>Talla</b>: x</li> 
                                <li><b>Tamaño de ruedas</b>: 29</li> 
                                <li><b>Precio por dia</b>: 15</li> 
                                <li><b>Complementos disponibles</b>: casco luz bomba guardabarros candado potenciometro </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en bibike</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>'''
    assert crearBodyBicis(listarBicis(respuestaText(conseguirRespuestaDatos( mongoKey(), mongoUrl())))) == body

@pytest.mark.test_crearBicisHtml
def test_crearBicisHtml():

    ruta = os.path.relpath(".\\docs\\second_pages\\bicis.html")
    bicisHtml(listarBicis(respuestaText(conseguirRespuestaDatos( mongoKey(), mongoUrl()))))
    assert os.path.isfile(ruta) == True

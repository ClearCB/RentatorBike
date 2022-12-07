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
                        <a href="./bicissolitarias/bicissolitariaPA0101.html"><img src="http://imgfz.com/i/CiZJnhA.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>bici de ciudad</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: up</li> 
                                <li>Marca: cube</li> 
                                <li>Groupset: kask</li> 
                                <li>Talla: x</li> 
                                <li>Tamaño de ruedas: 29</li> 
                                <li>Precio por dia: 15</li> 
                                <li>Complementos disponibles: casco luz bomba guardabarros candado potenciometro </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en bibike</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaPA0102.html"><img src="http://imgfz.com/i/YaJj6u9.jpeg" alt="bicicleta de la marca specialized y tipo bici de ciudad electrica"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>bici de ciudad electrica</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: down</li> 
                                <li>Marca: specialized</li> 
                                <li>Groupset: kask</li> 
                                <li>Talla: s</li> 
                                <li>Tamaño de ruedas: 26</li> 
                                <li>Precio por dia: 15</li> 
                                <li>Complementos disponibles: casco luz bomba guardabarros candado potenciometro </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en bibike</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaPA0201.html"><img src="http://imgfz.com/i/kaSt31V.jpeg" alt="bicicleta de la marca specialized y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>e-mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: up</li> 
                                <li>Marca: specialized</li> 
                                <li>Groupset: specialized</li> 
                                <li>Talla: l</li> 
                                <li>Tamaño de ruedas: 27</li> 
                                <li>Precio por dia: 14</li> 
                                <li>Complementos disponibles: casco luz bomba guardabarros candado potenciometro </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en rentbima</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaPA0202.html"><img src="http://imgfz.com/i/bn1AQ2q.jpeg" alt="bicicleta de la marca specialized y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>e-mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: down</li> 
                                <li>Marca: specialized</li> 
                                <li>Groupset: orbea</li> 
                                <li>Talla: xl</li> 
                                <li>Tamaño de ruedas: 29</li> 
                                <li>Precio por dia: 16</li> 
                                <li>Complementos disponibles: casco luz bomba guardabarros candado potenciometro sillita de bebe </li> 
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
                                <li>Estado: up</li> 
                                <li>Marca: specialized</li> 
                                <li>Groupset: kask</li> 
                                <li>Talla: m</li> 
                                <li>Tamaño de ruedas: 26</li> 
                                <li>Precio por dia: 18</li> 
                                <li>Complementos disponibles: casco luz bomba guardabarros candado potenciometro sillita de bebe </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en habikemall</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaMA0102.html"><img src="http://imgfz.com/i/PjOVTLa.jpeg" alt="bicicleta de la marca giant y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>e-mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: down</li> 
                                <li>Marca: giant</li> 
                                <li>Groupset: specialized</li> 
                                <li>Talla: m</li> 
                                <li>Tamaño de ruedas: 26</li> 
                                <li>Precio por dia: 17</li> 
                                <li>Complementos disponibles: casco luz bomba guardabarros candado potenciometro </li> 
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
                                <li>Estado: up</li> 
                                <li>Marca: cube</li> 
                                <li>Groupset: kask</li> 
                                <li>Talla: l</li> 
                                <li>Tamaño de ruedas: 29</li> 
                                <li>Precio por dia: 15</li> 
                                <li>Complementos disponibles: casco luz bomba guardabarros candado potenciometro </li> 
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
                                <li>Estado: down</li> 
                                <li>Marca: giant</li> 
                                <li>Groupset: orbea</li> 
                                <li>Talla: xs</li> 
                                <li>Tamaño de ruedas: 26</li> 
                                <li>Precio por dia: 15</li> 
                                <li>Complementos disponibles: casco luz bomba guardabarros candado </li> 
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
                                <li>Estado: up</li> 
                                <li>Marca: giant</li> 
                                <li>Groupset: specialized</li> 
                                <li>Talla: l</li> 
                                <li>Tamaño de ruedas: 26</li> 
                                <li>Precio por dia: 14</li> 
                                <li>Complementos disponibles: casco luz guardabarros candado potenciometro sillita de bebe </li> 
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
                                <li>Estado: down</li> 
                                <li>Marca: specialized</li> 
                                <li>Groupset: kask</li> 
                                <li>Talla: xl</li> 
                                <li>Tamaño de ruedas: 26</li> 
                                <li>Precio por dia: 16</li> 
                                <li>Complementos disponibles: casco luz bomba guardabarros candado potenciometro sillita de bebe </li> 
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
                                <li>Estado: up</li> 
                                <li>Marca: cube</li> 
                                <li>Groupset: kask</li> 
                                <li>Talla: l</li> 
                                <li>Tamaño de ruedas: 26</li> 
                                <li>Precio por dia: 18</li> 
                                <li>Complementos disponibles: casco luz bomba guardabarros candado potenciometro sillita de bebe </li> 
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
                                <li>Estado: down</li> 
                                <li>Marca: giant</li> 
                                <li>Groupset: specialized</li> 
                                <li>Talla: m</li> 
                                <li>Tamaño de ruedas: 27</li> 
                                <li>Precio por dia: 17</li> 
                                <li>Complementos disponibles: casco luz bomba guardabarros potenciometro </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en speedyrent</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaSO0101.html"><img src="http://imgfz.com/i/NvAWrJi.jpeg" alt="bicicleta de la marca cannondale y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>e-mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: up</li> 
                                <li>Marca: cannondale</li> 
                                <li>Groupset: giro</li> 
                                <li>Talla: </li> 
                                <li>Tamaño de ruedas: 26</li> 
                                <li>Precio por dia: 15</li> 
                                <li>Complementos disponibles: casco luz bomba guardabarros candado potenciometro </li> 
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
                                <li>Estado: down</li> 
                                <li>Marca: cube</li> 
                                <li>Groupset: giro</li> 
                                <li>Talla: l</li> 
                                <li>Tamaño de ruedas: 27</li> 
                                <li>Precio por dia: 15</li> 
                                <li>Complementos disponibles: casco luz bomba guardabarros candado potenciometro </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en energylegs</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaSO0201.html"><img src="http://imgfz.com/i/2eNLWgp.jpeg" alt="bicicleta de la marca giant y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: up</li> 
                                <li>Marca: giant</li> 
                                <li>Groupset: giro</li> 
                                <li>Talla: m</li> 
                                <li>Tamaño de ruedas: 26</li> 
                                <li>Precio por dia: 14</li> 
                                <li>Complementos disponibles: casco luz bomba guardabarros candado potenciometro </li> 
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
                                <li>Estado: down</li> 
                                <li>Marca: specialized</li> 
                                <li>Groupset: orbea</li> 
                                <li>Talla: xl</li> 
                                <li>Tamaño de ruedas: 27</li> 
                                <li>Precio por dia: 16</li> 
                                <li>Complementos disponibles: casco luz bomba guardabarros candado potenciometro sillita de bebe </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en rentingmanakia</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaCA0101.html"><img src="http://imgfz.com/i/u3NH9RI.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad electrica"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>bici de ciudad electrica</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: up</li> 
                                <li>Marca: cube</li> 
                                <li>Groupset: kona</li> 
                                <li>Talla: l</li> 
                                <li>Tamaño de ruedas: 26</li> 
                                <li>Precio por dia: 18</li> 
                                <li>Complementos disponibles: casco luz bomba guardabarros candado potenciometro sillita de bebe </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en touristbike</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaCA0102.html"><img src="http://imgfz.com/i/Gtuk9Ah.jpeg" alt="bicicleta de la marca giant y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: down</li> 
                                <li>Marca: giant</li> 
                                <li>Groupset: giro</li> 
                                <li>Talla: xs</li> 
                                <li>Tamaño de ruedas: 26</li> 
                                <li>Precio por dia: 17</li> 
                                <li>Complementos disponibles: casco luz bomba guardabarros candado potenciometro sillita de bebe </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en touristbike</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaCA0201.html"><img src="http://imgfz.com/i/nfUeIZh.jpeg" alt="bicicleta de la marca cannondale y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: up</li> 
                                <li>Marca: cannondale</li> 
                                <li>Groupset: specialized</li> 
                                <li>Talla: m</li> 
                                <li>Tamaño de ruedas: 29</li> 
                                <li>Precio por dia: 15</li> 
                                <li>Complementos disponibles: casco luz bomba guardabarros candado potenciometro </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en rentalride</p>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaCA0202.html"><img src="http://imgfz.com/i/8bkws5n.jpeg" alt="bicicleta de la marca cube y tipo bici de carretera"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>bici de carretera</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: down</li> 
                                <li>Marca: cube</li> 
                                <li>Groupset: kona</li> 
                                <li>Talla: xs</li> 
                                <li>Tamaño de ruedas: 27</li> 
                                <li>Precio por dia: 15</li> 
                                <li>Complementos disponibles: casco luz bomba guardabarros candado </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en rentalride</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>'''
    assert crearBodyBicis(listarBicis(respuestaText(conseguirRespuestaDatos( mongoKey(), mongoUrl())))) == body

@pytest.mark.test_crearBicisHtml
def test_crearBicisHtml():

    bicisHtml(listarBicis(respuestaText(conseguirRespuestaDatos( mongoKey(), mongoUrl()))))
    assert os.path.isfile("C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\second_pages\\bicis.html") == True

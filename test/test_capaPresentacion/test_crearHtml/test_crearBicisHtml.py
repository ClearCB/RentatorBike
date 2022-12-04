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
                        <a href="./bicissolitarias/bicisolitaria.html"><img src="http://imgfz.com/i/0bzEH63.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>bici de ciudad</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: up</li> 
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
                        <a href="./bicissolitarias/bicisolitaria.html"><img src="http://imgfz.com/i/3WgxtCF.jpeg" alt="bicicleta de la marca specialized y tipo bici de ciudad electrica"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>bici de ciudad electrica</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: down</li> 
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
                        <a href="./bicissolitarias/bicisolitaria.html"><img src="http://imgfz.com/i/uLz1k3I.png" alt="bicicleta de la marca specialized y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>e-mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: up</li> 
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
                        <a href="./bicissolitarias/bicisolitaria.html"><img src="http://imgfz.com/i/f2OzdrC.jpeg" alt="bicicleta de la marca specialized y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>e-mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: down</li> 
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
                        <a href="./bicissolitarias/bicisolitaria.html"><img src="http://imgfz.com/i/ZYmUuQV.jpeg " alt="bicicleta de la marca specialized y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: up</li> 
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
                        <a href="./bicissolitarias/bicisolitaria.html"><img src="http://imgfz.com/i/fLM1rap.jpeg" alt="bicicleta de la marca giant y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>e-mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: down</li> 
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
                        <a href="./bicissolitarias/bicisolitaria.html"><img src="http://imgfz.com/i/yspcgEA.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>bici de ciudad</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: up</li> 
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
                        <a href="./bicissolitarias/bicisolitaria.html"><img src="http://imgfz.com/i/VSt9ABZ.jpeg" alt="bicicleta de la marca giant y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: down</li> 
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
                        <a href="./bicissolitarias/bicisolitaria.html"><img src="http://imgfz.com/i/oFsXH7a.jpeg" alt="bicicleta de la marca giant y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: up</li> 
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
                        <a href="./bicissolitarias/bicisolitaria.html"><img src="http://imgfz.com/i/ASf5R7d.jpeg" alt="bicicleta de la marca specialized y tipo bici de ciudad electrica"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>bici de ciudad electrica</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: down</li> 
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
                        <a href="./bicissolitarias/bicisolitaria.html"><img src="http://imgfz.com/i/u1qZJXl.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>bici de ciudad</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: up</li> 
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
                        <a href="./bicissolitarias/bicisolitaria.html"><img src="http://imgfz.com/i/F9tJs46.jpeg" alt="bicicleta de la marca giant y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: down</li> 
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
                        <a href="./bicissolitarias/bicisolitaria.html"><img src="http://imgfz.com/i/aoBKA5Z.jpeg" alt="bicicleta de la marca cannondale y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>e-mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: up</li> 
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
                        <a href="./bicissolitarias/bicisolitaria.html"><img src="http://imgfz.com/i/cgK7Uxf.jpeg" alt="bicicleta de la marca cube y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>e-mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: down</li> 
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
                        <a href="./bicissolitarias/bicisolitaria.html"><img src="http://imgfz.com/i/baoeuFc.jpeg" alt="bicicleta de la marca giant y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: up</li> 
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
                        <a href="./bicissolitarias/bicisolitaria.html"><img src="http://imgfz.com/i/g31AHse.jpeg" alt="bicicleta de la marca specialized y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>bici de ciudad</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: down</li> 
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
                        <a href="./bicissolitarias/bicisolitaria.html"><img src="http://imgfz.com/i/ZoKTLvs.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad electrica"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>bici de ciudad electrica</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: up</li> 
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
                        <a href="./bicissolitarias/bicisolitaria.html"><img src="http://imgfz.com/i/p8eYINZ.jpeg" alt="bicicleta de la marca giant y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: down</li> 
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
                        <a href="./bicissolitarias/bicisolitaria.html"><img src="http://imgfz.com/i/1VcN9HE.jpeg" alt="bicicleta de la marca cannondale y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>mtb</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: up</li> 
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
                        <a href="./bicissolitarias/bicisolitaria.html"><img src="http://imgfz.com/i/b4jVFNa.jpeg" alt="bicicleta de la marca cube y tipo bici de carretera"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>bici de carretera</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: down</li> 
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

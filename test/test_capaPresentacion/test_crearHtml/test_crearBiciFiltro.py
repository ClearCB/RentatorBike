from src.capaPresentacion.crearHtml.crearBiciMarcaHtml import esFiltro, crearBodyBiciMarca
from src.capaPresentacion.crearHtml.crearBiciCategHtml import  crearBodyBiciCategoria
from src.capaPresentacion.crearHtml.crearBiciCaractHtml import  crearBodyBiciCaracteristica
from src.capaDatos.peticionMongo import respuestaMongo
from src.capaDatos.listarDatosMongo import respuestaText, listarBicis

listaBicis = listarBicis(respuestaText(respuestaMongo()))


import pytest

# Comprueba que la función ejecuta correctamente el filtro e inserta las bicis correspondientes.
@pytest.mark.test_esFiltro
def test_esFiltro():
    bici =  {
    '_id': 'ObjectId("63850e0400b41044eddde3c7")',
    '_idbike': 'PA0101',
    'state': 'up',
    'type': 'bici de ciudad',
    'techinfo': { 'groupset': 'kask', 'size': 'x', 'wheels': '29', 'brand': 'cube' },
    'complements': [
      'casco',
      'luz',
      'bomba',
      'guardabarros',
      'candado',
      'potenciometro'
    ],
    'prize_euros_days': '15',
    'where': [{"_idrental":"PA01","company_name":"bibike","address":{"zip":"07006","street":"joan alcover n7  ","country":"espana","town":"palma"},"social_media":{"twitter":"@bibike","instagram":"@bibike"},"contact":{"num":"678598234","email":"bibike@contact.eu"},"promotions":"15% descuento","stock":"2",'bikes': {'bikes_up':{'_idbikes': [ 'PA0101' ]},
        'bikes_down':{'_idbikes':['PA0102']}},'img':"http://imgfz.com/i/2sS6E8d.jpeg",'icono':'http://imgfz.com/i/x1Re2Mf.png'}],'img':'http://imgfz.com/i/CiZJnhA.jpeg'}


    biciFiltrada = '''
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaPA0101.html"><img src="http://imgfz.com/i/CiZJnhA.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
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
                </div>'''

    assert esFiltro(bici,"cube") == biciFiltrada

# Comprueba que se crear correctamente el body de bicipormarca.html
@pytest.mark.test_crearBodyBiciMarca
def test_crearBodyBiciMarca():

    bodyHtmlMarca='''
        <h3 class="titleBicis"> Bicis por marca </h3><hr>
        <section>
            <div id="contenedorPadre">
                <h4 class="filtrotitulo" id="cube"> Cube </h4>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaPA0101.html"><img src="http://imgfz.com/i/CiZJnhA.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaMA0201.html"><img src="http://imgfz.com/i/A4W1wGp.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaAL0201.html"><img src="http://imgfz.com/i/yXMpcKR.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaSO0102.html"><img src="http://imgfz.com/i/I8Q0myp.jpeg" alt="bicicleta de la marca cube y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaCA0101.html"><img src="http://imgfz.com/i/7VOlN5y.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad electrica"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaCA0202.html"><img src="http://imgfz.com/i/edw4hMz.jpeg" alt="bicicleta de la marca cube y tipo bici de carretera"></a>
                    </div>
                    <div class="contenedor_info">
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
                <h4 class="filtrotitulo" id="specialized"> Specialized</h4>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaPA0102.html"><img src="http://imgfz.com/i/YaJj6u9.jpeg" alt="bicicleta de la marca specialized y tipo bici de ciudad electrica"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaPA0201.html"><img src="http://imgfz.com/i/rBA18ZL.jpeg" alt="bicicleta de la marca specialized y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaPA0202.html"><img src="http://imgfz.com/i/yxr1LVT.jpeg" alt="bicicleta de la marca specialized y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaAL0102.html"><img src="http://imgfz.com/i/rovgac9.jpeg" alt="bicicleta de la marca specialized y tipo bici de ciudad electrica"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaSO0202.html"><img src="http://imgfz.com/i/n0APhL1.jpeg" alt="bicicleta de la marca specialized y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
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
                <h4 class="filtrotitulo" id="giant"> Giant</h4>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaMA0102.html"><img src="http://imgfz.com/i/i649ZwL.jpeg" alt="bicicleta de la marca giant y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaMA0202.html"><img src="http://imgfz.com/i/kaSt31V.jpeg" alt="bicicleta de la marca giant y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaAL0202.html"><img src="http://imgfz.com/i/q5d318P.jpeg" alt="bicicleta de la marca giant y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaSO0201.html"><img src="http://imgfz.com/i/pMB1Qkq.jpeg" alt="bicicleta de la marca giant y tipo bici de carretera"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaCA0102.html"><img src="http://imgfz.com/i/U8Mt6wR.jpeg" alt="bicicleta de la marca giant y tipo bici de carretera electrica"></a>
                    </div>
                    <div class="contenedor_info">
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
                <h4 class="filtrotitulo" id="cannondale"> Cannondale</h4>
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaSO0101.html"><img src="http://imgfz.com/i/DYxBSaC.jpeg" alt="bicicleta de la marca cannondale y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaCA0201.html"><img src="http://imgfz.com/i/tXK4M06.jpeg" alt="bicicleta de la marca cannondale y tipo bici de carretera electrica"></a>
                    </div>
                    <div class="contenedor_info">
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
            </div>
        </section>'''
    assert crearBodyBiciMarca(listaBicis)==bodyHtmlMarca

# Comprueba que se crear correctamente el body de biciscategoria.html
@pytest.mark.test_crearBodyBiciCaract
def test_crearBodyBiciCaract():

    bodyHtmlCaract='''
        <section>
            <h3 class="titleBicis"> Bicis por caracteristica </h3>
            <div class="categorias">
                <a href="#cuadro" target="_self"><div class="nombrecategorias"><h4>Por tamaño del cuadro</h4></div></a>
                <a href="#rueda" target="_self"><div class="nombrecategorias"><h4>Por tamaño de las ruedas</h4></div></a>
                <a href="#groupset" target="_self"><div class="nombrecategorias"><h4>Por marca del groupset</h4></div></a>
            </div><hr>
            <div id="contenedorPadre">
                    <h4 class="filtrotitulo"><span id="cuadro"></span>Tamaño del cuadro </h4>
                    <h5 class="filtrocaract"> Talla XS</h5> 
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaMA0202.html"><img src="http://imgfz.com/i/kaSt31V.jpeg" alt="bicicleta de la marca giant y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaCA0102.html"><img src="http://imgfz.com/i/U8Mt6wR.jpeg" alt="bicicleta de la marca giant y tipo bici de carretera electrica"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaCA0202.html"><img src="http://imgfz.com/i/edw4hMz.jpeg" alt="bicicleta de la marca cube y tipo bici de carretera"></a>
                    </div>
                    <div class="contenedor_info">
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
                <h5 class="filtrocaract"> Talla S</h5> 
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaPA0102.html"><img src="http://imgfz.com/i/YaJj6u9.jpeg" alt="bicicleta de la marca specialized y tipo bici de ciudad electrica"></a>
                    </div>
                    <div class="contenedor_info">
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
                <h5 class="filtrocaract"> Talla M</h5> 
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaMA0101.html"><img src="http://imgfz.com/i/B1zMU2r.jpeg" alt="bicicleta de la marca specialized y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaMA0102.html"><img src="http://imgfz.com/i/i649ZwL.jpeg" alt="bicicleta de la marca giant y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaAL0202.html"><img src="http://imgfz.com/i/q5d318P.jpeg" alt="bicicleta de la marca giant y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaSO0201.html"><img src="http://imgfz.com/i/pMB1Qkq.jpeg" alt="bicicleta de la marca giant y tipo bici de carretera"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaCA0201.html"><img src="http://imgfz.com/i/tXK4M06.jpeg" alt="bicicleta de la marca cannondale y tipo bici de carretera electrica"></a>
                    </div>
                    <div class="contenedor_info">
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
                <h5 class="filtrocaract"> Talla L</h5> 
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaPA0201.html"><img src="http://imgfz.com/i/rBA18ZL.jpeg" alt="bicicleta de la marca specialized y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaMA0201.html"><img src="http://imgfz.com/i/A4W1wGp.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaAL0101.html"><img src="http://imgfz.com/i/lDAfFpc.jpeg" alt="bicicleta de la marca giant y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaAL0201.html"><img src="http://imgfz.com/i/yXMpcKR.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaSO0102.html"><img src="http://imgfz.com/i/I8Q0myp.jpeg" alt="bicicleta de la marca cube y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaCA0101.html"><img src="http://imgfz.com/i/7VOlN5y.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad electrica"></a>
                    </div>
                    <div class="contenedor_info">
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
                <h5 class="filtrocaract"> Talla XL</h5> 
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaPA0202.html"><img src="http://imgfz.com/i/yxr1LVT.jpeg" alt="bicicleta de la marca specialized y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaAL0102.html"><img src="http://imgfz.com/i/rovgac9.jpeg" alt="bicicleta de la marca specialized y tipo bici de ciudad electrica"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaSO0202.html"><img src="http://imgfz.com/i/n0APhL1.jpeg" alt="bicicleta de la marca specialized y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
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
                <h4 class="filtrotitulo"> <span id="rueda"></span> Tamaño de la rueda </h4>
                <h5 class="filtrocaract"> Talla 26'</h5> 
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaPA0102.html"><img src="http://imgfz.com/i/YaJj6u9.jpeg" alt="bicicleta de la marca specialized y tipo bici de ciudad electrica"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaMA0101.html"><img src="http://imgfz.com/i/B1zMU2r.jpeg" alt="bicicleta de la marca specialized y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaMA0102.html"><img src="http://imgfz.com/i/i649ZwL.jpeg" alt="bicicleta de la marca giant y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaMA0202.html"><img src="http://imgfz.com/i/kaSt31V.jpeg" alt="bicicleta de la marca giant y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaSO0101.html"><img src="http://imgfz.com/i/DYxBSaC.jpeg" alt="bicicleta de la marca cannondale y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaSO0201.html"><img src="http://imgfz.com/i/pMB1Qkq.jpeg" alt="bicicleta de la marca giant y tipo bici de carretera"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaCA0101.html"><img src="http://imgfz.com/i/7VOlN5y.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad electrica"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaCA0102.html"><img src="http://imgfz.com/i/U8Mt6wR.jpeg" alt="bicicleta de la marca giant y tipo bici de carretera electrica"></a>
                    </div>
                    <div class="contenedor_info">
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
                <h5 class="filtrocaract"> Talla 27'</h5> 
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaPA0201.html"><img src="http://imgfz.com/i/rBA18ZL.jpeg" alt="bicicleta de la marca specialized y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaAL0202.html"><img src="http://imgfz.com/i/q5d318P.jpeg" alt="bicicleta de la marca giant y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaSO0102.html"><img src="http://imgfz.com/i/I8Q0myp.jpeg" alt="bicicleta de la marca cube y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaSO0202.html"><img src="http://imgfz.com/i/n0APhL1.jpeg" alt="bicicleta de la marca specialized y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaCA0202.html"><img src="http://imgfz.com/i/edw4hMz.jpeg" alt="bicicleta de la marca cube y tipo bici de carretera"></a>
                    </div>
                    <div class="contenedor_info">
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
                <h5 class="filtrocaract"> Talla 29'</h5> 
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaPA0101.html"><img src="http://imgfz.com/i/CiZJnhA.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaPA0202.html"><img src="http://imgfz.com/i/yxr1LVT.jpeg" alt="bicicleta de la marca specialized y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaMA0201.html"><img src="http://imgfz.com/i/A4W1wGp.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaCA0201.html"><img src="http://imgfz.com/i/tXK4M06.jpeg" alt="bicicleta de la marca cannondale y tipo bici de carretera electrica"></a>
                    </div>
                    <div class="contenedor_info">
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
                <h4 class="filtrotitulo"> <span id="groupset"></span>Marca del groupset </h4>
                <h5 class="filtrocaract"> Kask</h5>
                <h5 class="filtrocaract"> Specialized </h5> 
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaPA0201.html"><img src="http://imgfz.com/i/rBA18ZL.jpeg" alt="bicicleta de la marca specialized y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaMA0102.html"><img src="http://imgfz.com/i/i649ZwL.jpeg" alt="bicicleta de la marca giant y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaAL0101.html"><img src="http://imgfz.com/i/lDAfFpc.jpeg" alt="bicicleta de la marca giant y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaAL0202.html"><img src="http://imgfz.com/i/q5d318P.jpeg" alt="bicicleta de la marca giant y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaCA0201.html"><img src="http://imgfz.com/i/tXK4M06.jpeg" alt="bicicleta de la marca cannondale y tipo bici de carretera electrica"></a>
                    </div>
                    <div class="contenedor_info">
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
                <h5 class="filtrocaract"> Kona</h5> 
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaCA0101.html"><img src="http://imgfz.com/i/7VOlN5y.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad electrica"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaCA0202.html"><img src="http://imgfz.com/i/edw4hMz.jpeg" alt="bicicleta de la marca cube y tipo bici de carretera"></a>
                    </div>
                    <div class="contenedor_info">
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
                <h5 class="filtrocaract">Orbea</h5> 
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaPA0202.html"><img src="http://imgfz.com/i/yxr1LVT.jpeg" alt="bicicleta de la marca specialized y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaMA0202.html"><img src="http://imgfz.com/i/kaSt31V.jpeg" alt="bicicleta de la marca giant y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaSO0202.html"><img src="http://imgfz.com/i/n0APhL1.jpeg" alt="bicicleta de la marca specialized y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
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
            </div>
        </section>'''
    assert crearBodyBiciCaracteristica(listaBicis)==bodyHtmlCaract

# Comprueba que se crear correctamente el body de .html
@pytest.mark.test_crearBodyBiciCateg
def test_crearBodyBiciCateg():

    bodyHtmlCateg='''
        <h3 class="titleBicis"> Bicis por categoria </h3>
        <section><hr>
            <div id="contenedorPadre">
                <h4 class="filtrotitulo" id="mtb"> MTB</h4> 
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaMA0101.html"><img src="http://imgfz.com/i/B1zMU2r.jpeg" alt="bicicleta de la marca specialized y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaMA0202.html"><img src="http://imgfz.com/i/kaSt31V.jpeg" alt="bicicleta de la marca giant y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaAL0202.html"><img src="http://imgfz.com/i/q5d318P.jpeg" alt="bicicleta de la marca giant y tipo mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                <h4 class="filtrotitulo" id="emtb"> e-MTB</h4> 
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaPA0201.html"><img src="http://imgfz.com/i/rBA18ZL.jpeg" alt="bicicleta de la marca specialized y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaPA0202.html"><img src="http://imgfz.com/i/yxr1LVT.jpeg" alt="bicicleta de la marca specialized y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaMA0102.html"><img src="http://imgfz.com/i/i649ZwL.jpeg" alt="bicicleta de la marca giant y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaSO0101.html"><img src="http://imgfz.com/i/DYxBSaC.jpeg" alt="bicicleta de la marca cannondale y tipo e-mtb"></a>
                    </div>
                    <div class="contenedor_info">
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
                <h4 class="filtrotitulo" id="carretera"> Carretera</h4> 
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaSO0201.html"><img src="http://imgfz.com/i/pMB1Qkq.jpeg" alt="bicicleta de la marca giant y tipo bici de carretera"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaCA0202.html"><img src="http://imgfz.com/i/edw4hMz.jpeg" alt="bicicleta de la marca cube y tipo bici de carretera"></a>
                    </div>
                    <div class="contenedor_info">
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
                <h4 class="filtrotitulo" id="ecarretera"> Carretera eléctrica</h4> 
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaCA0102.html"><img src="http://imgfz.com/i/U8Mt6wR.jpeg" alt="bicicleta de la marca giant y tipo bici de carretera electrica"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaCA0201.html"><img src="http://imgfz.com/i/tXK4M06.jpeg" alt="bicicleta de la marca cannondale y tipo bici de carretera electrica"></a>
                    </div>
                    <div class="contenedor_info">
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
                <h4 class="filtrotitulo" id="ciudad"> Bici de ciudad</h4> 
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaPA0101.html"><img src="http://imgfz.com/i/CiZJnhA.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaMA0201.html"><img src="http://imgfz.com/i/A4W1wGp.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaAL0201.html"><img src="http://imgfz.com/i/yXMpcKR.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaSO0202.html"><img src="http://imgfz.com/i/n0APhL1.jpeg" alt="bicicleta de la marca specialized y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
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
                <h4 class="filtrotitulo" id="eciudad"> Bici de ciudad eléctrica</h4> 
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaPA0102.html"><img src="http://imgfz.com/i/YaJj6u9.jpeg" alt="bicicleta de la marca specialized y tipo bici de ciudad electrica"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaAL0102.html"><img src="http://imgfz.com/i/rovgac9.jpeg" alt="bicicleta de la marca specialized y tipo bici de ciudad electrica"></a>
                    </div>
                    <div class="contenedor_info">
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
                        <a href="./bicissolitarias/bicissolitariaCA0101.html"><img src="http://imgfz.com/i/7VOlN5y.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad electrica"></a>
                    </div>
                    <div class="contenedor_info">
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
            </div>
        </section>'''
    assert crearBodyBiciCategoria(listaBicis)==bodyHtmlCateg
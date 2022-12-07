from src.capaPresentacion.crearHtml.crearRentalsHtml import  rentalsHtml, crearBodyRentals
from src.capaDatos.listarDatosMongo import listarRentals, respuestaText
from src.capaDatos.peticionMongo import conseguirRespuestaDatos, mongoKey ,mongoUrl
import pytest
import os

@pytest.mark.test_crearRentalsHtml
def test_crearRentalsHtml():

    rentalsHtml(listarRentals(respuestaText(conseguirRespuestaDatos(mongoKey(),mongoUrl()))))
    assert os.path.isfile("C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\second_pages\\rentals.html") == True

@pytest.mark.test_crearBodyRentals
def test_crearRentalsHtml():

    body ='''
            <div class="rentals">
                <div class="rentals__container">
                    <div class="rentals__titulo__logo">
                        <h3 class="rentals__titulo">
                            bibike 
                        </h3>
                        <div class="rentals__logo">
                            <img  class="rentalIcono" src="http://imgfz.com/i/x1Re2Mf.png" alt="foto del icono del rental bibike">
                        </div>
                    </div>
                    <div class="rentals__description">
                        <ul>
                            <li>Ubicacion: joan alcover n7  , palma (espana). 07006</li>
                            <li>Contacto: num(678598234) / email(bibike@contact.eu)</li>
                            <li>Redes sociales: instagram(@bibike) / twitter(@bibike)</li>
                            <li>Bicis disponibles: <a href='./bicissolitarias/bicissolitariaPA0101.html'>PA0101</a> </li>
                            <li>Bicis no disponibles: <a href='./bicissolitarias/bicissolitariaPA0102.html'>PA0102</a> </li>
                        </ul>
                    </div>
                    <div class="rentals__img__location">
                        <a href="#"><img class=fotoRental src="http://imgfz.com/i/2sS6E8d.jpeg" alt="foto de la ubicacion del rental bibike"></a>
                    </div>
                </div>
            </div>
            <div class="rentals">
                <div class="rentals__container">
                    <div class="rentals__titulo__logo">
                        <h3 class="rentals__titulo">
                            rentbima 
                        </h3>
                        <div class="rentals__logo">
                            <img  class="rentalIcono" src="http://imgfz.com/i/pUvx325.png" alt="foto del icono del rental rentbima">
                        </div>
                    </div>
                    <div class="rentals__description">
                        <ul>
                            <li>Ubicacion: plaza de espana, palma (espana). 07005</li>
                            <li>Contacto: num(738912213) / email(rentbima@contact.eu)</li>
                            <li>Redes sociales: instagram(@rentbima) / twitter(@rentbima)</li>
                            <li>Bicis disponibles: <a href='./bicissolitarias/bicissolitariaPA0201.html'>PA0201</a> </li>
                            <li>Bicis no disponibles: <a href='./bicissolitarias/bicissolitariaPA0202.html'>PA0202</a> </li>
                        </ul>
                    </div>
                    <div class="rentals__img__location">
                        <a href="#"><img class=fotoRental src="http://imgfz.com/i/YlsSQVf.jpeg" alt="foto de la ubicacion del rental rentbima"></a>
                    </div>
                </div>
            </div>
            <div class="rentals">
                <div class="rentals__container">
                    <div class="rentals__titulo__logo">
                        <h3 class="rentals__titulo">
                            habikemall 
                        </h3>
                        <div class="rentals__logo">
                            <img  class="rentalIcono" src="http://imgfz.com/i/UkQEme7.png" alt="foto del icono del rental habikemall">
                        </div>
                    </div>
                    <div class="rentals__description">
                        <ul>
                            <li>Ubicacion: sant joan n2, manacor (espana). 07500</li>
                            <li>Contacto: num(678523945) / email(habikemall@contact.eu)</li>
                            <li>Redes sociales: instagram(@habikemall) / twitter(@habikemall)</li>
                            <li>Bicis disponibles: <a href='./bicissolitarias/bicissolitariaMA0101.html'>MA0101</a> </li>
                            <li>Bicis no disponibles: <a href='./bicissolitarias/bicissolitariaMA0102.html'>MA0102</a> </li>
                        </ul>
                    </div>
                    <div class="rentals__img__location">
                        <a href="#"><img class=fotoRental src="http://imgfz.com/i/Iw2GXTb.jpeg" alt="foto de la ubicacion del rental habikemall"></a>
                    </div>
                </div>
            </div>
            <div class="rentals">
                <div class="rentals__container">
                    <div class="rentals__titulo__logo">
                        <h3 class="rentals__titulo">
                            rybm 
                        </h3>
                        <div class="rentals__logo">
                            <img  class="rentalIcono" src="http://imgfz.com/i/eKAiq7R.png" alt="foto del icono del rental rybm">
                        </div>
                    </div>
                    <div class="rentals__description">
                        <ul>
                            <li>Ubicacion: carrer des sol n10, manacor (espana). 07500</li>
                            <li>Contacto: num(666554223) / email(rybm@contact.eu)</li>
                            <li>Redes sociales: instagram(@rybm) / twitter(@rybm)</li>
                            <li>Bicis disponibles: <a href='./bicissolitarias/bicissolitariaMA0201.html'>MA0201</a> </li>
                            <li>Bicis no disponibles: <a href='./bicissolitarias/bicissolitariaMA0202.html'>MA0202</a> </li>
                        </ul>
                    </div>
                    <div class="rentals__img__location">
                        <a href="#"><img class=fotoRental src="http://imgfz.com/i/duK0xBn.jpeg" alt="foto de la ubicacion del rental rybm"></a>
                    </div>
                </div>
            </div>
            <div class="rentals">
                <div class="rentals__container">
                    <div class="rentals__titulo__logo">
                        <h3 class="rentals__titulo">
                            bikeandgo 
                        </h3>
                        <div class="rentals__logo">
                            <img  class="rentalIcono" src="http://imgfz.com/i/kfOGrD5.png" alt="foto del icono del rental bikeandgo">
                        </div>
                    </div>
                    <div class="rentals__description">
                        <ul>
                            <li>Ubicacion: carrer de la creu n7, alcudia (espana). 07400</li>
                            <li>Contacto: num(897524645) / email(bikeandgo@contact.eu)</li>
                            <li>Redes sociales: instagram(@bikeandgo) / twitter(@bikeandgo)</li>
                            <li>Bicis disponibles: <a href='./bicissolitarias/bicissolitariaAL0101.html'>AL0101</a> </li>
                            <li>Bicis no disponibles: <a href='./bicissolitarias/bicissolitariaAL0102.html'>AL0102</a> </li>
                        </ul>
                    </div>
                    <div class="rentals__img__location">
                        <a href="#"><img class=fotoRental src="http://imgfz.com/i/vWtjfA5.jpeg" alt="foto de la ubicacion del rental bikeandgo"></a>
                    </div>
                </div>
            </div>
            <div class="rentals">
                <div class="rentals__container">
                    <div class="rentals__titulo__logo">
                        <h3 class="rentals__titulo">
                            speedyrent 
                        </h3>
                        <div class="rentals__logo">
                            <img  class="rentalIcono" src="http://imgfz.com/i/S5up7Iy.png" alt="foto del icono del rental speedyrent">
                        </div>
                    </div>
                    <div class="rentals__description">
                        <ul>
                            <li>Ubicacion: carrer de menorca n3, alcudia (espana). 07400</li>
                            <li>Contacto: num(689496982) / email(speedyrent@contact.eu)</li>
                            <li>Redes sociales: instagram(@speedyrent) / twitter(@speedyrent)</li>
                            <li>Bicis disponibles: <a href='./bicissolitarias/bicissolitariaAL0201.html'>AL0201</a> </li>
                            <li>Bicis no disponibles: <a href='./bicissolitarias/bicissolitariaAL0202.html'>AL0202</a> </li>
                        </ul>
                    </div>
                    <div class="rentals__img__location">
                        <a href="#"><img class=fotoRental src="http://imgfz.com/i/brfKjYW.jpeg" alt="foto de la ubicacion del rental speedyrent"></a>
                    </div>
                </div>
            </div>
            <div class="rentals">
                <div class="rentals__container">
                    <div class="rentals__titulo__logo">
                        <h3 class="rentals__titulo">
                            energylegs 
                        </h3>
                        <div class="rentals__logo">
                            <img  class="rentalIcono" src="http://imgfz.com/i/8pomsKj.png" alt="foto del icono del rental energylegs">
                        </div>
                    </div>
                    <div class="rentals__description">
                        <ul>
                            <li>Ubicacion: av de asturias n10, soller (espana). 07100</li>
                            <li>Contacto: num(987166998) / email(energylegs@contact.eu)</li>
                            <li>Redes sociales: instagram(@energylegs) / twitter(@energylegs)</li>
                            <li>Bicis disponibles: <a href='./bicissolitarias/bicissolitariaSO0101.html'>SO0101</a> </li>
                            <li>Bicis no disponibles: <a href='./bicissolitarias/bicissolitariaSO0102.html'>SO0102</a> </li>
                        </ul>
                    </div>
                    <div class="rentals__img__location">
                        <a href="#"><img class=fotoRental src="http://imgfz.com/i/AZr2KHT.jpeg" alt="foto de la ubicacion del rental energylegs"></a>
                    </div>
                </div>
            </div>
            <div class="rentals">
                <div class="rentals__container">
                    <div class="rentals__titulo__logo">
                        <h3 class="rentals__titulo">
                            rentingmanakia 
                        </h3>
                        <div class="rentals__logo">
                            <img  class="rentalIcono" src="http://imgfz.com/i/u3qdkED.png" alt="foto del icono del rental rentingmanakia">
                        </div>
                    </div>
                    <div class="rentals__description">
                        <ul>
                            <li>Ubicacion: cami des curat n9, soller (espana). 07100</li>
                            <li>Contacto: num(213245685) / email(rentingmanakia@contact.eu)</li>
                            <li>Redes sociales: instagram(@rentingmanakia) / twitter(@rentingmanakia)</li>
                            <li>Bicis disponibles: <a href='./bicissolitarias/bicissolitariaSO0201.html'>SO0201</a> </li>
                            <li>Bicis no disponibles: <a href='./bicissolitarias/bicissolitariaSO0202.html'>SO0202</a> </li>
                        </ul>
                    </div>
                    <div class="rentals__img__location">
                        <a href="#"><img class=fotoRental src="http://imgfz.com/i/NvZjUzc.jpeg" alt="foto de la ubicacion del rental rentingmanakia"></a>
                    </div>
                </div>
            </div>
            <div class="rentals">
                <div class="rentals__container">
                    <div class="rentals__titulo__logo">
                        <h3 class="rentals__titulo">
                            touristbike 
                        </h3>
                        <div class="rentals__logo">
                            <img  class="rentalIcono" src="http://imgfz.com/i/zPt1Yg6.png" alt="foto del icono del rental touristbike">
                        </div>
                    </div>
                    <div class="rentals__description">
                        <ul>
                            <li>Ubicacion: avinguda des capdella n10, calvia (espana). 07011</li>
                            <li>Contacto: num(987987987) / email(touristbike@contact.eu)</li>
                            <li>Redes sociales: instagram(@touristbike) / twitter(@touristbike)</li>
                            <li>Bicis disponibles: <a href='./bicissolitarias/bicissolitariaCA0101.html'>CA0101</a> </li>
                            <li>Bicis no disponibles: <a href='./bicissolitarias/bicissolitariaCA0102.html'>CA0102</a> </li>
                        </ul>
                    </div>
                    <div class="rentals__img__location">
                        <a href="#"><img class=fotoRental src="http://imgfz.com/i/PfOTSMF.jpeg" alt="foto de la ubicacion del rental touristbike"></a>
                    </div>
                </div>
            </div>
            <div class="rentals">
                <div class="rentals__container">
                    <div class="rentals__titulo__logo">
                        <h3 class="rentals__titulo">
                            rentalride 
                        </h3>
                        <div class="rentals__logo">
                            <img  class="rentalIcono" src="http://imgfz.com/i/I5K98Hz.png" alt="foto del icono del rental rentalride">
                        </div>
                    </div>
                    <div class="rentals__description">
                        <ul>
                            <li>Ubicacion: carrer serral n5, calvia (espana). 07013</li>
                            <li>Contacto: num(687875483) / email(rentalride@contact.eu)</li>
                            <li>Redes sociales: instagram(@rybrentalridem) / twitter(@rentalride)</li>
                            <li>Bicis disponibles: <a href='./bicissolitarias/bicissolitariaCA0201.html'>CA0201</a> </li>
                            <li>Bicis no disponibles: <a href='./bicissolitarias/bicissolitariaCA0202.html'>CA0202</a> </li>
                        </ul>
                    </div>
                    <div class="rentals__img__location">
                        <a href="#"><img class=fotoRental src="http://imgfz.com/i/Rg3dPDb.jpeg" alt="foto de la ubicacion del rental rentalride"></a>
                    </div>
                </div>
            </div>'''
    assert crearBodyRentals(listarRentals(respuestaText(conseguirRespuestaDatos(mongoKey(),mongoUrl())))) == body

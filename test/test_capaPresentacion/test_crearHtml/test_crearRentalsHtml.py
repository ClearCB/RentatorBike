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
        <section class="rental_lista">
            <h3 class="titleRental">Rentals disponibles</h3>
            <hr>
            <div class="rental_lista_div">
                <ul class="lista">
                
                        <li class="rental"><h3> bibike <br><br><br><img  class="rentalIcono" src="http://imgfz.com/i/x1Re2Mf.png" alt="foto del icono del rental bibike"></h3> 
                            <ul class="contenidoDeRental">
                                <li class="imparLista">Ubicacion: calle joan alcover n7  , 07006. palma, espana</li>
                                <li class="parLista">Contacto: num (678598234) email (bibike@contact.eu)</li>
                                <li class="imparLista">Instagram:@bibike /  Twitter: @bibike</li>
                                <li class="parLista">Bicis disponibles:['PA0101']</li>
                                <li class="imparLista">Bicis no disponibles:['PA0102']</li>
                            </ul>
                            <a href="#"><img class=fotoRental src="http://imgfz.com/i/2sS6E8d.jpeg" alt="foto de la ubicacion del rental bibike"></a>
                        </li>
                        <li class="rental"><h3> rentbima <br><br><br><img  class="rentalIcono" src="http://imgfz.com/i/pUvx325.png" alt="foto del icono del rental rentbima"></h3> 
                            <ul class="contenidoDeRental">
                                <li class="imparLista">Ubicacion: calle plaza de espana, 07005. palma, espana</li>
                                <li class="parLista">Contacto: num (738912213) email (rentbima@contact.eu)</li>
                                <li class="imparLista">Instagram:@rentbima /  Twitter: @rentbima</li>
                                <li class="parLista">Bicis disponibles:['PA0201']</li>
                                <li class="imparLista">Bicis no disponibles:['PA0202']</li>
                            </ul>
                            <a href="#"><img class=fotoRental src="http://imgfz.com/i/YlsSQVf.jpeg" alt="foto de la ubicacion del rental rentbima"></a>
                        </li>
                        <li class="rental"><h3> habikemall <br><br><br><img  class="rentalIcono" src="http://imgfz.com/i/UkQEme7.png" alt="foto del icono del rental habikemall"></h3> 
                            <ul class="contenidoDeRental">
                                <li class="imparLista">Ubicacion: calle sant joan n2, 07500. manacor, espana</li>
                                <li class="parLista">Contacto: num (678523945) email (habikemall@contact.eu)</li>
                                <li class="imparLista">Instagram:@habikemall /  Twitter: @habikemall</li>
                                <li class="parLista">Bicis disponibles:['MA0101']</li>
                                <li class="imparLista">Bicis no disponibles:['MA0102']</li>
                            </ul>
                            <a href="#"><img class=fotoRental src="http://imgfz.com/i/Iw2GXTb.jpeg" alt="foto de la ubicacion del rental habikemall"></a>
                        </li>
                        <li class="rental"><h3> rybm <br><br><br><img  class="rentalIcono" src="http://imgfz.com/i/eKAiq7R.png" alt="foto del icono del rental rybm"></h3> 
                            <ul class="contenidoDeRental">
                                <li class="imparLista">Ubicacion: calle carrer des sol n10, 07500. manacor, espana</li>
                                <li class="parLista">Contacto: num (666554223) email (rybm@contact.eu)</li>
                                <li class="imparLista">Instagram:@rybm /  Twitter: @rybm</li>
                                <li class="parLista">Bicis disponibles:['MA0201']</li>
                                <li class="imparLista">Bicis no disponibles:['MA0202']</li>
                            </ul>
                            <a href="#"><img class=fotoRental src="http://imgfz.com/i/duK0xBn.jpeg" alt="foto de la ubicacion del rental rybm"></a>
                        </li>
                        <li class="rental"><h3> bikeandgo <br><br><br><img  class="rentalIcono" src="http://imgfz.com/i/kfOGrD5.png" alt="foto del icono del rental bikeandgo"></h3> 
                            <ul class="contenidoDeRental">
                                <li class="imparLista">Ubicacion: calle carrer de la creu n7, 07400. alcudia, espana</li>
                                <li class="parLista">Contacto: num (897524645) email (bikeandgo@contact.eu)</li>
                                <li class="imparLista">Instagram:@bikeandgo /  Twitter: @bikeandgo</li>
                                <li class="parLista">Bicis disponibles:['AL0101']</li>
                                <li class="imparLista">Bicis no disponibles:['AL0102']</li>
                            </ul>
                            <a href="#"><img class=fotoRental src="http://imgfz.com/i/vWtjfA5.jpeg" alt="foto de la ubicacion del rental bikeandgo"></a>
                        </li>
                        <li class="rental"><h3> speedyrent <br><br><br><img  class="rentalIcono" src="http://imgfz.com/i/S5up7Iy.png" alt="foto del icono del rental speedyrent"></h3> 
                            <ul class="contenidoDeRental">
                                <li class="imparLista">Ubicacion: calle carrer de menorca n3, 07400. alcudia, espana</li>
                                <li class="parLista">Contacto: num (689496982) email (speedyrent@contact.eu)</li>
                                <li class="imparLista">Instagram:@speedyrent /  Twitter: @speedyrent</li>
                                <li class="parLista">Bicis disponibles:['AL0201']</li>
                                <li class="imparLista">Bicis no disponibles:['AL0202']</li>
                            </ul>
                            <a href="#"><img class=fotoRental src="http://imgfz.com/i/brfKjYW.jpeg" alt="foto de la ubicacion del rental speedyrent"></a>
                        </li>
                        <li class="rental"><h3> energylegs <br><br><br><img  class="rentalIcono" src="http://imgfz.com/i/8pomsKj.png" alt="foto del icono del rental energylegs"></h3> 
                            <ul class="contenidoDeRental">
                                <li class="imparLista">Ubicacion: calle av de asturias n10, 07100. soller, espana</li>
                                <li class="parLista">Contacto: num (987166998) email (energylegs@contact.eu)</li>
                                <li class="imparLista">Instagram:@energylegs /  Twitter: @energylegs</li>
                                <li class="parLista">Bicis disponibles:['SO0101']</li>
                                <li class="imparLista">Bicis no disponibles:['SO0102']</li>
                            </ul>
                            <a href="#"><img class=fotoRental src="http://imgfz.com/i/AZr2KHT.jpeg" alt="foto de la ubicacion del rental energylegs"></a>
                        </li>
                        <li class="rental"><h3> rentingmanakia <br><br><br><img  class="rentalIcono" src="http://imgfz.com/i/u3qdkED.png" alt="foto del icono del rental rentingmanakia"></h3> 
                            <ul class="contenidoDeRental">
                                <li class="imparLista">Ubicacion: calle cami des curat n9, 07100. soller, espana</li>
                                <li class="parLista">Contacto: num (213245685) email (rentingmanakia@contact.eu)</li>
                                <li class="imparLista">Instagram:@rentingmanakia /  Twitter: @rentingmanakia</li>
                                <li class="parLista">Bicis disponibles:['SO0201']</li>
                                <li class="imparLista">Bicis no disponibles:['SO0202']</li>
                            </ul>
                            <a href="#"><img class=fotoRental src="http://imgfz.com/i/NvZjUzc.jpeg" alt="foto de la ubicacion del rental rentingmanakia"></a>
                        </li>
                        <li class="rental"><h3> touristbike <br><br><br><img  class="rentalIcono" src="http://imgfz.com/i/zPt1Yg6.png" alt="foto del icono del rental touristbike"></h3> 
                            <ul class="contenidoDeRental">
                                <li class="imparLista">Ubicacion: calle avinguda des capdella n10, 07011. calvia, espana</li>
                                <li class="parLista">Contacto: num (987987987) email (touristbike@contact.eu)</li>
                                <li class="imparLista">Instagram:@touristbike /  Twitter: @touristbike</li>
                                <li class="parLista">Bicis disponibles:['CA0101']</li>
                                <li class="imparLista">Bicis no disponibles:['CA0102']</li>
                            </ul>
                            <a href="#"><img class=fotoRental src="http://imgfz.com/i/PfOTSMF.jpeg" alt="foto de la ubicacion del rental touristbike"></a>
                        </li>
                        <li class="rental"><h3> rentalride <br><br><br><img  class="rentalIcono" src="http://imgfz.com/i/I5K98Hz.png" alt="foto del icono del rental rentalride"></h3> 
                            <ul class="contenidoDeRental">
                                <li class="imparLista">Ubicacion: calle carrer serral n5, 07013. calvia, espana</li>
                                <li class="parLista">Contacto: num (687875483) email (rentalride@contact.eu)</li>
                                <li class="imparLista">Instagram:@rybrentalridem /  Twitter: @rentalride</li>
                                <li class="parLista">Bicis disponibles:['CA0201']</li>
                                <li class="imparLista">Bicis no disponibles:['CA0202']</li>
                            </ul>
                            <a href="#"><img class=fotoRental src="http://imgfz.com/i/Rg3dPDb.jpeg" alt="foto de la ubicacion del rental rentalride"></a>
                        </li>
                </ul>
            </div>
        </section>'''
    assert crearBodyRentals(listarRentals(respuestaText(conseguirRespuestaDatos(mongoKey(),mongoUrl())))) == body

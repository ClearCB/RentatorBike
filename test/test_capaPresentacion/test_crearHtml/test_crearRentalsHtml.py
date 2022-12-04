from src.capaPresentacion.crearHtml.crearRentalsHtml import crearBodyRentals, rentalsHtml
import pytest
import os

@pytest.mark.test_crearBodyRentals
def test_crearBodyRentals():

    body ='''
        <section class="rental_lista">
            <h3 class="titleRental">Rentals disponibles</h3>
            <hr>
            <div class="rental_lista_div">
                <ul class="lista">
                    <li class="rental"><h3> {nombreRental} <br><br><br><img  class="rentalIcono" src="{iconoRental}" alt="foto del icono del rental {nombreRental}"></h3> 
                        <ul class="contenidoDeRental">
                            <li class="imparLista">Ubicacion: {direccion}</li>
                            <li class="parLista">Contacto:{contacto}</li>
                            <li class="imparLista">Redes sociales:{redes}</li>
                            <li class="parLista">Bicis disponibles:{bicisdisponibles}</li>
                            <li class="imparLista">Bicis no disponibles:{bicisdisponibles}</li>
                        </ul>
                        <a href="#"><img class=fotoRental src="{fotoRental}" alt="foto de la ubicacion del rental {nombreRental}"></a>
                    </li>
                </ul>
            </div>
        </section>'''

    assert crearBodyRentals() == body

@pytest.mark.test_crearRentalsHtml
def test_crearRentalsHtml():

    rentalsHtml()
    assert os.path.isfile("C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\second_pages\\rentals.html") == True

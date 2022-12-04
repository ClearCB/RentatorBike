from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHeader, crearHtmlHead, crearFooter

def crearBodyRentals():

    rentalsBodyHtml ='''
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
    return rentalsBodyHtml

def rentalsHtml():

    head = crearHtmlHead("Rentals cercanos", "Página donde aparecen todos los rental de bikes cercanos", "bicicletas, alquilar, rental, bike, ubicacion, contacto, redes, sociales","../cssStyles/","rentals")
    header = crearHeader("","../")
    body = crearBodyRentals()
    footer = crearFooter()

    try:
        with open("C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\second_pages\\rentals.html","w", encoding="utf-8") as archivo:
            archivo.write(head)

    except FileNotFoundError:
        print("El directorio no existe, ejecuta correctamente el programa y vuelve a intentarlo.")

    else:
        with open("C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\second_pages\\rentals.html","a", encoding="utf-8") as archivo:
            archivo.write(header)
            archivo.write(body)
            archivo.write(footer)
            print("El archivo 'rentals.html' creado correctamente.")
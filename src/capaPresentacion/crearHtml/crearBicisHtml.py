from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHeader, crearHtmlHead, crearFooter

def crearBodyBicis():

    bicisBodyHtml ='''
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
    return bicisBodyHtml

def bicisHtml():

    head = crearHtmlHead("Bicis disponibles", "Página donde aparecen todas las bicicletas disponibles", "bicicletas, disponible, up, down alquilar, rental, bike","../cssStyles/","bicis")
    header = crearHeader("","../")
    body = crearBodyBicis()
    footer = crearFooter()

    try:
        with open("C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\second_pages\\bicis.html","w", encoding="utf-8") as archivo:
            archivo.write(head)

    except FileNotFoundError:
        print("El directorio no existe, ejecuta correctamente el programa y vuelve a intentarlo.")

    else:
        with open("C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\second_pages\\bicis.html","a", encoding="utf-8") as archivo:
            archivo.write(header)
            archivo.write(body)
            archivo.write(footer)
            print("El archivo 'bicis.html' creado correctamente.")
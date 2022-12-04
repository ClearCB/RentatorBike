from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHeader, crearHtmlHead, crearFooter

def crearBodyMarcas():

    marcasBodyHtml ='''
        <section>
            <h3 class="titleBike">Marcas de bicicletas</h3>
            <hr>
            <div id="container">
                <a href="bicispormarca.html#cube"><div class="box"> Cube</div></a>
                <a href="bicispormarca.html#specialized"><div class="box"> Specialized</div></a>
                <a href="bicispormarca.html#giant"><div class="box"> Giant</div></a>
                <a href="bicispormarca.html#cannondale"><div class="box"> Cannondale</div></a>
            </div>
        </section>'''
    return marcasBodyHtml

def marcasHtml():

    head = crearHtmlHead("Marcas disponibles", "Página donde aparecen un link a todas las marcas disponibles", "cube, specialized, giant, cannondale, marca, brand, alquilar, rental, bike","../cssStyles/","marcas")
    header = crearHeader("","../")
    body = crearBodyMarcas()
    footer = crearFooter()

    try:
        with open("C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\second_pages\\marcas.html","w", encoding="utf-8") as archivo:
            archivo.write(head)

    except FileNotFoundError:
        print("El directorio no existe, ejecuta correctamente el programa y vuelve a intentarlo.")

    else:
        with open("C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\second_pages\\marcas.html","a", encoding="utf-8") as archivo:
            archivo.write(header)
            archivo.write(body)
            archivo.write(footer)
            print("El archivo 'marcas.html' creado correctamente.")
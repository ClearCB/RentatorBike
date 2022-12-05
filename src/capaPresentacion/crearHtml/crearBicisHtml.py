from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHeader, crearHtmlHead, crearFooter
from src.capaPresentacion.crearCss.crearSecundarioCss import crearBicisCss

def crearBodyBicis(listaBicis):

    bicisBodyHtml ='''
        <h3 class="titleBicis"> Bicis disponibles </h3>
        <hr>
        <section>
            <div id="contenedorPadre">
                '''
    for bici in listaBicis:

        tipo = bici["type"]
        estado = bici["state"]
        groupset = bici["techinfo"]["groupset"]
        talla = bici["techinfo"]["size"]
        ruedas = bici["techinfo"]["wheels"]
        precio = bici["prize_euros_days"]
        complementos = bici["complements"]
        imagenBici = bici["img"]
        marca = bici["techinfo"]["brand"]
        strComplementos = ""
        for complemento in complementos:
            strComplementos += (complemento+" ")
        rental = bici["where"][0]["company_name"]

        bicisBodyHtml+=f'''
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitaria{bici["_idbike"]}.html"><img src="{imagenBici}" alt="bicicleta de la marca {marca} y tipo {tipo}"></a>
                    </div>
                    <div class="contenedor_info">
                        <h5>{tipo}</h5>
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: {estado}</li> 
                                <li>Marca: {marca}</li> 
                                <li>Groupset: {groupset}</li> 
                                <li>Talla: {talla}</li> 
                                <li>Tamaño de ruedas: {ruedas}</li> 
                                <li>Precio por dia: {precio}</li> 
                                <li>Complementos disponibles: {strComplementos}</li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en {rental}</p>
                        </div>
                    </div>
                </div>'''
    bicisBodyHtml+='''
            </div>
        </section>'''
            

    return bicisBodyHtml

def bicisHtml(listaBicis):

    crearBicisCss()
    
    head = crearHtmlHead("Bicis disponibles", "Página donde aparecen todas las bicicletas disponibles", "bicicletas, disponible, up, down alquilar, rental, bike","../cssStyles/","bicis")
    header = crearHeader("","../")
    body = crearBodyBicis(listaBicis)
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
from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHeader, crearHtmlHead, crearFooter
from src.capaNegocio.crearArchivos import crearArchivo

# En este módulo vamos a crear funciones que van a crear un archivo "bicipormarca.html"

# Definimos una función que nos comprueba si la bici cumple la condicion para ser añadida en el body o no.
def esFiltro(bici,marcaBici):

    # Comprobamos que la bici cumple la condicion
    if marcaBici == bici["techinfo"]["brand"]:

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

        # Generamos la nueva bici que va a ser añadida al body
        nuevaBici = f'''
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitaria{bici["_idbike"]}.html"><img src="{imagenBici}" alt="bicicleta de la marca {marca} y tipo {tipo}"></a>
                    </div>
                    <div class="contenedor_info">
                        <div class="infoBike">
                            <ul> 
                                <li><b>Estado</b>: {estado}</li> 
                                <li><b>Marca</b>: {marca}</li> 
                                <li><b>Groupset</b>: {groupset}</li> 
                                <li><b>Talla</b>: {talla}</li> 
                                <li><b>Tamaño de ruedas</b>: {ruedas}</li> 
                                <li><b>Precio por dia</b>: {precio}</li> 
                                <li><b>Complementos disponibles</b>: {strComplementos}</li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en {rental}</p>
                        </div>
                    </div>
                </div>'''

        return nuevaBici

    else: # En el caso de que no cumpla la condición no ocurrirá nada.
        pass


# Función que devuelve el valor del body del bicipormarca.html
def crearBodyBiciMarca(listaBicis):

    # Añadimos la parte superior del body de bicipormarca.html
    bodyBiciMarcas ='''
        <h3 class="titleBicis"> Bicis por marca </h3><hr>
        <section>
            <div id="contenedorPadre">
                <h4 class="filtrotitulo" id="cube"> Cube </h4>'''

    # Recorremos la lista de las bicis
    for bici in listaBicis:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciMarcas += esFiltro(bici, "cube")
        except TypeError:
            pass

    # Añadimos la siguiente marca
    bodyBiciMarcas +='''
                <h4 class="filtrotitulo" id="specialized"> Specialized</h4>'''

    # Recorremos la lista de las bicis
    for bici in listaBicis:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciMarcas += esFiltro(bici, "specialized")
        except TypeError:
            pass

    # Añadimos la siguiente marca
    bodyBiciMarcas +='''
                <h4 class="filtrotitulo" id="giant"> Giant</h4>'''

    # Recorremos la lista de las bicis
    for bici in listaBicis:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciMarcas += esFiltro(bici, "giant")
        except TypeError:
            pass

    # Añadimos la siguiente marca
    bodyBiciMarcas +='''
                <h4 class="filtrotitulo" id="cannondale"> Cannondale</h4>'''

    # Recorremos la lista de las bicis
    for bici in listaBicis:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciMarcas += esFiltro(bici, "cannondale")
        except TypeError:
            pass

    # Añadimos la parte final del body
    bodyBiciMarcas += '''
            </div>
        </section>'''

    return bodyBiciMarcas

# Función que construye el bicipormarca.html y lo devuelve en una variable
def biciMarcaHtml(listaBicis):
  

    biciMarca = ''''''
    # Añadimos cada parte del código independientemente 
    biciMarca += crearHtmlHead("Bicis por marca", "Página donde aparecen todas las bicicletas filtradas por su marca", "bicicletas, marcas, specialized, cannondale, giant, cube, alquilar, rental, bike","../cssStyles/","bicisfiltro")
    biciMarca += crearHeader("../","")
    biciMarca += crearBodyBiciMarca(listaBicis)
    biciMarca += crearFooter()

    return biciMarca # Devolvemos la variable biciMarcas que contiene el código del archivo bicipormarca.html

# Definimos una función que ejecuta la función necesaria para crear el archivo correctamente.
def crearBiciMarcaHtml(listaBicis):

    crearArchivo(biciMarcaHtml(listaBicis),".\\docs\\second_pages","bicispormarca","html")

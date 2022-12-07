from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHeader, crearHtmlHead, crearFooter
from src.capaNegocio.crearArchivos import crearArchivo

# En este módulo vamos a crear funciones que van a crear un archivo "bicicaracteristica.html"

# Definimos una función que nos comprueba si la bici cumple la condicion para ser añadida en el body o no.
def esFiltro(bici, caracteristicaBici, caracteristicaObj):

    # Comprobamos que la bici cumple la condicion
    if caracteristicaBici == bici["techinfo"][f"{caracteristicaObj}"]:

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

        return nuevaBici

    else: # En el caso de que no cumpla la condición no ocurrirá nada.
        pass

# Función que devuelve el valor del body del bicicaracteristica.html
def crearBodyBiciCaracteristica(listaBicis):

    # Añadimos la parte superior del body de bicicaracteristica.html
    bodyBiciCaracteristica ='''
        <section>
            <h3 class="titleBicis"> Bicis por caracteristica </h3>
            <div class="categorias">
                <a href="#cuadro" target="_self"><div class="nombrecategorias"><h4>Por tamaño del cuadro</h4></div></a>
                <a href="#rueda" target="_self"><div class="nombrecategorias"><h4>Por tamaño de las ruedas</h4></div></a>
                <a href="#groupset" target="_self"><div class="nombrecategorias"><h4>Por marca del groupset</h4></div></a>
            </div><hr>
            <div id="contenedorPadre">
                    <h4 class="filtrotitulo"><span id="cuadro"></span>Tamaño del cuadro </h4>
                    <h5 class="filtrocaract"> Talla XS</h5>'''

    # Recorremos la lista de las bicis
    for bici in listaBicis:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciCaracteristica += esFiltro(bici, "xs", "size")
        except TypeError:
            pass

    # Añadimos la siguiente Caracteristica
    bodyBiciCaracteristica +='''
                <h5 class="filtrocaract"> Talla S</h5>'''

    # Recorremos la lista de las bicis
    for bici in listaBicis:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciCaracteristica += esFiltro(bici, "s", "size")
        except TypeError:
            pass

    # Añadimos la siguiente Caracteristica
    bodyBiciCaracteristica +='''
                <h5 class="filtrocaract"> Talla M</h5>'''

    # Recorremos la lista de las bicis
    for bici in listaBicis:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciCaracteristica += esFiltro(bici, "m", "size")
        except TypeError:
            pass

    # Añadimos la siguiente Caracteristica
    bodyBiciCaracteristica +='''
                <h5 class="filtrocaract"> Talla L</h5>'''

    # Recorremos la lista de las bicis
    for bici in listaBicis:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciCaracteristica += esFiltro(bici, "l", "size")
        except TypeError:
            pass

    # Añadimos la siguiente Caracteristica
    bodyBiciCaracteristica +='''
                <h5 class="filtrocaract"> Talla XL</h5>'''

    # Recorremos la lista de las bicis
    for bici in listaBicis:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciCaracteristica += esFiltro(bici, "xl", "size")
        except TypeError:
            pass

    # Añadimos la siguiente Caracteristica
    bodyBiciCaracteristica +='''
                <h4 class="filtrotitulo"> <span id="rueda"></span> Tamaño de la rueda </h4>
                <h5 class="filtrocaract"> Talla 26'</h5>'''

    # Recorremos la lista de las bicis
    for bici in listaBicis:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciCaracteristica += esFiltro(bici, "26", "wheels")
        except TypeError:
            pass
    
    # Añadimos la siguiente Caracteristica
    bodyBiciCaracteristica +='''
                <h5 class="filtrocaract"> Talla 27'</h5>'''

    # Recorremos la lista de las bicis
    for bici in listaBicis:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciCaracteristica += esFiltro(bici, "27", "wheels")
        except TypeError:
            pass

    # Añadimos la siguiente Caracteristica
    bodyBiciCaracteristica +='''
                <h5 class="filtrocaract"> Talla 29'</h5>'''

    # Recorremos la lista de las bicis
    for bici in listaBicis:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciCaracteristica += esFiltro(bici, "29", "wheels")
        except TypeError:
            pass

    # Añadimos la siguiente Caracteristica
    bodyBiciCaracteristica +='''
                <h4 class="filtrotitulo"> <span id="groupset"></span>Marca del groupset </h4>
                <h5 class="filtrocaract"> Kask</h5>'''

    # Recorremos la lista de las bicis
    for bici in listaBicis:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciCaracteristica += esFiltro(bici, "Kask", "groupset")
        except TypeError:
            pass

    # Añadimos la siguiente Caracteristica
    bodyBiciCaracteristica +='''
                <h5 class="filtrocaract"> Specialized </h5>'''

    # Recorremos la lista de las bicis
    for bici in listaBicis:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciCaracteristica += esFiltro(bici, "specialized", "groupset")
        except TypeError:
            pass

    # Añadimos la siguiente Caracteristica
    bodyBiciCaracteristica +='''
                <h5 class="filtrocaract"> Kona</h5>'''

    # Recorremos la lista de las bicis
    for bici in listaBicis:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciCaracteristica += esFiltro(bici, "kona", "groupset")
        except TypeError:
            pass

    # Añadimos la siguiente Caracteristica
    bodyBiciCaracteristica +='''
                <h5 class="filtrocaract">Orbea</h5>'''

    # Recorremos la lista de las bicis
    for bici in listaBicis:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciCaracteristica += esFiltro(bici, "orbea", "groupset")
        except TypeError:
            pass

    # Añadimos la parte final del body
    bodyBiciCaracteristica += '''
            </div>
        </section>'''

    return bodyBiciCaracteristica

# Función que construye el bicicaracteristica.html y lo devuelve en una variable
def biciCaracteristicaHtml(listaBicis):
  

    biciCaracteristica = ''''''
    # Añadimos cada parte del código independientemente 
    biciCaracteristica += crearHtmlHead("Bicicletas por caracteristica", "Página donde aparecen las bicicletas filtradas por sus caracteristica", "bicicletas, cuadro, talla, ruedas, tamaño, groupset","../cssStyles/","bicisfiltro")
    biciCaracteristica += crearHeader("../","")
    biciCaracteristica += crearBodyBiciCaracteristica(listaBicis)
    biciCaracteristica += crearFooter()

    return biciCaracteristica # Devolvemos la variable biciCaracteristica que contiene el código del archivo bicicaracteristica.html

# Definimos una función que ejecuta la función necesaria para crear el archivo correctamente.
def crearBiciCaracteristicaHtml(listaBicis):

    crearArchivo(biciCaracteristicaHtml(listaBicis),".\\docs\\second_pages","biciscaracteristica","html")

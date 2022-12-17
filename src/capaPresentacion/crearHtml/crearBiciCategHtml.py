from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHeader, crearHtmlHead
from src.capaPresentacion.variables.variablesHtml import footerBase
from src.capaNegocio.crearArchivos import crearArchivo

# En este módulo vamos a crear funciones que van a crear un archivo "bicicategoria.html"

# Definimos una función que nos comprueba si la bici cumple la condicion para ser añadida en el body o no.
def esFiltro(bici,categoriaBici):

    # Comprobamos que la bici cumple la condicion
    if categoriaBici == bici["type"]:

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


# Función que devuelve el valor del body del bicicategoria.html
def crearBodyBiciCategoria(listaBicis):

    # Añadimos la parte superior del body de bicicategoria.html
    bodyBiciCategoria ='''
        <h3 class="titleBicis"> Bicis por categoria </h3>
        <section><hr>
            <div id="contenedorPadre">
                <h4 class="filtrotitulo" id="mtb"> MTB</h4>'''

    # Recorremos la lista de las bicis
    for bici in listaBicis:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciCategoria += esFiltro(bici, "mtb")
        except TypeError:
            pass

    # Añadimos la siguiente Categoria
    bodyBiciCategoria +='''
                <h4 class="filtrotitulo" id="emtb"> e-MTB</h4>'''

    # Recorremos la lista de las bicis
    for bici in listaBicis:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciCategoria += esFiltro(bici, "e-mtb")
        except TypeError:
            pass

    # Añadimos la siguiente Categoria
    bodyBiciCategoria +='''
                <h4 class="filtrotitulo" id="carretera"> Carretera</h4>'''

    # Recorremos la lista de las bicis
    for bici in listaBicis:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciCategoria += esFiltro(bici, "bici de carretera")
        except TypeError:
            pass

    # Añadimos la siguiente Categoria
    bodyBiciCategoria +='''
                <h4 class="filtrotitulo" id="ecarretera"> Carretera eléctrica</h4>'''

    # Recorremos la lista de las bicis
    for bici in listaBicis:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciCategoria += esFiltro(bici, "bici de carretera electrica")
        except TypeError:
            pass

    bodyBiciCategoria +='''
                <h4 class="filtrotitulo" id="ciudad"> Bici de ciudad</h4>'''

    # Recorremos la lista de las bicis
    for bici in listaBicis:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciCategoria += esFiltro(bici, "bici de ciudad")
        except TypeError:
            pass

    bodyBiciCategoria +='''
                <h4 class="filtrotitulo" id="eciudad"> Bici de ciudad eléctrica</h4>'''

    # Recorremos la lista de las bicis
    for bici in listaBicis:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciCategoria += esFiltro(bici, "bici de ciudad electrica")
        except TypeError:
            pass

    # Añadimos la parte final del body
    bodyBiciCategoria += '''
            </div>
        </section>'''

    return bodyBiciCategoria

# Función que construye el bicicategoria.html y lo devuelve en una variable
def biciCategoriaHtml(listaBicis):
  

    biciCategoria = ''''''
    # Añadimos cada parte del código independientemente 
    biciCategoria += crearHtmlHead("Bicicletas por categoría", "Página donde aparecen las bicicletas filtradas por su categoria", "bicicletas, tipos, mtb, carretera, electrica, ciudad, alquilar, rental, bike","../cssStyles/","bicisfiltro")
    biciCategoria += crearHeader("../","")
    biciCategoria += crearBodyBiciCategoria(listaBicis)
    biciCategoria += footerBase

    return biciCategoria # Devolvemos la variable biciCategoria que contiene el código del archivo bicicategoria.html

# Definimos una función que ejecuta la función necesaria para crear el archivo correctamente.
def crearBiciCategoriaHtml(listaBicis):

    crearArchivo(biciCategoriaHtml(listaBicis),".\\docs\\second_pages","biciscategoria","html")

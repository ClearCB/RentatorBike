from src.capaDatos.listarDatosMongo import listarBicis, listarRentals, respuestaText
from src.capaDatos.peticionMongo import respuestaMongo
from src.capaPresentacion.crearHtml.funcionHtmlBase import crearContenedorRental, crearContenedorBici, esFiltro
# En este modulo vamos a poner todos los "body" de las funciones que
# creen un body

respuesta = respuestaText(respuestaMongo()) 
listaBicis = listarBicis(respuesta)
listaRentals = listarRentals(respuesta)

# Función que construye el body del rentals.html
def crearBodyRentals(lista):

    # Definimos parte del body de rentals
    bodyRentals = '''
        <h3 class="titleBicis"> Bicis disponibles </h3>
        <hr>
        <section>
            <div id="contenedorPadre">'''

    # Recorremos la lista de los rentals para determinar los valores que queremos en el contenedor
    for rental in lista:

        bodyRentals+=crearContenedorRental(rental)

    bodyRentals +='''
            </div>
        </section>'''

    return bodyRentals

# Devuelve una variable con el html del body de rentals.html
def bodyRentals():

    return crearBodyRentals(listaRentals)

# Creamos una función que devuelva el valor del body del bicis.html
def crearBodyBicis(lista):

    # Definimos parte del body html
    bicisBodyHtml ='''
        <h3 class="titleBicis"> Bicis disponibles </h3>
        <hr>
        <section>
            <div id="contenedorPadre">'''
    
    for bici in lista: # Recorremos la lista de las bicis para conseguir los valores que queremos

        bicisBodyHtml += crearContenedorBici(bici)
    
    bicisBodyHtml+='''
            </div>
        </section>'''

    return bicisBodyHtml

# Devuelve una variable con el html del body de bicis.html
def bodyBicis():

    return crearBodyBicis(listaBicis)

# Creamos una funcion que nos creará el body de la pagina bicicaract.html
def crearBodyCaracteristica(lista):

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
    
    for bici in lista:

        try:
            bodyBiciCaracteristica += esFiltro(bici, "caracteristicaMarco", "xs")
        except TypeError:
            pass

    bodyBiciCaracteristica +='''
                <h5 class="filtrocaract"> Talla S</h5>'''

    for bici in lista:

        try:
            bodyBiciCaracteristica += esFiltro(bici, "caracteristicaMarco", "s")
        except TypeError:
            pass

    bodyBiciCaracteristica +='''
                <h5 class="filtrocaract"> Talla M</h5>'''

    for bici in lista:

        try:
            bodyBiciCaracteristica += esFiltro(bici, "caracteristicaMarco", "m")
        except TypeError:
            pass

    bodyBiciCaracteristica +='''
                <h5 class="filtrocaract"> Talla L</h5>'''

    for bici in lista:

        try:
            bodyBiciCaracteristica += esFiltro(bici, "caracteristicaMarco", "l")
        except TypeError:
            pass

    bodyBiciCaracteristica +='''
                <h5 class="filtrocaract"> Talla XL</h5>'''

    for bici in lista:

        try:
            bodyBiciCaracteristica += esFiltro(bici, "caracteristicaMarco", "xl")
        except TypeError:
            pass

    bodyBiciCaracteristica +='''
                <h4 class="filtrotitulo"> <span id="rueda"></span> Tamaño de la rueda </h4>
                <h5 class="filtrocaract"> Talla 26'</h5>'''
    
    for bici in lista:

        try:
            bodyBiciCaracteristica += esFiltro(bici, "caracteristicaRueda", "26")
        except TypeError:
            pass

    bodyBiciCaracteristica +='''
                <h5 class="filtrocaract"> Talla 27'</h5>'''


    for bici in listaBicis:
        
        try:
            bodyBiciCaracteristica += esFiltro(bici,  "caracteristicaRueda", "27")
        except TypeError:
            pass

    bodyBiciCaracteristica +='''
                <h5 class="filtrocaract"> Talla 29'</h5>'''


    for bici in listaBicis:
        
        try:
            bodyBiciCaracteristica += esFiltro(bici,  "caracteristicaRueda", "29")
        except TypeError:
            pass

    bodyBiciCaracteristica +='''
                <h4 class="filtrotitulo"> <span id="groupset"></span>Marca del groupset </h4>
                <h5 class="filtrocaract"> Kask</h5>'''
    

    for bici in listaBicis:
        
        try:
            bodyBiciCaracteristica += esFiltro(bici,  "caracteristicaGroup", "kask")
        except TypeError:
            pass

    bodyBiciCaracteristica +='''
                <h5 class="filtrocaract"> Specialized </h5>'''
    

    for bici in listaBicis:
        
        try:
            bodyBiciCaracteristica += esFiltro(bici,  "caracteristicaGroup", "specialized")
        except TypeError:
            pass

    bodyBiciCaracteristica +='''
                <h5 class="filtrocaract"> Kona </h5>'''
    

    for bici in listaBicis:
        
        try:
            bodyBiciCaracteristica += esFiltro(bici,  "caracteristicaGroup", "kona")
        except TypeError:
            pass

    bodyBiciCaracteristica +='''
                <h5 class="filtrocaract"> Orbea </h5>'''
    

    for bici in listaBicis:
        
        try:
            bodyBiciCaracteristica += esFiltro(bici,  "caracteristicaGroup", "orbea")
        except TypeError:
            pass

    bodyBiciCaracteristica += '''
            </div>
        </section>'''

    return bodyBiciCaracteristica

# Devuelve una variable con el html del body de bicicaract.html
def bodyCaractirsticaHtml():

    return crearBodyCaracteristica(listaBicis)

# Creamos una funcion que nos creará el body de la pagina bicicateg.html
def crearBodyCategoria(lista):

    # Añadimos la parte superior del body de bicicategoria.html
    bodyBiciCategoria ='''
        <h3 class="titleBicis"> Bicis por categoria </h3>
        <section><hr>
            <div id="contenedorPadre">
                <h4 class="filtrotitulo" id="mtb"> MTB</h4>'''

    # Recorremos la lista de las bicis
    for bici in lista:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciCategoria += esFiltro(bici,"categoria" ,"mtb")
        except TypeError:
            pass

    # Añadimos la siguiente Categoria
    bodyBiciCategoria +='''
                <h4 class="filtrotitulo" id="emtb"> e-MTB</h4>'''

    # Recorremos la lista de las bicis
    for bici in lista:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciCategoria += esFiltro(bici,"categoria" , "e-mtb")
        except TypeError:
            pass

    # Añadimos la siguiente Categoria
    bodyBiciCategoria +='''
                <h4 class="filtrotitulo" id="carretera"> Carretera</h4>'''

    # Recorremos la lista de las bicis
    for bici in lista:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciCategoria += esFiltro(bici,"categoria" , "bici de carretera")
        except TypeError:
            pass

    # Añadimos la siguiente Categoria
    bodyBiciCategoria +='''
                <h4 class="filtrotitulo" id="ecarretera"> Carretera eléctrica</h4>'''

    # Recorremos la lista de las bicis
    for bici in lista:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciCategoria += esFiltro(bici,"categoria" , "bici de carretera electrica")
        except TypeError:
            pass

    bodyBiciCategoria +='''
                <h4 class="filtrotitulo" id="ciudad"> Bici de ciudad</h4>'''

    # Recorremos la lista de las bicis
    for bici in lista:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciCategoria += esFiltro(bici,"categoria" , "bici de ciudad")
        except TypeError:
            pass

    bodyBiciCategoria +='''
                <h4 class="filtrotitulo" id="eciudad"> Bici de ciudad eléctrica</h4>'''

    # Recorremos la lista de las bicis
    for bici in lista:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciCategoria += esFiltro(bici,"categoria" , "bici de ciudad electrica")
        except TypeError:
            pass

    # Añadimos la parte final del body
    bodyBiciCategoria += '''
            </div>
        </section>'''

    return bodyBiciCategoria

# Devuelve una variable con el html del body de bicicateg.html
def bodyCategoriaHtml():

    return crearBodyCategoria(listaBicis)

# Creamos una funcion que nos creará el body de la pagina bicipormarca.html
def crearBodyMarca(lista):

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
            bodyBiciMarcas += esFiltro(bici,"marca" , "cube")
        except TypeError:
            pass

    # Añadimos la siguiente marca
    bodyBiciMarcas +='''
                <h4 class="filtrotitulo" id="specialized"> Specialized</h4>'''

    # Recorremos la lista de las bicis
    for bici in listaBicis:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciMarcas += esFiltro(bici,"marca" , "specialized")
        except TypeError:
            pass

    # Añadimos la siguiente marca
    bodyBiciMarcas +='''
                <h4 class="filtrotitulo" id="giant"> Giant</h4>'''

    # Recorremos la lista de las bicis
    for bici in listaBicis:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciMarcas += esFiltro(bici,"marca" , "giant")
        except TypeError:
            pass

    # Añadimos la siguiente marca
    bodyBiciMarcas +='''
                <h4 class="filtrotitulo" id="cannondale"> Cannondale</h4>'''

    # Recorremos la lista de las bicis
    for bici in listaBicis:
        
        # Comprobamos que cunple la condicion y la añadimos si es "True"
        try:
            bodyBiciMarcas += esFiltro(bici, "marca" ,"cannondale")
        except TypeError:
            pass

    # Añadimos la parte final del body
    bodyBiciMarcas += '''
            </div>
        </section>'''

    return bodyBiciMarcas

# Devuelve una variable con el html del body de bicipormarca.html
def bodyMarcaHtml():

    return crearBodyMarca(listaBicis)
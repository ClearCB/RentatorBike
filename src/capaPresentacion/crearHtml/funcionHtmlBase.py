
# Esta función a raiz de una serie de parámetros, va a devolver la variable head que contiene el código html de la parte head.
def crearHtmlHead(head, titulo, descripcion, keywords, cssPath, cssLink):

    # Buscamos en la plantilla las palabras indicadas y las cambiamos por los valores de los parametros
    head=head.replace("-titulo-", titulo)
    head=head.replace("-descripcion-", descripcion)
    head=head.replace("-keywords-",keywords)
    head=head.replace("-csspath-",cssPath)
    head=head.replace("-csslink-",cssLink)
    
    return head

# Esta funcion a raiz de una serie de parámetros, va a devolver la variable header que contiene el código html de la parte del header/nav
def crearHeader(header, indexPath, path):

    # Buscamos en la plantilla las palabras indicadas y las cambiamos por los valores de los parametros
    header=header.replace("-indexpath-",indexPath)
    header=header.replace("-path-",path)

    return header

# Esta funcion se encargará de crear el contenedor de información de un "rental"
def crearContenedorRental(rental):

    # Nombramos las variables que vamos a introducir en la plantilla de los rental
    nombreRental = rental["company_name"]
    iconoRental = rental["icono"]
    direccionCalle = rental["address"]["street"]
    direccionZip = rental["address"]["zip"]
    direccionPais = rental["address"]["country"]
    direccionCiudad = rental["address"]["town"]
    contactoNum = rental["contact"]["num"]
    contactoEmail = rental["contact"]["email"]
    redesInsta = rental["social_media"]["instagram"]
    redesTwitter = rental["social_media"]["twitter"]
    bicisdisponibles = rental["bikes"]["bikes_up"]["_idbikes"]
    bicisnodisponibles = rental["bikes"]["bikes_down"]["_idbikes"]
    bicisi=""
    bicino=""

    # Por cada bici disponible, se añade el link a su respectiva página
    for bici in bicisdisponibles:

        bicisi += f" <a href='./bicissolitarias/bicissolitaria{bici}.html'>{bici}</a> "

    # Por cada bici disponible, se añade el link a su respectiva página
    for bici in bicisnodisponibles:

            bicino += f" <a href='./bicissolitarias/bicissolitaria{bici}.html'>{bici}</a> "

    fotoRental = rental["img"]

    # Introducimos las variables que nombramos anteriormente en la plantilla
    bodyRental = f'''
            <div class="rentals">
                <div class="rentals__container">
                    <div class="rentals__titulo__logo">
                        <h3 class="rentals__titulo">
                            {nombreRental} 
                        </h3>
                        <div class="rentals__logo">
                            <img  class="rentalIcono" src="{iconoRental}" alt="foto del icono del rental {nombreRental}">
                        </div>
                    </div>
                    <div class="rentals__description">
                        <ul>
                            <li>Ubicacion: {direccionCalle}, {direccionCiudad} ({direccionPais}). {direccionZip}</li>
                            <li>Contacto: num({contactoNum}) / email({contactoEmail})</li>
                            <li>Redes sociales: instagram({redesInsta}) / twitter({redesTwitter})</li>
                            <li>Bicis disponibles:{bicisi}</li>
                            <li>Bicis no disponibles:{bicino}</li>
                        </ul>
                    </div>
                    <div class="rentals__img__location">
                        <a href="#"><img class=fotoRental src="{fotoRental}" alt="foto de la ubicacion del rental {nombreRental}"></a>
                    </div>
                </div>
            </div>'''

    return bodyRental # Esta variable contiene el codigo html del rental introducido en el parámetro

# Esta función nos creará el código html de los archivos .html, le pasamos parámetros de las partes del codigo
def crearCodigoHtml(head, header, body, footer):

    # Unimos las partes del codigo html
    codigoHtml = head+header+body+footer

    return codigoHtml # Devolvemos la variable que contiene el código del archivo .html

# Funcion que determina el html de una bici en solitario
def biciSolitariaHtml(htmlBiciSolitaria, bici):

    assert isinstance(bici,dict) == True
    
    # Definimos las variables que queremos implementar en el html de la bici en solitario
    imagen = bici["img"]
    marca = bici["techinfo"]["brand"]
    tipo = bici["type"]
    id = bici["_idbike"]
    estado = bici["state"]
    groupset = bici["techinfo"]["groupset"]
    rueda = bici["techinfo"]["wheels"]
    cuadro = bici["techinfo"]["size"]
    complementos = ""
    for complemento in bici["complements"]:
        complementos += complemento+"  "
    precio = bici["prize_euros_days"]
    ubicacion = bici["where"][0]["company_name"]

    htmlBiciSolitaria = htmlBiciSolitaria.replace("-imagen-",imagen)
    htmlBiciSolitaria = htmlBiciSolitaria.replace("-marca-",marca)
    htmlBiciSolitaria = htmlBiciSolitaria.replace("-tipo-",tipo)
    htmlBiciSolitaria = htmlBiciSolitaria.replace("-id-",id)
    htmlBiciSolitaria = htmlBiciSolitaria.replace("-estado-",estado)
    htmlBiciSolitaria = htmlBiciSolitaria.replace("-groupset-",groupset)
    htmlBiciSolitaria = htmlBiciSolitaria.replace("-rueda-",rueda)
    htmlBiciSolitaria = htmlBiciSolitaria.replace("-cuadro-",cuadro)
    htmlBiciSolitaria = htmlBiciSolitaria.replace("-complementos-",complementos)
    htmlBiciSolitaria = htmlBiciSolitaria.replace("-ubicacion-",ubicacion)
    htmlBiciSolitaria = htmlBiciSolitaria.replace("-precio-",precio)

    return htmlBiciSolitaria

# Funcion que crea el contenedor del codigo html de una bicicleta
def crearContenedorBici(bici):


    # Definimos las variables que vamos a implementar
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

    # Definimos la parte final del body html
    biciBodyHtml=f'''
            <div class="container">
                <div class="img">
                    <a href="./bicissolitarias/bicissolitaria{bici["_idbike"]}.html"><img src="{imagenBici}" alt="bicicleta de la marca {marca} y tipo {tipo}"></a>
                </div>
                <div class="contenedor_info">
                    <h5>{tipo}</h5>
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
    return biciBodyHtml

# Definimos una función que nos comprueba si la bici cumple la condicion para ser añadida en el body o no.
def esFiltro(bici,campoBici, campoObjetivo):

    filtroCaractRueda = bici["techinfo"]["wheels"]
    filtroCaractGroup = bici["techinfo"]["groupset"]
    filtroCaractMarco = bici["techinfo"]["size"]
    filtroCateg = bici["type"]
    filtroMarca = bici["techinfo"]["brand"]

    if campoBici == "marca":
        filtro = filtroMarca

    elif campoBici == "categoria":
        filtro = filtroCateg

    elif campoBici == "caracteristicaRueda":
        filtro = filtroCaractRueda

    elif campoBici == "caracteristicaMarco":
        filtro = filtroCaractMarco

    elif campoBici == "caracteristicaGroup":
        filtro = filtroCaractGroup


    # Comprobamos que la bici cumple la condicion
    if campoObjetivo == filtro:

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
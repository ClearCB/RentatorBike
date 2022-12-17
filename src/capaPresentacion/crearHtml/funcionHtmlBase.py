# En este modulo vamos a definir todas las funcionalidades que van a definir y 
# estan relacionadas con la estructura común de nuestros html: "head", "header", "footer" y "nav"
# que serán llamadas desde otro modulo para printar el contenido en un archivo ".html"

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


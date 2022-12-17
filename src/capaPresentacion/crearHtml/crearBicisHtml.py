from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHeader, crearHtmlHead
from src.capaPresentacion.variables.variablesHtml import footer
from src.capaNegocio.crearArchivos import crearArchivo

# En este módulo vamos a crear funciones que van a crear un archivo "bicis.html"

# En primer lugar, creamos una función que devuelva el valor del body del bicis.html
def crearBodyBicis(listaBicis):

    # Definimos parte del body html
    bicisBodyHtml ='''
        <h3 class="titleBicis"> Bicis disponibles </h3>
        <hr>
        <section>
            <div id="contenedorPadre">'''
    
    for bici in listaBicis: # Recorremos la lista de las bicis para conseguir los valores que queremos

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
        bicisBodyHtml+=f'''
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
    
    bicisBodyHtml+='''
            </div>
        </section>'''
            

    return bicisBodyHtml

# Funcion que crear el html de bicis.html
def bicisHtml(listaBicis):

    # Vamos a unificar el html
    bicis=''''''
    bicis += crearHtmlHead("Bicis disponibles", "Página donde aparecen todas las bicicletas disponibles", "bicicletas, disponible, up, down alquilar, rental, bike","../cssStyles/","bicis")
    bicis += crearHeader("../","")
    bicis += crearBodyBicis(listaBicis)
    bicis += footer

    return bicis # Devolvemos la variable bicis que contiene el código del archivo bicis.html

# Definimos una función que ejecuta la función necesaria para crear el archivo correctamente.
def crearBicisHtml(listaBicis):

    crearArchivo(bicisHtml(listaBicis),".\\docs\\second_pages","bicis","html")

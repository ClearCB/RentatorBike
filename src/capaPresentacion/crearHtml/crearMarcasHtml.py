from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHeader, crearHtmlHead, crearFooter
from src.capaNegocio.crearArchivos import crearArchivo

# En este módulo vamos a crear funciones que van a crear un archivo "marcas.html"

# En primer lugar, creamos una función que devuelva el valor del body del marcas.html
def crearBodyMarcas():

    bodyMarcas ='''
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
    
    return bodyMarcas

# Función que construye el marcas.html y lo devuelve en una variable
def marcasHtml():
  

    marcas = ''''''
    # Añadimos cada parte del código independientemente 
    marcas += crearHtmlHead("Marcas disponibles", "Página donde aparecen un link a todas las marcas disponibles", "cube, specialized, giant, cannondale, marca, brand, alquilar, rental, bike","../cssStyles/","marcas")
    marcas += crearHeader("../","")
    marcas += crearBodyMarcas()
    marcas += crearFooter()

    return marcas # Devolvemos la variable marcas que contiene el código del archivo marcas.html

# Definimos una función que ejecuta la función necesaria para crear el archivo correctamente.
def crearMarcasHtml():

    crearArchivo(marcasHtml(),".\\docs\\second_pages","marcas","html")
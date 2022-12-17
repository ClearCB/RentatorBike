from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHeader, crearHtmlHead
from src.capaPresentacion.variables.variablesHtml import footerBase
from src.capaNegocio.crearArchivos import crearArchivo

# En este módulo vamos a crear funciones que van a crear un archivo "marcas.html"

# En primer lugar, creamos una función que devuelva el valor del body del marcas.html
def crearBodyMarcas():

    bodyMarcas ='''
        <section>
            <h3 class="titleBike">Marcas de bicicletas</h3>
            <hr>
            <div id="container">
                <a href="bicispormarca.html#cube"><div class="box"> <img src="http://imgfz.com/i/hex2z4u.png" width="200" height="200" alt="logo cube"></div></a>
                <a href="bicispormarca.html#specialized"><div class="box"><img src="http://imgfz.com/i/uDo52nq.png" width="200" height="200" alt="logo specialized"></div></a>
                <a href="bicispormarca.html#giant"><div class="box"><img src="http://imgfz.com/i/PmJ14L8.png" width="200" height="200" alt="logo giant"></div></a>
                <a href="bicispormarca.html#cannondale"><div class="box"><img src="http://imgfz.com/i/Cp5nJfo.jpeg" width="200" height="200" alt="logo cannondale"></div></a>
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
    marcas += footerBase

    return marcas # Devolvemos la variable marcas que contiene el código del archivo marcas.html

# Definimos una función que ejecuta la función necesaria para crear el archivo correctamente.
def crearMarcasHtml():

    crearArchivo(marcasHtml(),".\\docs\\second_pages","marcas","html")
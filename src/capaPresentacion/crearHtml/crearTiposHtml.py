from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHeader, crearHtmlHead, crearFooter
from src.capaNegocio.crearArchivos import crearArchivo

# En este módulo vamos a crear funciones que van a crear un archivo "tipos.html"

# En primer lugar, creamos una función que devuelva el valor del body del tipos.html
def crearBodyTipos():

    bodyTipos ='''
        <h3 class="titleBicis">Tipos de bicicletas</h3><hr>
        <section id="tiposbici">
            <div class="tiposbici_container">
                <h4>MTB</h4>
                 <div class="flex-container">
                <div class="flex-item" >
                        <a href="biciscategoria.html#mtb"><img src="{imagenBici}" alt="una imagen de una bicicleta con la categoria {categoria} de la marca {marca}" ></a>
                </div>
                <div class="flex-item">
                    <p></p>
                </div>
                </div>
            </div>
            <div class="tiposbici_container">
                <h4>MTB electrica</h4>
                 <div class="flex-container">
                <div class="flex-item" >
                    <a href="biciscategoria.html#emtb"><img src="{imagenBici}" alt="una imagen de una bicicleta con la categoria {categoria} de la marca {marca}" ></a>
                </div>
                <div class="flex-item">
                    <p></p>
                </div>
                </div>
            </div>
            <div class="tiposbici_container">
                <h4>Bici de carretera</h4>
                 <div class="flex-container">
                <div class="flex-item" >
                    <a href="biciscategoria.html#carretera"><img src="{imagenBici}" alt="una imagen de una bicicleta con la categoria {categoria} de la marca {marca}" ></a>
                </div>
                <div class="flex-item">
                    <p></p>
                </div>
                </div>
            </div>
            <div class="tiposbici_container">
                <h4>Bici de carretera electrica</h4>
                 <div class="flex-container">
                <div class="flex-item" >
                    <a href="biciscategoria.html#ecarretera"><img src="{imagenBici}" alt="una imagen de una bicicleta con la categoria {categoria} de la marca {marca}" ></a>
                </div>
                <div class="flex-item">
                    <p></p>
                </div>
                </div>
            </div>
            <div class="tiposbici_container">
                <h4>Bici de ciudad</h4>
                 <div class="flex-container">
                <div class="flex-item" >
                    <a href="biciscategoria.html#ciudad"><img src="{imagenBici}" alt="una imagen de una bicicleta con la categoria {categoria} de la marca {marca}" ></a>
                </div>
                <div class="flex-item">
                    <p></p>
                </div>
                </div>
            </div>
            <div class="tiposbici_container">
                <h4>Bici de ciudad electrica</h4>
                 <div class="flex-container">
                <div class="flex-item" >
                    <a href="biciscategoria.html#eciudad"><img src="{imagenBici}" alt="una imagen de una bicicleta con la categoria {categoria} de la marca {marca}" ></a>
                </div>
                <div class="flex-item">
                    <p></p>
                </div>
                </div>
            </div>
        </section>'''
    return bodyTipos

# Función que construye el tipos.html y lo devuelve en una variable
def tiposHtml():
   

    tipos = ''''''
    # Añadimos cada parte del código independientemente 
    tipos += crearHtmlHead("Tipos de bicicletas", "Página donde aparecen las definiciones de los principales tipos de bicicletas", "bicicletas, tipos, mtb, carretera, electrica, ciudad, alquilar, rental, bike","../cssStyles/","tipos")
    tipos += crearHeader("..\\","")
    tipos += crearBodyTipos()
    tipos += crearFooter()

    return tipos # Devolvemos la variable tipos que contiene el código del archivo tipos.html

# Definimos una función que ejecuta la función necesaria para crear el archivo correctamente.
def crearTiposHtml():

    crearArchivo(tiposHtml(),".\\docs\\second_pages","tipos","html")
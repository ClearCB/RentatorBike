from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHtmlHead, crearHeader, crearFooter
from src.capaPresentacion.crearArchivos import crearArchivo

# En este módulo vamos a crear funciones que van a crear un archivo "index.html"

# En primer lugar, creamos una función que devuelva el valor del body del index.html
def crearBodyIndex():

    bodyIndex ='''
        <hr>
        <section class="contenido">
            <div class="video_background">
                <video autoplay muted>
                    <source src="videos/production_ID_4277525.mp4" type="video/mp4">
                </video>
            </div> 
            <div class="contenedorinfo" id="rutasFamosas">
                <article class="rutas">
                    <h3>Rutas mas famosas de mallorca</h3>
                    <p> Mallorca es una lugar con unos paisajes increibles, ultimamente el ciclismo se está convirtiendo en una de las formas más agradables de visitar nuestra hermosa isla. Si quieres conocer más sobre nuestro pequeño hogar, te recomendamos que visites esta página donde aparecen rutas para bicicletas y que puedas pasar un dia estupendo. ¡Estamos ansiosos por conocerte!</p>
                    
                        <div class="linkpagina"><a href="https://mallorca-touristguide.com/las-mejores-rutas-ciclistas-de-mallorca">Ir a la pagina</a></div>
                    
                </article>
            </div>
            <div class="contenedorinfo">
                <h3>Noticias mas recientes del mundo del ciclismo</h3>
                    <iframe src="https://www.esciclismo.com/actualidad/"></iframe>
            </div>
        </section>'''

    return bodyIndex

# Función que construye el index.html y lo devuelve en una variable
def indexHtml():

    index = ''''''
    # Añadimos cada parte del código independientemente 
    index += crearHtmlHead("Rentator", "Página principal de un buscador de bicicletas para alquilar", "Bicicletas, inicio, index, alquilar, rental, bike","cssStyles/","index")
    index += crearHeader("second_pages/","")
    index += crearBodyIndex()
    index += crearFooter()

    return index # Devolvemos la variable index que contiene el código del archivo index.html

# Definimos una función que ejecuta la función necesaria para crear el archivo correctamente.
def crearIndexHtml():

    crearArchivo(indexHtml(),".\\docs","index","html")
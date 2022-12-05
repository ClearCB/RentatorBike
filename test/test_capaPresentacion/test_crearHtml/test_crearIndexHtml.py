from src.capaPresentacion.crearHtml.crearIndexHtml import crearBodyIndex, crearIndexHtml
import pytest
import os

# Estos test se encargan de comprobar que el body se crea correctamente y de comprobar que el archivo index.html existe

# Comprueba que el body se crea correctamente
@pytest.mark.test_crearBodyIndex
def test_crearBodyIndex():

    body='''
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

    assert crearBodyIndex() == body

# Comprueba que el archivo index.html se crea correctamente
@pytest.mark.test_crearIndexHtml
def test_crearIndexHtml():

    crearIndexHtml()
    assert os.path.isfile("C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\index.html") == True

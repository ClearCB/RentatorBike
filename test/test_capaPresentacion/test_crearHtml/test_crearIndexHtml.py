from src.capaPresentacion.crearHtml.crearIndexHtml import crearIndexHtml
import pytest
import os

# Estos test se encargan de comprobar que el body se crea correctamente y de comprobar que el archivo index.html existe

# # Comprueba que el body se crea correctamente
# @pytest.mark.test_crearBodyIndex
# def test_crearBodyIndex():

#     body='''
#         <hr>
#         <section class="contenido">
#             <div class="video_background">
#                 <video autoplay muted loop>
#                     <source src="https://thumbs-eu-west-1.myalbum.io/video/1k0_h264/8f0ee98f-a7e7-4463-9bb3-2b27b648d0c1.mp4" type='video/mp4'>
#                 </video>
#             </div> 
#             <div class="contenedorinfo" id="rutasFamosas">
#                 <article class="rutas">
#                     <h3>Rutas mas famosas de mallorca</h3>
#                     <p> Mallorca es una lugar con unos paisajes increibles, ultimamente el ciclismo se está convirtiendo en una de las formas más agradables de visitar nuestra hermosa isla. Si quieres conocer más sobre nuestro pequeño hogar, te recomendamos que visites esta página donde aparecen rutas para bicicletas y que puedas pasar un dia estupendo. ¡Estamos ansiosos por conocerte!</p>
                    
#                         <div class="linkpagina"><a href="https://mallorca-touristguide.com/las-mejores-rutas-ciclistas-de-mallorca">Ir a la pagina</a></div>
                    
#                 </article>
#             </div>
#             <div class="contenedorinfo">
#                 <h3>Noticias mas recientes del mundo del ciclismo</h3>
#                     <iframe src="https://www.esciclismo.com/actualidad/"></iframe>
#             </div>
#         </section>'''

    

# Comprueba que el archivo index.html se crea correctamente
@pytest.mark.test_crearIndexHtml
def test_crearIndexHtml():

    crearIndexHtml()
    ruta = os.path.relpath(".\\docs\\index.html")
    assert os.path.isfile(ruta) == True

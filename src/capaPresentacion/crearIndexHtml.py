# En este módulo vamos a crear funciones que van a crear un archivo "index.html"

from src.capaPresentacion.funcionHtmlBase import crearHtmlHead, crearHeader, crearFooter

def crearBodyIndex():

    bodyIndex ='''
        <hr>
        <section class="contenido">
            <div class="video_background">
                <video autoplay muted>
                    <source src="videos/production_ID_4277525.mp4" type="video/mp4">
                </video>
            </div> 
            <div class="contenedorinfo">
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
        </section>
        '''

    return bodyIndex

def crearIndexHtml():

    head = crearHtmlHead("Rentator", "Página principal de un buscador de bicicletas para alquilar", "Bicicletas, inicio, index, alquilar, rental, bike","cssStyles/","index")
    header = crearHeader("second_pages/")
    body = crearBodyIndex()
    footer = crearFooter()

    try:
        with open("C:\\Users\\abelc\Desktop\github\RentatorBike\docs\\index.html","w", encoding="utf-8") as archivo:
            archivo.write(head)

    except FileNotFoundError:
        print("El directorio no existe, ejecuta correctamente el programa y vuelve a intentarlo.")

    else:
        with open("C:\\Users\\abelc\Desktop\github\RentatorBike\docs\\index.html","a", encoding="utf-8") as archivo:
            archivo.write(header)
            archivo.write(body)
            archivo.write(footer)
            print("El archivo 'index.html' creado correctamente.")
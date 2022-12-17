# En este modulo vamos a localizar todas las variables con código Html que vamos a utilizar

# -------funcionHtmlBase-------

# Variable que define el código html del footer base
footerBase ='''
        <footer id="footer">
            <div class="soporte_links">
                <ul>
                    <li><a href="#">Contacto: 971621612 / rentatorsl@company.eu<br><br></a></li>
                    <li><a href="#">Soporte<br><br></a></li>
                    <li>
                        <a href="https://twitter.com/topbici"><img class="icono_red" src="http://imgfz.com/i/j9If6lw.png" alt="icono de twitter" width="20" height="20"></a>
                        <a href="https://www.instagram.com/sansebikes/?hl=es"><img class="icono_red" src="http://imgfz.com/i/4YfLF68.png" alt="icono de instagram" width="20" height="20"></a>
                    </li>
                </ul>
            </div>
            <div class="copyright_footer">
                <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">
                    <div class="footer__license__description">
                        <p>Este obra está bajo una licencia de Creative Commons Reconocimiento-Compartir. Igual 4.0 Internacional.</p>
                    </div>
                    <div class="footer__license__img">
                        <img class="copyright_img" alt="Licencia de Creative Commons" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png">
                    </div>
                </a>
            </div>
        </footer>
    </body>
</html>'''

# Variable que define el código html del head base
headBase = '''
<!DOCTYPE html>
<!-- Hemos añadido el atributo lang en la etiqueta html en lugar de hacerlo en meta porque el validador nos daba problemas -->
<html lang="es" dir="ltr">
    <head>
        <!-- La etiqueta meta la hemos obviado ya que en el footer hemos incluido una licencia de Creative Commons, sin embargo esta sería su sintaxis:  
        <meta name="copyright" content="Licencia de la empresa RentatorSL, propiedad de Gema Marquinez y Abel Casas"-->
        <title>-titulo-</title>
        <base target="_blank">
        <meta charset="UTF-8">
        <meta name="author" content="Gema Marquinez y Abel Casas">
        <meta name="description" content="-descripcion-">
        <meta name="generator" content="Visual Studio Code">
        <meta name="keywords" content="-keywords-">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="icon" type="image/png" href="https://i.ibb.co/ZNnGXHB/favicon.jpg">
        <link rel="stylesheet" type="text/css" href="-csspath-footer.css">
        <link rel="stylesheet" type="text/css" href="-csspath-header.css">
        <link rel="stylesheet" type="text/css" href="-csspath-base.css">
        <link rel="stylesheet" type="text/css" href="-csspath-nav.css">
        <link rel="stylesheet" type="text/css" href="-csspath--csslink-.css">
    </head>'''

# Variable que define el código html del header base
headerBase ='''
    <body>
        <header>
            <div class="header">
                <div class="header__logo">
                    <h1>Rentator</h1>
                    <h2>Tu Mejor Opción</h2>
                </div>
                <div class="header__nav">
                    <div class="header__links">
                        <a href="">Iniciar Sesión</a>
                        <a href="">Registrarse</a>
                    </div>
                </div>
            </div>
        </header>
        <nav id="nav">
            <ul>
                <li><a href="-indexpath-index.html">Inicio</a></li>
                <li class="bicisfiltroboton">Bicicletas
                    <ul>
                        <li><a href="-path-bicis.html">Todas las bicis</a></li>
                        <li><a href="-path-biciscategoria.html">Bicis por categoria</a></li>
                        <li><a href="-path-bicispormarca.html">Bicis por marca</a></li>
                        <li><a href="-path-biciscaracteristica.html">Bicis por caracteristicas</a></li>
                    </ul>
                </li>
                <li><a href="-path-marcas.html">Marcas</a></li>
                <li><a href="-path-rentals.html">Rentals</a></li>
            </ul>
        </nav>
        <div id="buscador">
                <form method="get" action="https://www.google.es/search">
                    <label for="search"></label>
                    <input type="text" id="search" placeholder="Buscar..." name="q" value="">
                </form>
        </div>
        <div  class="volverArriba">
            <a href="#nav" target="_self"><img class="flechaSubir" alt="flecha_arriba" src="http://imgfz.com/i/63T0IuS.png"></a>
        </div>'''


# -------crearIndexHtml-------

# Variable que define el código html del body de index.html
bodyIndex ='''
        <hr>
        <section class="contenido">
            <div class="video_background">
                <video autoplay muted loop>
                    <source src="https://thumbs-eu-west-1.myalbum.io/video/1k0_h264/8f0ee98f-a7e7-4463-9bb3-2b27b648d0c1.mp4" type='video/mp4'>
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

# -------crearMarcasHtml-------

# Variable que define el código del body de marcas.html
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

# -------crearBiciSolitariaHtml-------

# Variable del body de una bicisolitaria.html
htmlBiciSolitaria ='''
<!DOCTYPE html>
<!-- Hemos añadido el atributo lang en la etiqueta html en lugar de hacerlo en meta porque el validador nos daba problemas -->
<html lang="es" dir="ltr">
    <head>
        <!-- La etiqueta meta la hemos obviado ya que en el footer hemos incluido una licencia de Creative Commons, sin embargo esta sería su sintaxis:  
        <meta name="copyright" content="Licencia de la empresa RentatorSL, propiedad de Gema Marquinez y Abel Casas"-->
        <title>Bicis disponibles</title>
        <base target="_blank">
        <meta charset="UTF-8">
        <meta name="author" content="Gema Marquinez y Abel Casas">
        <meta name="description" content="Página donde aparece la bicicleta seleccionada y toda su informacion">
        <meta name="generator" content="Visual Studio Code">
        <meta name="keywords" content="bicicletas, disponible, up, down alquilar, rental, bike">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="icon" type="image/png" href="https://i.ibb.co/ZNnGXHB/favicon.jpg">
        <link rel="stylesheet" type="text/css" href="../../cssStyles/footer.css">
        <link rel="stylesheet" type="text/css" href="../../cssStyles/header.css">
        <link rel="stylesheet" type="text/css" href="../../cssStyles/base.css">
        <link rel="stylesheet" type="text/css" href="../../cssStyles/nav.css">
        <link rel="stylesheet" type="text/css" href="../../cssStyles/index.css">
        <link rel="stylesheet" type="text/css" href="../../cssStyles/bicisolitaria.css">
    </head>
    <body>
        <header>
            <div class="header">
                <div class="header__logo">
                    <h1>Rentator</h1>
                    <h2>Tu Mejor Opcion</h2>
                </div>
                <div class="header__nav">
                    <div class="header__links">
                        <a href="">Iniciar Sesión</a>
                        <a href="">Registrarse</a>
                    </div>
                </div>
            </div>
        </header>
        <nav id="nav">
            <ul>
                <li><a href="../../index.html">Inicio</a></li>
                <li class="bicisfiltroboton">Bicicletas
                    <ul>
                        <li><a href="../bicis.html">Todas las bicis</a></li>
                        <li><a href="../biciscategoria.html">Bicis por categoria</a></li>
                        <li><a href="../bicispormarca.html">Bicis por marca</a></li>
                        <li><a href="../biciscaracteristica.html">Bicis por caracteristicas</a></li>
                    </ul>
                </li>
                <li><a href="../marcas.html">Marcas</a></li>
                <li><a href="../rentals.html">Rentals</a></li>
            </ul>
        </nav>
        <div id="buscador">
                <form method="get" action="https://www.google.es/search">
                    <label for="search"></label>
                    <input type="text" id="search" placeholder="Buscar..." name="q" value="">
                </form>
        </div>
        <section>
            <h3 class="titleBicis">Información de la bici seleccionada</h3>
            <div class="biciinformacion">
                    <div class="img" id =img-Bike>
                        <img src="-imagen-" alt="bicicleta de la marca -marca- y catergoria -tipo-" >
                    </div>
                    <div class="descripcion">
                        <table> 
                            <tr>
                                <th>Identificador</th>
                                <th>Estado</th>
                                <th>Marca</th>
                                <th>Tipo</th>
                                <th>Groupset</th>
                                <th>Tamaño de la rueda</th>
                                <th>Tamaño del cuadro</th>
                                <th>Complementos</th>
                                <th>Precio</th>
                                <th>Ubicacion</th>
                            </tr>
                            <tr>
                                <td>-id-</td>
                                <td>-estado-</td>
                                <td>-marca-</td>
                                <td>-tipo-</td>
                                <td>-groupset-</td>
                                <td>-rueda-</td>
                                <td>-cuadro-</td>
                                <td>-complementos-</td>
                                <td>-precio-</td>
                                <td>-ubicacion-</td>
                            </tr>
                        </table>
                    </div>
            </div>
        </section>
        <footer id="footer">
            <div class="soporte_links">
                <ul>
                    <li><a href="#">Contacto: 971621612 / rentatorsl@company.eu<br><br></a></li>
                    <li><a href="#">Soporte<br><br></a></li>
                    <li>
                        <a href="https://twitter.com/topbici"><img class="icono_red" src="http://imgfz.com/i/j9If6lw.png" alt="icono de twitter" width="20" height="20"></a>
                        <a href="https://www.instagram.com/sansebikes/?hl=es"><img class="icono_red" src="http://imgfz.com/i/4YfLF68.png" alt="icono de instagram" width="20" height="20"></a>
                    </li>
                </ul>
            </div>
            <div class="copyright_footer">
                
                <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">
                    <div class="footer__license__description">
                        <p>Este obra está bajo una licencia de Creative Commons Reconocimiento-Compartir. Igual 4.0 Internacional.</p>
                    </div>

                    <div class="footer__license__img">
                        <img class="copyright_img" alt="Licencia de Creative Commons" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png">
                    </div>
                </a>
            </div>
        </footer>
    </body>
</html>'''
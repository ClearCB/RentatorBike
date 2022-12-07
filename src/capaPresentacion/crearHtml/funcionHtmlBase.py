# En este modulo vamos a definir todas las funcionalidades que van a definir y 
# estan relacionadas con la estructura común de nuestros html: "head", "header", "footer" y "nav"
# que serán llamadas desde otro modulo para printar el contenido en un archivo ".html"


# Esta función a raiz de una serie de parámetros, va a devolver la variable head que contiene el código html de la parte head.
def crearHtmlHead(titulo, descripcion, keywords, cssPath, cssLink):

    head = f'''
<!DOCTYPE html>
<!-- Hemos añadido el atributo lang en la etiqueta html en lugar de hacerlo en meta porque el validador nos daba problemas -->
<html lang="es" dir="ltr">
    <head>
        <!-- La etiqueta meta la hemos obviado ya que en el footer hemos incluido una licencia de Creative Commons, sin embargo esta sería su sintaxis:  
        <meta name="copyright" content="Licencia de la empresa RentatorSL, propiedad de Gema Marquinez y Abel Casas"-->
        <title>{titulo}</title>
        <base target="_blank">
        <meta charset="UTF-8">
        <meta name="author" content="Gema Marquinez y Abel Casas">
        <meta name="description" content="{descripcion}">
        <meta name="generator" content="Visual Studio Code">
        <meta name="keywords" content="{keywords}">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="icon" type="image/jpg" href="http://imgfz.com/i/MtOFPGk.jpeg">
        <link rel="stylesheet" type="text/css" href="{cssPath}footer.css">
        <link rel="stylesheet" type="text/css" href="{cssPath}header.css">
        <link rel="stylesheet" type="text/css" href="{cssPath}base.css">
        <link rel="stylesheet" type="text/css" href="{cssPath}nav.css">
        <link rel="stylesheet" type="text/css" href="{cssPath}{cssLink}.css">
    </head>'''
    
    return head

# Esta funcion a raiz de una serie de parámetros, va a devolver la variable header que contiene el código html de la parte del header/nav
def crearHeader(indexPath, path):

    header =f'''
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
                <li><a href="{indexPath}index.html">Inicio</a></li>
                <li class="bicisfiltroboton">Bicicletas
                    <ul>
                        <li><a href="{path}bicis.html">Todas las bicis</a></li>
                        <li><a href="{path}biciscategoria.html">Bicis por categoria</a></li>
                        <li><a href="{path}bicispormarca.html">Bicis por marca</a></li>
                        <li><a href="{path}biciscaracteristica.html">Bicis por caracteristicas</a></li>
                    </ul>
                </li>
                <li><a href="{path}marcas.html">Marcas</a></li>
                <li><a href="{path}rentals.html">Rentals</a></li>
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
    
    return header

# Esta funcion a raiz de una serie de parámetros, va a devolver la variable footer que contiene el código html de la parte del footer
def crearFooter():

    footer ='''
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
    
    return footer
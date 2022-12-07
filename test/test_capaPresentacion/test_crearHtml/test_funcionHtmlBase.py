from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHtmlHead, crearHeader, crearFooter
import pytest

# Vamos a realizar los test de las funcionalidades del modulo htmlBase para comprobar
# que se comportan como queremos


# En primer lugar, un test que nos permite comprobar que los parametros asignados se introducen en la variable head para conseguir así una función
# común a todos los archivos .html
@pytest.mark.test_crearHtmlHead
def test_crearHtmlHead():

    # Le asignamos el valor que queremos a una variable
    head = f'''
<!DOCTYPE html>
<!-- Hemos añadido el atributo lang en la etiqueta html en lugar de hacerlo en meta porque el validador nos daba problemas -->
<html lang="es" dir="ltr">
    <head>
        <!-- La etiqueta meta la hemos obviado ya que en el footer hemos incluido una licencia de Creative Commons, sin embargo esta sería su sintaxis:  
        <meta name="copyright" content="Licencia de la empresa RentatorSL, propiedad de Gema Marquinez y Abel Casas"-->
        <title>Rentator</title>
        <base target="_blank">
        <meta charset="UTF-8">
        <meta name="author" content="Gema Marquinez y Abel Casas">
        <meta name="description" content="Página principal de un buscador de bicicletas para alquilar">
        <meta name="generator" content="Visual Studio Code">
        <meta name="keywords" content="Bicicletas, inicio, index, alquilar, rental, bike">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="icon" type="image/png" href="https://i.ibb.co/ZNnGXHB/favicon.jpg">
        <link rel="stylesheet" type="text/css" href="cssStyles/footer.css">
        <link rel="stylesheet" type="text/css" href="cssStyles/header.css">
        <link rel="stylesheet" type="text/css" href="cssStyles/base.css">
        <link rel="stylesheet" type="text/css" href="cssStyles/nav.css">
        <link rel="stylesheet" type="text/css" href="cssStyles/index.css">
    </head>'''
    # Comprobamos que la función con los parámetros es igual a la variable que buscamos.
    assert crearHtmlHead("Rentator", "Página principal de un buscador de bicicletas para alquilar", "Bicicletas, inicio, index, alquilar, rental, bike", "cssStyles/", 'index') == head

# Comprobamos que la función crea un header para el index igual al que le pasamos en la variable
@pytest.mark.test_crearHeaderIndex
def test_crearHeaderIndex():

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
                <li><a href="index.html">Inicio</a></li>
                <li class="bicisfiltroboton">Bicicletas
                    <ul>
                        <li><a href="second_pages/bicis.html">Todas las bicis</a></li>
                        <li><a href="second_pages/biciscategoria.html">Bicis por categoria</a></li>
                        <li><a href="second_pages/bicispormarca.html">Bicis por marca</a></li>
                        <li><a href="second_pages/biciscaracteristica.html">Bicis por caracteristicas</a></li>
                    </ul>
                </li>
                <li><a href="second_pages/marcas.html">Marcas</a></li>
                <li><a href="second_pages/rentals.html">Rentals</a></li>
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

    assert crearHeader("", "second_pages/") ==  header

# Ahora comprobamos que si le asignamos diferentes valores, también nos devuelve el valor que deseamos
@pytest.mark.test_crearHeaderSecondPages
def test_crearHeaderSecondPages():

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
                <li><a href="../index.html">Inicio</a></li>
                <li class="bicisfiltroboton">Bicicletas
                    <ul>
                        <li><a href="bicis.html">Todas las bicis</a></li>
                        <li><a href="biciscategoria.html">Bicis por categoria</a></li>
                        <li><a href="bicispormarca.html">Bicis por marca</a></li>
                        <li><a href="biciscaracteristica.html">Bicis por caracteristicas</a></li>
                    </ul>
                </li>
                <li><a href="marcas.html">Marcas</a></li>
                <li><a href="rentals.html">Rentals</a></li>
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

    assert crearHeader("../","") ==  header

# Finalmente, comprobamos que la función nos devuelve el footer tal y como deseamos
@pytest.mark.test_crearFooter
def test_crearFooter():

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

    assert crearFooter() ==  footer
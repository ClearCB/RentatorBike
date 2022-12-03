# Vamos a realizar los test de las funcionalidades del modulo htmlBase para comprobar
# que se comportan como queremos

from src.capaPresentacion.funcionHtmlBase import crearHtmlHead, crearHeader
import pytest

# En primer lugar, un test que nos permite comprobar que los parametros asignados se introducen en la variable.

@pytest.mark.test_crearHtmlHead
def test_crearHtmlHead():

    
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
        <link rel="stylesheet" type="text/css" href="cssStyles/footer.css">
        <link rel="stylesheet" type="text/css" href="cssStyles/header.css">
        <link rel="stylesheet" type="text/css" href="cssStyles/base.css">
        <link rel="stylesheet" type="text/css" href="cssStyles/nav.css">
        <link rel="stylesheet" type="text/css" href="cssStyles/index.css">
    </head>
'''
    
    assert crearHtmlHead("Rentator", "Página principal de un buscador de bicicletas para alquilar", "Bicicletas, inicio, index, alquilar, rental, bike", "cssStyles/", 'index') == head

@pytest.mark.test_crearHeaderIndex
def test_crearHeaderIndex():

    header =f'''
    <body>
        <header>
            <div class="banner_social_network">
                <a href="https://twitter.com/topbici"><img class="icono_red" src="http://imgfz.com/i/j9If6lw.png" alt="icono de twitter" width="20" height="20"></a>
                <a href="https://www.instagram.com/sansebikes/?hl=es"><img class="icono_red" src="http://imgfz.com/i/4YfLF68.png" alt="icono de instagram" width="20" height="20"></a>
            </div>
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
                <li><a href="second_pages/tipos.html">Tipos</a></li>
                <li><a href="second_pages/rentals.html">Rentals</a></li>
            </ul>
        </nav>
            <div id="buscador">
                <form method="get" action="https://www.google.es/search">
                    <label for="search"></label>
                    <input type="text" id="search" placeholder="Buscar..." name="q" value="">
                </form>
            </div>
        <div>
            <a href="#nav" target="_self"><div class="volverarriba"><p>Volver arriba</p></div></a>
        </div>
'''

    assert crearHeader("second_pages/") ==  header

@pytest.mark.test_crearHeaderSecondPages
def test_crearHeaderSecondPages():

    header =f'''
    <body>
        <header>
            <div class="banner_social_network">
                <a href="https://twitter.com/topbici"><img class="icono_red" src="http://imgfz.com/i/j9If6lw.png" alt="icono de twitter" width="20" height="20"></a>
                <a href="https://www.instagram.com/sansebikes/?hl=es"><img class="icono_red" src="http://imgfz.com/i/4YfLF68.png" alt="icono de instagram" width="20" height="20"></a>
            </div>
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
                <li><a href="second_pages/tipos.html">Tipos</a></li>
                <li><a href="second_pages/rentals.html">Rentals</a></li>
            </ul>
        </nav>
            <div id="buscador">
                <form method="get" action="https://www.google.es/search">
                    <label for="search"></label>
                    <input type="text" id="search" placeholder="Buscar..." name="q" value="">
                </form>
            </div>
        <div>
            <a href="#nav" target="_self"><div class="volverarriba"><p>Volver arriba</p></div></a>
        </div>
'''

    assert crearHeader("second_pages/") ==  header
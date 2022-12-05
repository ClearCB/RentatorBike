from src.capaPresentacion.crearHtml.funcionHtmlBase import crearFooter, crearHeader, crearHtmlHead
from src.capaDatos.listarDatosMongo import listarBicis, respuestaText
from src.capaDatos.peticionMongo import conseguirRespuestaDatos, mongoKey, mongoUrl


def crearHtmlBiciSolitaria(bici):

    htmlBiciSolitaria = '''
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
        <link rel="stylesheet" type="text/css" href="../../cssStyles/footer.css">
        <link rel="stylesheet" type="text/css" href="../../cssStyles/header.css">
        <link rel="stylesheet" type="text/css" href="../../cssStyles/base.css">
        <link rel="stylesheet" type="text/css" href="../../cssStyles/nav.css">
        <link rel="stylesheet" type="text/css" href="../../cssStyles/index.css">
        <link rel="stylesheet" type="text/css" href="../../cssStyles/bicisolitaria.css">
    </head>
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
                <li><a href="../../index.html">Inicio</a></li>
                <li class="bicisfiltroboton">Bicicletas
                    <ul>
                        <li><a href="../bicis.html">Todas las bicis</a></li>
                        <li><a href="../biciscategoria.html">Bicis por categoria</a></li>
                        <li><a href="../bicispormarca.html">Bicis por marca</a></li>
                        <li><a href="../biciscaracteristica.html">Bicis por caracteristicas</a></li>
                    </ul>
                </li>
                <li><a href="marcas.html">Marcas</a></li>
                <li><a href="tipos.html">Tipos</a></li>
                <li><a href="rentals.html">Rentals</a></li>
            </ul>
        </nav>
        <div id="buscador">
                <form method="get" action="https://www.google.es/search">
                    <label for="search"></label>
                    <input type="text" id="search" placeholder="Buscar..." name="q" value="">
                </form>
        </div>'''

    imagen = bici["img"]
    marca = bici["techinfo"]["brand"]
    tipo = bici["type"]
    id = bici["_idbike"]
    estado = bici["state"]
    groupset = bici["techinfo"]["groupset"]
    rueda = bici["techinfo"]["wheels"]
    cuadro = bici["techinfo"]["size"]
    complementos = ""
    for complemento in bici["complements"]:
        complementos += complemento
    precio = bici["prize_euros_days"]
    ubicacion = bici["where"][0]["company_name"]

    htmlBiciSolitaria+=f'''
        <section>
            <h3>Informacion de la bici</h3>
            <div class="biciinformacion">
                    <div class="img" id =img-Bike>
                        <img src="{imagen}" alt="bicicleta de la marca {marca} y catergoria {tipo}" >
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
                                <td>{id}</td>
                                <td>{estado}</td>
                                <td>{marca}</td>
                                <td>{tipo}</td>
                                <td>{groupset}</td>
                                <td>{rueda}</td>
                                <td>{cuadro}</td>
                                <td>{complementos}</td>
                                <td>{precio}</td>
                                <td>{ubicacion}</td>
                            </tr>
                        </table>
                    </div>
            </div>
        </section>'''
    return htmlBiciSolitaria

def crearBiciSolitariaHtml(bici):

    id = bici["_idbike"]
    html = crearHtmlBiciSolitaria(bici)


    try:
        with open(f"C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\second_pages\\bicissolitarias\\bicissolitaria{id}.html","w", encoding="utf-8") as archivo:
            archivo.write(html)
            print(f"El archivo 'bicisolitaria{id}' creado correctamente.")

    except FileNotFoundError:
        print("El directorio no existe, ejecuta correctamente el programa y vuelve a intentarlo.")

def crearBicisSolitarias (listaBicis):

    for bici in listaBicis:

        crearBiciSolitariaHtml(bici)


crearBicisSolitarias(listarBicis(respuestaText(conseguirRespuestaDatos(mongoKey(),mongoUrl()))))
# # from src.capaPresentacion.crearHtml.crearBiciSolitariaHtml import biciSolitariaHtml
# # import pytest

# # # Test que comprueba que la funcion, se ejecuta correctamente y genera una variable con código html
# # # de una bicicleta en concreto
# # @pytest.mark.test_biciSolitariaHtml
# # def test_biciSolitariaHtml():

#     bici =  {
#     '_id': 'ObjectId("63850e0400b41044eddde3c7")',
#     '_idbike': 'PA0101',
#     'state': 'up',
#     'type': 'bici de ciudad',
#     'techinfo': { 'groupset': 'kask', 'size': 'x', 'wheels': '29', 'brand': 'cube' },
#     'complements': [
#       'casco',
#       'luz',
#       'bomba',
#       'guardabarros',
#       'candado',
#       'potenciometro'
#     ],
#     'prize_euros_days': '15',
#     'where': [
# {
# "_idrental":"PA01",
# "company_name":"bibike",
# "address":{
# "zip":"07006","street":"joan alcover n7  ","country":"espana","town":"palma"},
# "social_media":{
# "twitter":"@bibike","instagram":"@bibike"},
# "contact":{
# "num":"678598234","email":"bibike@contact.eu"},
# "promotions":"15% descuento",
# "stock":"2",
# 'bikes': {'bikes_up':{'_idbikes': [ 'PA0101' ]},
#         'bikes_down':{'_idbikes':['PA0102']}},
# 'img':"http://imgfz.com/i/2sS6E8d.jpeg",
# 'icono':'http://imgfz.com/i/x1Re2Mf.png'}],
#     'img':'http://imgfz.com/i/CiZJnhA.jpeg'}

#     htmlBici ='''
# <!DOCTYPE html>
# <!-- Hemos añadido el atributo lang en la etiqueta html en lugar de hacerlo en meta porque el validador nos daba problemas -->
# <html lang="es" dir="ltr">
#     <head>
#         <!-- La etiqueta meta la hemos obviado ya que en el footer hemos incluido una licencia de Creative Commons, sin embargo esta sería su sintaxis:  
#         <meta name="copyright" content="Licencia de la empresa RentatorSL, propiedad de Gema Marquinez y Abel Casas"-->
#         <title>Bicis disponibles</title>
#         <base target="_blank">
#         <meta charset="UTF-8">
#         <meta name="author" content="Gema Marquinez y Abel Casas">
#         <meta name="description" content="Página donde aparece la bicicleta seleccionada y toda su informacion">
#         <meta name="generator" content="Visual Studio Code">
#         <meta name="keywords" content="bicicletas, disponible, up, down alquilar, rental, bike">
#         <meta name="viewport" content="width=device-width, initial-scale=1.0">
#         <link rel="icon" type="image/png" href="https://i.ibb.co/ZNnGXHB/favicon.jpg">
#         <link rel="stylesheet" type="text/css" href="../../cssStyles/footer.css">
#         <link rel="stylesheet" type="text/css" href="../../cssStyles/header.css">
#         <link rel="stylesheet" type="text/css" href="../../cssStyles/base.css">
#         <link rel="stylesheet" type="text/css" href="../../cssStyles/nav.css">
#         <link rel="stylesheet" type="text/css" href="../../cssStyles/index.css">
#         <link rel="stylesheet" type="text/css" href="../../cssStyles/bicisolitaria.css">
#     </head>
#     <body>
#         <header>
#             <div class="header">
#                 <div class="header__logo">
#                     <h1>Rentator</h1>
#                     <h2>Tu Mejor Opcion</h2>
#                 </div>
#                 <div class="header__nav">
#                     <div class="header__links">
#                         <a href="">Iniciar Sesión</a>
#                         <a href="">Registrarse</a>
#                     </div>
#                 </div>
#             </div>
#         </header>
#         <nav id="nav">
#             <ul>
#                 <li><a href="../../index.html">Inicio</a></li>
#                 <li class="bicisfiltroboton">Bicicletas
#                     <ul>
#                         <li><a href="../bicis.html">Todas las bicis</a></li>
#                         <li><a href="../biciscategoria.html">Bicis por categoria</a></li>
#                         <li><a href="../bicispormarca.html">Bicis por marca</a></li>
#                         <li><a href="../biciscaracteristica.html">Bicis por caracteristicas</a></li>
#                     </ul>
#                 </li>
#                 <li><a href="../marcas.html">Marcas</a></li>
#                 <li><a href="../rentals.html">Rentals</a></li>
#             </ul>
#         </nav>
#         <div id="buscador">
#                 <form method="get" action="https://www.google.es/search">
#                     <label for="search"></label>
#                     <input type="text" id="search" placeholder="Buscar..." name="q" value="">
#                 </form>
#         </div>
#         <section>
#             <h3 class="titleBicis">Información de la bici seleccionada</h3>
#             <div class="biciinformacion">
#                     <div class="img" id =img-Bike>
#                         <img src="http://imgfz.com/i/CiZJnhA.jpeg" alt="bicicleta de la marca cube y catergoria bici de ciudad" >
#                     </div>
#                     <div class="descripcion">
#                         <table> 
#                             <tr>
#                                 <th>Identificador</th>
#                                 <th>Estado</th>
#                                 <th>Marca</th>
#                                 <th>Tipo</th>
#                                 <th>Groupset</th>
#                                 <th>Tamaño de la rueda</th>
#                                 <th>Tamaño del cuadro</th>
#                                 <th>Complementos</th>
#                                 <th>Precio</th>
#                                 <th>Ubicacion</th>
#                             </tr>
#                             <tr>
#                                 <td>PA0101</td>
#                                 <td>up</td>
#                                 <td>cube</td>
#                                 <td>bici de ciudad</td>
#                                 <td>kask</td>
#                                 <td>29</td>
#                                 <td>x</td>
#                                 <td>casco  luz  bomba  guardabarros  candado  potenciometro  </td>
#                                 <td>15</td>
#                                 <td>bibike</td>
#                             </tr>
#                         </table>
#                     </div>
#             </div>
#         </section>
#         <footer id="footer">
#             <div class="soporte_links">
#                 <ul>
#                     <li><a href="#">Contacto: 971621612 / rentatorsl@company.eu<br><br></a></li>
#                     <li><a href="#">Soporte<br><br></a></li>
#                     <li>
#                         <a href="https://twitter.com/topbici"><img class="icono_red" src="http://imgfz.com/i/j9If6lw.png" alt="icono de twitter" width="20" height="20"></a>
#                         <a href="https://www.instagram.com/sansebikes/?hl=es"><img class="icono_red" src="http://imgfz.com/i/4YfLF68.png" alt="icono de instagram" width="20" height="20"></a>
#                     </li>
#                 </ul>
#             </div>
#             <div class="copyright_footer">
                
#                 <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">
#                     <div class="footer__license__description">
#                         <p>Este obra está bajo una licencia de Creative Commons Reconocimiento-Compartir. Igual 4.0 Internacional.</p>
#                     </div>

#                     <div class="footer__license__img">
#                         <img class="copyright_img" alt="Licencia de Creative Commons" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png">
#                     </div>
#                 </a>
#             </div>
#         </footer>
#     </body>
# </html>'''

#     biciSolitariaHtml(bici) == htmlBici
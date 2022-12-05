from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHeader, crearHtmlHead, crearFooter
from src.capaPresentacion.crearCss.crearSecundarioCss import crearTiposCss

def crearBodyTipos():

    tiposBodyHtml ='''
        <h3 class="titleBicis">Tipos de bicicletas</h3><hr>
        <section id="tiposbici">
            <h4>MTB</h4>
            <div class="flex-container">
                <div class="flex-item" >
                        <a href="biciscategoria.html#mtb"><img src="{imagenBici}" alt="una imagen de una bicicleta con la categoria {categoria} de la marca {marca}" ></a>
                </div>
                <div class="flex-item">
                    <p></p>
                </div>
            </div>
            <h4>MTB electrica</h4>
            <div class="flex-container">
                <div class="flex-item" >
                    <a href="biciscategoria.html#emtb"><img src="{imagenBici}" alt="una imagen de una bicicleta con la categoria {categoria} de la marca {marca}" ></a>
                </div>
                <div class="flex-item">
                    <p></p>
                </div>
            </div>
            <h4>Bici de carretera</h4>
            <div class="flex-container">
                <div class="flex-item" >
                    <a href="biciscategoria.html#carretera"><img src="{imagenBici}" alt="una imagen de una bicicleta con la categoria {categoria} de la marca {marca}" ></a>
                </div>
                <div class="flex-item">
                    <p></p>
                </div>
            </div>
            <h4>Bici de carretera electrica</h4>
            <div class="flex-container">
                <div class="flex-item" >
                    <a href="biciscategoria.html#ecarretera"><img src="{imagenBici}" alt="una imagen de una bicicleta con la categoria {categoria} de la marca {marca}" ></a>
                </div>
                <div class="flex-item">
                    <p></p>
                </div>
            </div>
            <h4>Bici de ciudad</h4>
            <div class="flex-container">
                <div class="flex-item" >
                    <a href="biciscategoria.html#ciudad"><img src="{imagenBici}" alt="una imagen de una bicicleta con la categoria {categoria} de la marca {marca}" ></a>
                </div>
                <div class="flex-item">
                    <p></p>
                </div>
            </div>
            <h4>Bici de ciudad electrica</h4>
            <div class="flex-container">
                <div class="flex-item" >
                    <a href="biciscategoria.html#eciudad"><img src="{imagenBici}" alt="una imagen de una bicicleta con la categoria {categoria} de la marca {marca}" ></a>
                </div>
                <div class="flex-item">
                    <p></p>
                </div>
            </div>
        </section>'''
    return tiposBodyHtml

def tiposHtml():
    
    crearTiposCss()

    head = crearHtmlHead("Tipos de bicicletas", "Página donde aparecen las definiciones de los principales tipos de bicicletas", "bicicletas, tipos, mtb, carretera, electrica, ciudad, alquilar, rental, bike","../cssStyles/","tipos")
    header = crearHeader("","../")
    body = crearBodyTipos()
    footer = crearFooter()

    try:
        with open("C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\second_pages\\tipos.html","w", encoding="utf-8") as archivo:
            archivo.write(head)

    except FileNotFoundError:
        print("El directorio no existe, ejecuta correctamente el programa y vuelve a intentarlo.")

    else:
        with open("C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\second_pages\\tipos.html","a", encoding="utf-8") as archivo:
            archivo.write(header)
            archivo.write(body)
            archivo.write(footer)
            print("El archivo 'tipos.html' creado correctamente.")
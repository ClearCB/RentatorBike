from src.capaPresentacion.crearHtml.crearTiposHtml import crearBodyTipos, crearTiposHtml
import pytest
import os

# Estos test se encargan de comprobar que el body se crea correctamente y de comprobar que el archivo tipos.html existe

# Comprueba que el body se crea correctamente
@pytest.mark.test_crearBodyTipos
def test_crearBodyTipos():

    body ='''
        <h3 class="titleBicis">Tipos de bicicletas</h3><hr>
        <section id="tiposbici">
            <div class="tiposbici_container">
                <h4>MTB</h4>
                 <div class="flex-container">
                <div class="flex-item" >
                        <a href="biciscategoria.html#mtb"><img src="{imagenBici}" alt="una imagen de una bicicleta con la categoria {categoria} de la marca {marca}" ></a>
                </div>
                <div class="flex-item">
                    <p>Si buscas tu primera bicicleta de montaña, las MTB de suspensión delantera son una gran opción. Se denominan así porque sólo disponen de suspensión en la rueda delantera, llamada horquilla de suspensión. A este tipo de bicicletas también se les conoce vulgarmente como bicicletas “rígidas”.
                    Con ellas podrás optar a una gran bicicleta de MTB con componentes iguales que una de doble suspensión o incluso mejores, si comparamos de bicis rígidas de gama alta con las bicis de doble suspensión de primer precio. Pero lógicamente carece de las ventajas de las bicicletas de doble suspensión, descritas más abajo.</p>
                </div>
                </div>
            </div>
            <div class="tiposbici_container">
                <h4>MTB electrica</h4>
                 <div class="flex-container">
                <div class="flex-item" >
                    <a href="biciscategoria.html#emtb"><img src="{imagenBici}" alt="una imagen de una bicicleta con la categoria {categoria} de la marca {marca}" ></a>
                </div>
                <div class="flex-item">
                    <p>Para las personas que quieren disfrutar del MTB-e: el motor eléctrico es una excelente forma de volver a practicar deporte con suavidad para mantener la forma. Con la ayuda a tope, en los recorridos planos, el esfuerzo es comparable a ir a pie.
                    Para los que practican MTB en senderismo o sólo como actividad de ocio: una MTB eléctrica te permite completar trayectos que antes te parecían muy largos o muy exigentes tanto en el plano físico o técnico, especialmente en montaña.
                    Para los pilotos experimentados: Rodar con una MTB eléctrica es una forma de abordar su deporte desde otra perspectiva, centrándose en la conducción sin tener muy presente la condición física. Podrás rodar más rápido en las partes llanas para llegar antes a las zonas técnicas con la mejor disposición.</p>
                </div>
                </div>
            </div>
            <div class="tiposbici_container">
                <h4>Bici de carretera</h4>
                 <div class="flex-container">
                <div class="flex-item" >
                    <a href="biciscategoria.html#carretera"><img src="{imagenBici}" alt="una imagen de una bicicleta con la categoria {categoria} de la marca {marca}" ></a>
                </div>
                <div class="flex-item">
                    <p>Las bicicletas de carretera son distintas que las bicis a las que más acostumbrados estamos (a no ser que hagamos ciclismo de carretera, claro), que suelen ser más de montaña o aptas para todos los terrenos.Las de carretera no son adecuadas para circular fuera del asfalto, ya que las ruedas son completamente lisas, careciendo, por lo tanto, de agarre alguno en tierra. Además, se pincharían muy fácilmente. 
                    También son mucho más estrechas que las ruedas de una mountain bike, pues así es como aportan una mayor velocidad en carretera y un menor peso.</p>
                </div>
                </div>
            </div>
            <div class="tiposbici_container">
                <h4>Bici de carretera electrica</h4>
                 <div class="flex-container">
                <div class="flex-item" >
                    <a href="biciscategoria.html#ecarretera"><img src="{imagenBici}" alt="una imagen de una bicicleta con la categoria {categoria} de la marca {marca}" ></a>
                </div>
                <div class="flex-item">
                    <p>Una bici de pedaleo asistido gracias al montaje de un motor, una batería y sistemas electrónicos con sensores. Con estos últimos se consigue adaptar la ayuda al pedaleo del ciclista y apagarla en cuanto se alcanzan los 25 km/h. Es así el mismo sistema que las e-bikes de montaña, gravel o urbanas.
                    Por otro lado, las bicis conservan buena parte del diseño y geometría que las versiones convencionales, con un diseño generalmente Endurance o Gran Fondo. 
                    Poseen las modificaciones lógicas en el tubo diagonal y pedalier por la inclusión del motor o la batería. Pero el resto de elementos son iguales o muy similares a los de una bicicleta sin motor.</p>
                </div>
                </div>
            </div>
            <div class="tiposbici_container">
                <h4>Bici de ciudad</h4>
                 <div class="flex-container">
                <div class="flex-item" >
                    <a href="biciscategoria.html#ciudad"><img src="{imagenBici}" alt="una imagen de una bicicleta con la categoria {categoria} de la marca {marca}" ></a>
                </div>
                <div class="flex-item">
                    <p>Las bicicletas urbanas son aquellas que nos permiten circular por ciudad cómodamente y sin la necesidad de llevar la ropa específica de ciclismo, es decir, con nuestras prendas de diario. Para formar parte de este tipo de bicicletas, deben contar con una serie de características, como por ejemplo llevar cubrecadenas y guardabarros con la finalidad de no mancharnos en caso de salpicaduras. Si estás pensando en adquirir una bicicleta para ir por ciudad y quieres saber cuáles son las características de las bicicletas urbanas, no te pierdas este artículo</p>
                </div>
                </div>
            </div>
            <div class="tiposbici_container">
                <h4>Bici de ciudad electrica</h4>
                 <div class="flex-container">
                <div class="flex-item" >
                    <a href="biciscategoria.html#eciudad"><img src="{imagenBici}" alt="una imagen de una bicicleta con la categoria {categoria} de la marca {marca}" ></a>
                </div>
                <div class="flex-item">
                    <p>El uso de una bicicleta de ciudad una ‘agilidad’ legal en el uso de la bicicleta eléctrica es, de hecho, uno de sus mayores atractivos, ya que el usuario puede gozar de todos los beneficios de la electromovilidad (disfrutar del pedaleo asistido mientras utiliza un medio de transporte limpio, barato y con muy pocos costes de mantenimiento) sin tener que invertir tiempo en la realización de trámites burocráticos que, también, suponen un mayor desembolso económico. 
                    Eso sí, a la hora de circular, no es posible hacerlo por la acera, sino que están obligadas a utilizar los carriles bici si están habilitados o, en el caso de que no haya, deberán ir por la calzada como el resto de vehículos a motor.</p>
                </div>
                </div>
            </div>
        </section>'''

    assert crearBodyTipos() == body

# Comprueba que el archivo tipos.html se crea correctamente
@pytest.mark.test_crearTiposHtml
def test_crearTiposHtml():

    crearTiposHtml()
    ruta = os.path.relpath(".\\docs\\second_pages\\tipos.html")
    assert os.path.isfile(ruta) == True

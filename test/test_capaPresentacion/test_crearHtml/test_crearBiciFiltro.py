from src.capaPresentacion.crearHtml.crearBiciMarcaHtml import esFiltro, crearBodyBiciMarca, crearBiciMarcaHtml
import pytest

# Comprueba que la función ejecuta correctamente el filtro e inserta las bicis correspondientes.
@pytest.mark.test_esFiltro
def test_esFiltro():

    bici =  {
    '_id': 'ObjectId("63850e0400b41044eddde3c7")',
    '_idbike': 'PA0101',
    'state': 'up',
    'type': 'bici de ciudad',
    'techinfo': { 'groupset': 'kask', 'size': 'x', 'wheels': '29', 'brand': 'cube' },
    'complements': [
      'casco',
      'luz',
      'bomba',
      'guardabarros',
      'candado',
      'potenciometro'
    ],
    'prize_euros_days': '15',
    'where': [{"_idrental":"PA01","company_name":"bibike","address":{"zip":"07006","street":"joan alcover n7  ","country":"espana","town":"palma"},"social_media":{"twitter":"@bibike","instagram":"@bibike"},"contact":{"num":"678598234","email":"bibike@contact.eu"},"promotions":"15% descuento","stock":"2",'bikes': {'bikes_up':{'_idbikes': [ 'PA0101' ]},
        'bikes_down':{'_idbikes':['PA0102']}},'img':"http://imgfz.com/i/2sS6E8d.jpeg",'icono':'http://imgfz.com/i/x1Re2Mf.png'}],'img':'http://imgfz.com/i/CiZJnhA.jpeg'}


    biciFiltrada = '''
                <div class="container">
                    <div class="img">
                        <a href="./bicissolitarias/bicissolitariaPA0101.html"><img src="http://imgfz.com/i/CiZJnhA.jpeg" alt="bicicleta de la marca cube y tipo bici de ciudad"></a>
                    </div>
                    <div class="contenedor_info">
                        <div class="infoBike">
                            <ul> 
                                <li>Estado: up</li> 
                                <li>Marca: cube</li> 
                                <li>Groupset: kask</li> 
                                <li>Talla: x</li> 
                                <li>Tamaño de ruedas: 29</li> 
                                <li>Precio por dia: 15</li> 
                                <li>Complementos disponibles: casco luz bomba guardabarros candado potenciometro </li> 
                            </ul>
                        </div>
                        <div class="ubicationShow">
                            <p>Se ubica en bibike</p>
                        </div>
                    </div>
                </div>'''

    assert esFiltro(bici,"cube") == biciFiltrada
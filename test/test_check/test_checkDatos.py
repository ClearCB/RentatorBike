from src.check.checkDatos import respuestaCorrecta, respuestaEsModelo, checkBiciModelo, checkRentalModelo
from src.capaDatos.peticionMongo import conseguirRespuestaDatos
import pytest

# Este modulo comprobará que las funcionalidades de los check de datos detectaran correctamente

# Este test comprueba que si la respuesta no es correcta el programa devuelve False
@pytest.mark.test_respuestaCorrecta
def test_respuestaCorrecta():

    respuesta = conseguirRespuestaDatos("2Cnq4rZ0jDULrUwKEG0j8p37MVu7WMXatSXuGVjdbsc4", "https://data.mongodb-api.com/app/data-exlmr/endpoint/data/v1/action/aggregate")
    assert respuestaCorrecta(respuesta) == False

# Este test comprueba que si la respuesta transformada no es correcta el programa devuelve False
@pytest.mark.test_respuestaEsModelo
def test_respuestaEsModelo():

    listaBicis = [{},"hola",{}]
    assert respuestaEsModelo(listaBicis) == False 
    listaBicis = [{},{}]
    assert respuestaEsModelo(listaBicis) == True

# Este test comprueba que si la lista de bicis no es modelo el programa devuelve False
@pytest.mark.test_biciModelo
def test_biciModelo():

    bici1 ={"hasf"}
    bici2 ={"_idbike":"afasf","state":4}
    lista1 = [bici1,bici2]

    assert checkBiciModelo(lista1) == False

    bici3=   { "_idbike": 'CA0201',
    "state": 'up',
    "type": 'bici de carretera electrica',
    "techinfo": {
      "groupset": 'specialized',
      "size": 'm',
      "wheels": '29',
      "brand": 'cannondale'
    },
    "complements": [
      'casco',
      'luz',
      'bomba',
      'guardabarros',
      'candado',
      'potenciometro'
    ],
    "prize_euros_days": '15',
    "where": { "_idrental": 'CA02' },
    "img": 'http://imgfz.com/i/tXK4M06.jpeg'
  }
    bici4= { "_idbike": 'CA0201',
    "state": 'up',
    "type": 'bici de carretera electrica',
    "techinfo": {
      "groupset": 'specialized',
      "size": 'm',
      "wheels": '29',
      "brand": 'cannondale'
    },
    "complements": [
      'casco',
      'luz',
      'bomba',
      'guardabarros',
      'candado',
      'potenciometro'
    ],
    "prize_euros_days": '15',
    "where": { "_idrental": 'CA02' },
    "img": 'http://imgfz.com/i/tXK4M06.jpeg'
  }
    lista2= [bici3,bici4]

    assert checkBiciModelo(lista2) == True

# Este test comprueba que si la lista de rentals no es modelo el programa devuelve False
@pytest.mark.test_rentalModelo
def test_rentalModelo():

    
    rental1 ={"qwqw":2}
    rental2 ={2:1,23:4}
    lista1 = [rental1,rental2]

    assert checkRentalModelo(lista1) == False

    rental3= {
    "_idrental": 'CA02',
    "company_name": 'rentalride',
    "address": {
      "zip": '07013',
      "street": 'carrer serral n5',
      "country": 'espana',
      "town": 'calvia'
    },
    "social_media": { "twitter": '@rentalride', "instagram": '@rybrentalridem' },
    "contact": { "num": '687875483', "email": 'rentalride@contact.eu' },
    "promotions": '5% descuento',
    "stock": '1',
    "bikes":"ha",
    "img": 'http://imgfz.com/i/Rg3dPDb.jpeg',
    "icono": 'http://imgfz.com/i/I5K98Hz.png'
  }
    rental4= {
    "_idrental": 'CA02',
    "company_name": 'rentalride',
    "address": {
      "zip": '07013',
      "street": 'carrer serral n5',
      "country": 'espana',
      "town": 'calvia'
    },
    "social_media": { "twitter": '@rentalride', "instagram": '@rybrentalridem' },
    "contact": { "num": '687875483', "email": 'rentalride@contact.eu' },
    "promotions": '5% descuento',
    "stock": '1',
    "bikes":"ha",
    "img": 'http://imgfz.com/i/Rg3dPDb.jpeg',
    "icono": 'http://imgfz.com/i/I5K98Hz.png'
  }
    lista2= [rental3,rental4]

    assert checkRentalModelo(lista2) == True
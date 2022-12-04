import json

def respuestaText(respuesta):

    respuesta = respuesta.text
    respuesta = json.loads(respuesta)

    return respuesta

def listarBicis(respuesta):

    assert isinstance(respuesta,dict)
    
    try:
        listaBicis = respuesta["documents"]
    except KeyError:
        print("El documento no cumple las condiciones de uso")
    else:
        return listaBicis

def listarRentals(respuesta):

    assert isinstance(respuesta,dict)
    try:
        listaBicis = respuesta["documents"]
    except KeyError:
        print("El documento no cumple las condiciones de uso")
    else:
        listaRentals = []
        for bici in listaBicis:
            
            rental = bici["where"][0]

            if rental in listaRentals:
                continue
            else:
                listaRentals.append(rental)

    return listaRentals

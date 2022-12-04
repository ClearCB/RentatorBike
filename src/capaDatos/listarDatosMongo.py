import json

def respuestaText(respuesta):

    respuesta = respuesta.text
    respuesta = json.loads(respuesta)

    return respuesta

def listarBicis(json):

    assert isinstance(json,dict)
    
    try:
        listaBicis = json["documents"]
    except KeyError:
        print("El documento no cumple las condiciones de uso")
    else:
        return listaBicis

def listarRentals(json):

    assert isinstance(json,dict)
    try:
        listaBicis = json["documents"]
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

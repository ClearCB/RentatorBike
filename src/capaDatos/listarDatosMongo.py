from src.capaDatos.peticionMongo import mongoUrl, mongoKey, conseguirRespuestaDatos
import json

respuesta = conseguirRespuestaDatos(mongoKey(),mongoUrl())

def listarBicis():

    bicis = (respuesta.text)
    bicis = json.loads(bicis)
    listaBicis = bicis["documents"]
    return listaBicis

def listarRentals():

    bicis = (respuesta.text)
    bicis = json.loads(bicis)
    listaBicis = bicis["documents"]
    listaRentals = []
    for bici in listaBicis:
        
        rental = bici["where"][0]

        if rental in listaRentals:
            continue
        else:
            listaRentals.append(rental)

    return listaRentals
